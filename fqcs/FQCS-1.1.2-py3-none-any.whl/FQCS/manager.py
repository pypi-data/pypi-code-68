import numpy as np
from . import detector, helper, fqcs_api, fqcs_constants
import os
import asyncio
import cv2

COMPARE_FACTOR = 1.5


class FQCSManager:
    def __init__(self, config_folder=None):
        self.__config_folder = config_folder
        if config_folder is None:
            configs = {}
        else:
            configs = detector.load_json_cfg(config_folder)
        self.__configs = configs
        self.__model = None
        self.__sample_area = None
        self.__sample_left = None
        self.__sample_right = None
        self.__last_group_count = 0
        self.__last_check_min_x = None
        self.__speed = 1
        return

    def load_sample_images(self):
        self.__sample_left_path = self.get_sample_path(True)
        self.__sample_right_path = self.get_sample_path(False)
        if os.path.exists(self.__sample_left_path):
            self.__sample_left = cv2.imread(self.__sample_left_path)
            self.__sample_right = cv2.imread(self.__sample_right_path)
            self.__sample_area = self.__sample_left.shape[
                0] * self.__sample_left.shape[1]

    def get_sample_path(self, is_left):
        if is_left:
            return os.path.join(self.__config_folder,
                                detector.SAMPLE_LEFT_FILE)
        return os.path.join(self.__config_folder, detector.SAMPLE_RIGHT_FILE)

    def get_configs(self):
        return self.__configs

    def get_sample_left(self):
        return self.__sample_left

    def get_sample_right(self):
        return self.__sample_right

    def get_last_check_min_x(self):
        return self.__last_check_min_x

    def get_last_group_count(self):
        return self.__last_group_count

    def check_group(self, check_group_idx, final_grouped):
        check_group = final_grouped[check_group_idx]
        check_group_min_x = self.get_min_x(check_group)
        self.__last_check_min_x = check_group_min_x
        self.__speed = 1

    def group_pairs(self, boxes):
        max_seperated_area = self.__sample_area * COMPARE_FACTOR if self.__sample_area is not None else None
        grouped = []
        sizes = []
        boxes_count = len(boxes)
        not_sep_count = 0
        for i in reversed(range(0, boxes_count)):
            b = boxes[i]
            c, rect, dimA, dimB, box, tl, tr, br, bl, minx, maxx, cenx = b
            grouped.append([b])
            sizes.append(maxx - minx)
            area = dimA * dimB
            if max_seperated_area is not None and area >= max_seperated_area:
                not_sep_count += 1
            next_idx = i - 1
            if next_idx > -1:
                next_box = boxes[next_idx]
                minx = next_box[-3]
                grouped.append([b])
                grouped[-1].append(next_box)
                sizes.append(maxx - minx)

        check_group = None
        group_count = len(grouped)
        final_grouped = []
        final_sizes = []
        final_status = []
        if group_count == 0:
            group_count = len(final_grouped)
            self.__last_group_count = group_count
            return final_grouped, final_sizes, final_status, check_group
        max_size = np.max(sizes)
        min_size = np.min(sizes)
        range_size = (max_size, max_size)
        if group_count < 3:
            range_size = None
        elif group_count + not_sep_count > 3:
            range_size = self.__devide_range_size(sizes, group_count)
        # print("Sizes:", range_size, min_size, max_size)
        # print("------------------------")
        tmp_last_check_min_x = self.__last_check_min_x
        for i, g in enumerate(grouped):
            # print("Group", i, len(g), sizes[i])
            status = self.__calc_status(g)
            if status: tmp_last_check_min_x = self.get_min_x(g)
            if (range_size is None or
                (sizes[i] >= range_size[0] and sizes[i] <= range_size[1])
                    and self.__is_same_status(g)):
                final_grouped.append(g)
                final_sizes.append(sizes[i])
                final_status.append(status)
                if not status and check_group is None:
                    check_group = len(final_grouped) - 1
        if tmp_last_check_min_x is not None and self.__last_check_min_x is not None:
            tmp_speed = tmp_last_check_min_x - self.__last_check_min_x
            if tmp_speed <= 0:
                tmp_last_check_min_x += self.__speed
            else:
                self.__speed = tmp_speed
        self.__last_check_min_x = tmp_last_check_min_x

        # print("--------- FINAL --------")
        # for i, g in enumerate(final_grouped):
        #     print("Group", i, len(g), final_sizes[i])

        group_count = len(final_grouped)
        self.__last_group_count = group_count
        return final_grouped, final_sizes, final_status, check_group

    def __calc_status(self, group):
        final_cen_x = self.__get_cen_x(group)
        return self.__last_check_min_x is not None and final_cen_x > self.__last_check_min_x

    def __is_same_status(self, group):
        last_stt = None
        for b in group:
            cur_stt = self.__calc_status([b])
            if last_stt is None:
                last_stt = cur_stt
            else:
                return last_stt == cur_stt
        return True

    def __devide_range_size(self, sizes, group_count):
        sizes = sorted(sizes)
        diffs = []
        max_1, max_2 = 0, 0
        range_1, range_2 = None, None
        for i in range(group_count - 1):
            diff = sizes[i + 1] - sizes[i]
            if diff > max_1:
                max_2 = max_1
                max_1 = diff
                range_2 = range_1
                range_1 = (sizes[i], sizes[i + 1])
            elif diff > max_2:
                max_2 = diff
                range_2 = (sizes[i], sizes[i + 1])
        min_1 = np.min(range_1)
        min_2 = np.min(range_2)
        if min_1 < min_2:
            return (range_1[1], range_2[0])
        return (range_2[1], range_1[0])

    def get_min_x(self, group):
        final_min_x = None
        for b in group:
            c, rect, dimA, dimB, box, tl, tr, br, bl, minx, maxx, cenx = b
            if final_min_x is None or minx < final_min_x:
                final_min_x = minx
        return final_min_x

    def __get_cen_x(self, group):
        final_cen_x = None
        for b in group:
            c, rect, dimA, dimB, box, tl, tr, br, bl, minx, maxx, cenx = b
            if final_cen_x is None or cenx < final_cen_x:
                final_cen_x = cenx
        return final_cen_x

    async def load_model(self, cam_cfg):
        err_cfg = cam_cfg["err_cfg"]
        weights = err_cfg["weights"]
        if weights is None or not os.path.exists(weights): return
        model = await detector.get_yolov4_model(
            inp_shape=err_cfg["inp_shape"],
            num_classes=err_cfg["num_classes"],
            training=False,
            yolo_max_boxes=err_cfg["yolo_max_boxes"],
            yolo_iou_threshold=err_cfg["yolo_iou_threshold"],
            weights=err_cfg["weights"],
            yolo_score_threshold=err_cfg["yolo_score_threshold"])
        self.__model = model

    def get_find_cnt_func(self, cam_cfg):
        find_contours_func = detector.get_find_contours_func_by_method(
            cam_cfg["detect_method"])
        return find_contours_func

    # MAIN
    def extract_boxes(self, cam_cfg, resized_image):
        frame_width, frame_height = cam_cfg["frame_width"], cam_cfg[
            "frame_height"]
        min_width, min_height = cam_cfg["min_width_per"], cam_cfg[
            "min_height_per"]
        min_width, min_height = frame_width * min_width, frame_height * min_height

        # return
        find_contours_func = self.get_find_cnt_func(cam_cfg)
        d_cfg = cam_cfg['d_cfg']

        # adjust thresh
        if (cam_cfg["detect_method"] == "thresh"):
            adj_thresh = d_cfg["light_adj_thresh"]
            if adj_thresh is not None and adj_thresh > 0:
                adj_bg_thresh = helper.adjust_thresh_by_brightness(
                    resized_image, d_cfg["light_adj_thresh"],
                    d_cfg["bg_thresh"])
            else:
                adj_bg_thresh = d_cfg["bg_thresh"]
            d_cfg["adj_bg_thresh"] = adj_bg_thresh
        elif (cam_cfg["detect_method"] == "range"):
            adj_thresh = d_cfg["light_adj_thresh"]
            if adj_thresh is not None and adj_thresh > 0:
                adj_cr_to = helper.adjust_crange_by_brightness(
                    resized_image, d_cfg["light_adj_thresh"], d_cfg["cr_to"])
                d_cfg["adj_cr_to"] = adj_cr_to
            else:
                d_cfg["adj_cr_to"] = d_cfg["cr_to"]

        # return
        boxes, proc = detector.find_contours_and_box(
            resized_image,
            find_contours_func,
            d_cfg,
            min_width=min_width,
            min_height=min_height,
            detect_range=cam_cfg['detect_range'])

        return boxes, proc

    def detect_pair_side_cam(self, cam_cfg, boxes, image_detect):
        find_contours_func = self.get_find_cnt_func(cam_cfg)
        pair, image_detect = detector.detect_pair_side_cam(
            image_detect, find_contours_func, cam_cfg["d_cfg"], boxes)
        return pair, image_detect

    def detect_groups_and_checked_pair(self, cam_cfg, boxes, resized_image):
        final_grouped, _, _, check_group_idx = self.group_pairs(boxes)
        find_contours_func = self.get_find_cnt_func(cam_cfg)
        d_cfg = cam_cfg['d_cfg']

        # return
        pair, split_left, split_right, image_detect = None, None, None, None
        check_group = None
        if check_group_idx is not None:
            check_group = final_grouped[check_group_idx]
            image_detect = resized_image.copy()
            pair, image_detect, split_left, split_right, check_group = detector.detect_pair_and_size(
                image_detect,
                find_contours_func,
                d_cfg,
                check_group,
                stop_condition=cam_cfg['stop_condition'])
            final_grouped[check_group_idx] = check_group

        # output
        per_10px = cam_cfg["length_per_10px"]
        # return
        sizes = []
        for idx, group in enumerate(final_grouped):
            sizes.append([])
            for b in group:
                c, rect, dimA, dimB, box, tl, tr, br, bl, minx, maxx, cenx = b
                if per_10px is not None:
                    lH, lW = helper.calculate_length(
                        dimA,
                        per_10px), helper.calculate_length(dimB, per_10px)
                    sizes[-1].append((lH, lW))
                else:
                    sizes[-1].append((dimA, dimB))
        return final_grouped, sizes, check_group_idx, pair, split_left, split_right, image_detect

    def compare_size(self, cam_cfg, check_size):
        h_diff, w_diff = detector.compare_size(check_size[0], check_size[1],
                                               cam_cfg)
        return h_diff, w_diff

    def preprocess(self, cam_cfg, image, is_left):
        c_cfg = cam_cfg['color_cfg']
        if is_left:
            image = detector.preprocess_for_color_diff(
                image, c_cfg['img_size'], c_cfg['blur_val'], c_cfg['alpha_l'],
                c_cfg['beta_l'], c_cfg['sat_adj'])
        else:
            image = detector.preprocess_for_color_diff(
                image, c_cfg['img_size'], c_cfg['blur_val'], c_cfg['alpha_r'],
                c_cfg['beta_r'], c_cfg['sat_adj'])
        return image

    def preprocess_images(self, cam_cfg, left_img, right_img):
        # start
        pre_sample_left = self.preprocess(cam_cfg, self.__sample_left, True)
        pre_sample_right = self.preprocess(cam_cfg, self.__sample_right, False)
        pre_left = self.preprocess(cam_cfg, left_img, True)
        pre_right = self.preprocess(cam_cfg, right_img, False)
        return pre_left, pre_right, pre_sample_left, pre_sample_right

    def detect_asym(self, cam_cfg, pre_left, pre_right, pre_sample_left,
                    pre_sample_right):
        # Similarity compare
        sim_cfg = cam_cfg["sim_cfg"]
        asym_left_task = asyncio.create_task(
            detector.detect_asym_diff(
                pre_left, pre_sample_left, sim_cfg['segments_list'],
                sim_cfg['C1'], sim_cfg['C2'], sim_cfg['psnr_trigger'],
                sim_cfg['asym_amp_thresh'], sim_cfg['asym_amp_rate'],
                sim_cfg['re_calc_factor_left'], sim_cfg['min_similarity']))
        asym_right_task = asyncio.create_task(
            detector.detect_asym_diff(
                pre_right, pre_sample_right, sim_cfg['segments_list'],
                sim_cfg['C1'], sim_cfg['C2'], sim_cfg['psnr_trigger'],
                sim_cfg['asym_amp_thresh'], sim_cfg['asym_amp_rate'],
                sim_cfg['re_calc_factor_right'], sim_cfg['min_similarity']))
        return asym_left_task, asym_right_task

    def detect_errors(self, cam_cfg, images):
        err_cfg = cam_cfg["err_cfg"]
        err_task = asyncio.create_task(
            detector.detect_errors(self.__model, images, err_cfg["img_size"]))
        return err_task

    def compare_colors(self, cam_cfg, pre_left, pre_right, pre_sample_left,
                       pre_sample_right):
        c_cfg = cam_cfg["color_cfg"]
        left_coroutine, right_coroutine = detector.detect_color_difference(
            pre_left, pre_right, pre_sample_left, pre_sample_right,
            c_cfg['amplify_thresh'], c_cfg['supp_thresh'],
            c_cfg['amplify_rate'], c_cfg['max_diff'])
        left_task = asyncio.create_task(left_coroutine)
        right_task = asyncio.create_task(right_coroutine)
        return left_task, right_task
