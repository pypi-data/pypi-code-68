import base64
import csv
import glob
import hashlib
import os
import uuid
import json
import boto3
from botocore.exceptions import ClientError
from django.utils.text import slugify

from PIL import Image, ImageOps
import StringIO

# import settings
from tasq_cli.db import UploadsDatabase
# from utils import timestamp_for_file_name

logger = None

def upload_file(dataset_name, db, settings, client, file_name_with_path, leaf_path):
    # TODO only tested on unix systems
    file_path, file_name = os.path.split(file_name_with_path)
    relative_file_path = f'{leaf_path}{file_path.split(leaf_path)[-1]}'.replace('-', '_')
    ext = file_name.split('.')[-1]

    object_name = f'client_{settings.CLIENT_ID}/{relative_file_path}/{uuid.uuid4().hex}.{ext}'
    logger.info(f'upload file name is {object_name}')
    logger.debug(f'Checking if file needs to be uploaded ...')

    # before upload check if file exists on server under this dataset
    with open(f'{file_path}/{file_name}', 'rb') as infile:
        # if file is png, jpg, or jpeg - rotate
        if ext in ['png', 'jpg', 'jpeg']:
            image = Image.open(infile)
            transposed_image = ImageOps.exif_transpose(image)
            image_wrapper = StringIO.StringIO()
            transposed_image.save(image_wrapper, ext)
        else:
            transposed_image = infile

        md5 = hashlib.md5(transposed_image.read())
        transposed_image.seek(0)
        content_md5 = base64.b64encode(md5.digest()).decode('utf-8')
        md5_hash = md5.hexdigest()

        logger.debug(f'File hash: {md5_hash}')
        uploaded_entry = db.get_upload(dataset_name, md5_hash)

        if uploaded_entry:
            logger.debug(f'\tFile with hash {md5_hash} is already uploaded to dataset {dataset_name}.')
            return uploaded_entry

        logger.info(f'\tUploading to {settings.BUCKET} as {object_name} ...')
        try:
            upload_entry = {
                    'bucket': settings.BUCKET,
                    'dataset_name': dataset_name,
                    'file_name': f'{relative_file_path}/{file_name}',
                    'object_name': object_name,
                    'md5_hash': md5_hash,
                    'url': f'https://{settings.BUCKET}.s3.amazonaws.com/{object_name}',
                    'cdn_url': settings.CDN_URL.format(object_name=object_name),
                }
            if not settings.dry:
                response = client.put_object(
                    Body=image_wrapper,
                    Bucket=settings.BUCKET,
                    Key=object_name,
                    ContentMD5=content_md5,
                    # TODO this is questionable
                    # we might not want to make these
                    # public in the long term
                    ACL='public-read'
                    # NOTE
                    # consider that sync might work faster than put_object
                )
                if response['ResponseMetadata']['HTTPStatusCode'] == 200 and response['ETag'] == f'"{md5_hash}"':
                    tag_response = client.put_object_tagging(
                        Bucket=settings.BUCKET,
                        Key=object_name,
                        Tagging={
                            'TagSet': [
                                {
                                    'Key': 'original_name',
                                    'Value': slugify(file_name)
                                },
                            ]
                        }
                    )
                    
                    return upload_entry
                else:
                    logger.error(response)
                    return None
            else:
                return upload_entry
        except ClientError as e:
            logger.error(e)
            return None
        return None


def get_files(dir_path, excluded_extensions):
    files = []
    logger.info(excluded_extensions)
    if len(excluded_extensions) > 1:
        glob_ending = f'!(**.{"|**.".join(excluded_extensions)})'
    else:
        glob_ending = '**'
    # files.extend(glob.glob(f'{dir_path}/{glob_ending}', recursive=True))
    # NOTE
    # The above glob patterns excludes things when run with ls in bash,
    # but for some reason it won't work through python. Check it out by uncommenting:
    #
    # logger.info(f'ls {dir_path}/{glob_ending}')
    #
    # That is why we run a dumb glob and a list comprehension to exclude all
    # the files we don't like.
    files.extend(glob.glob(f'{dir_path}/**', recursive=True))
    filtered_files = [f for f in files 
        if (f.split('.')[-1] not in excluded_extensions) and not os.path.isdir(f)]

    return filtered_files

def do_upload(dataset_name, search_path, exclude, settings):
    global logger
    logger = settings.get_logger()
    if exclude:
        if len(exclude) > 0:
            excluded_extensions = [ext[0] for ext in exclude]
    else:
        excluded_extensions = []

    client = boto3.client(
        's3',
        aws_access_key_id=settings.ACCESS_KEY,
        aws_secret_access_key=settings.SECRET_KEY,
    )

    logger.info(f'Using access key {settings.ACCESS_KEY[:3]}*********{settings.ACCESS_KEY[-3:]} and secret {settings.SECRET_KEY[:3]}*********{settings.SECRET_KEY[-3:]}.')

    db = UploadsDatabase()

    leaf_path = os.path.basename(os.path.normpath(search_path))
    added_files = []

    files = get_files(search_path, excluded_extensions)
    num_files = len(files)
    logger.info(f'Found {num_files} files.')

    for i, file_name in enumerate(files):
        logger.info(f'Uploading file [{i + 1}/{num_files}] {file_name} {settings.BUCKET}')
        upload_entry = upload_file(dataset_name, db, settings, client, file_name, leaf_path) 
        if not upload_entry:
            db.close()
            exit(1)
        else:
            added_files.append(upload_entry)
            if not settings.dry:
                db.insert_upload(**upload_entry)
    db.close()

    # write out image urls to csv
    os.makedirs("./out/", exist_ok=True)

    csv_rows = [
        [
            settings.CDN_URL.format(object_name=uploaded_entry['object_name']), # object_name
            json.dumps({'file_name': uploaded_entry['file_name']}), # object
            # uploaded_entry['file_name'], # file_name
        ] for uploaded_entry in added_files]

    # NOTE
    # the csv output used to contain a full timestamp
    # with open(f'./out/{dataset_name}_{timestamp_for_file_name()}.csv', 'w') as csvfile:
    with open(f'./out/{dataset_name}.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, dialect='unix')
        csvwriter.writerows(csv_rows)

def create_csv_from_currently_uploaded_files(dataset_name, file_name, settings):
    db = UploadsDatabase()
    global logger
    logger = settings.get_logger()

    if not dataset_name:
        if not file_name:
            logger.error('No dataset_name or example file_name was provided.')
            return
        res = get_dataset_name(db, file_name)
        if not res:
            logger.error('No such file was uploaded.')
            return
        dataset_name = res[0]

    entries = db.get_uploaded_files_by_dataset_name(dataset_name)
    row_values = {'file_name': 0, 'cdn_url': 1}
    csv_rows = [
        [
            entry[row_values['cdn_url']],
            json.dumps({'file_name': entry[row_values['file_name']]}),  # object
        ] for entry in entries]
    if not os.path.exists('./out/'):
        os.makedirs('./out')
    with open(f'./out/{dataset_name}.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, dialect='unix')
        csvwriter.writerows(csv_rows)


def get_dataset_name(db, file_name):
    file_path, file_name = os.path.split(file_name)
    leaf_path = os.path.basename(os.path.normpath(file_path))
    relative_file_path = f'{leaf_path}{file_path.split(leaf_path)[-1]}'.replace('-', '_')
    res = db.get_dataset_name_by_filename(f'{relative_file_path}/{file_name}')
    return res
