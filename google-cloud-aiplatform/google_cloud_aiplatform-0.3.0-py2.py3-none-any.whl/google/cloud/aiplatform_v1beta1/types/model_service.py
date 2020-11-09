# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.cloud.aiplatform_v1beta1.types import io
from google.cloud.aiplatform_v1beta1.types import model as gca_model
from google.cloud.aiplatform_v1beta1.types import model_evaluation
from google.cloud.aiplatform_v1beta1.types import model_evaluation_slice
from google.cloud.aiplatform_v1beta1.types import operation
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1",
    manifest={
        "UploadModelRequest",
        "UploadModelOperationMetadata",
        "UploadModelResponse",
        "GetModelRequest",
        "ListModelsRequest",
        "ListModelsResponse",
        "UpdateModelRequest",
        "DeleteModelRequest",
        "ExportModelRequest",
        "ExportModelOperationMetadata",
        "ExportModelResponse",
        "GetModelEvaluationRequest",
        "ListModelEvaluationsRequest",
        "ListModelEvaluationsResponse",
        "GetModelEvaluationSliceRequest",
        "ListModelEvaluationSlicesRequest",
        "ListModelEvaluationSlicesResponse",
    },
)


class UploadModelRequest(proto.Message):
    r"""Request message for
    ``ModelService.UploadModel``.

    Attributes:
        parent (str):
            Required. The resource name of the Location into which to
            upload the Model. Format:
            ``projects/{project}/locations/{location}``
        model (~.gca_model.Model):
            Required. The Model to create.
    """

    parent = proto.Field(proto.STRING, number=1)

    model = proto.Field(proto.MESSAGE, number=2, message=gca_model.Model,)


class UploadModelOperationMetadata(proto.Message):
    r"""Details of
    ``ModelService.UploadModel``
    operation.

    Attributes:
        generic_metadata (~.operation.GenericOperationMetadata):
            The common part of the operation metadata.
    """

    generic_metadata = proto.Field(
        proto.MESSAGE, number=1, message=operation.GenericOperationMetadata,
    )


class UploadModelResponse(proto.Message):
    r"""Response message of
    ``ModelService.UploadModel``
    operation.

    Attributes:
        model (str):
            The name of the uploaded Model resource. Format:
            ``projects/{project}/locations/{location}/models/{model}``
    """

    model = proto.Field(proto.STRING, number=1)


class GetModelRequest(proto.Message):
    r"""Request message for
    ``ModelService.GetModel``.

    Attributes:
        name (str):
            Required. The name of the Model resource. Format:
            ``projects/{project}/locations/{location}/models/{model}``
    """

    name = proto.Field(proto.STRING, number=1)


class ListModelsRequest(proto.Message):
    r"""Request message for
    ``ModelService.ListModels``.

    Attributes:
        parent (str):
            Required. The resource name of the Location to list the
            Models from. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            The standard list filter.
        page_size (int):
            The standard list page size.
        page_token (str):
            The standard list page token. Typically obtained via
            ``ListModelsResponse.next_page_token``
            of the previous
            ``ModelService.ListModels``
            call.
        read_mask (~.field_mask.FieldMask):
            Mask specifying which fields to read.
    """

    parent = proto.Field(proto.STRING, number=1)

    filter = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)

    read_mask = proto.Field(proto.MESSAGE, number=5, message=field_mask.FieldMask,)


class ListModelsResponse(proto.Message):
    r"""Response message for
    ``ModelService.ListModels``

    Attributes:
        models (Sequence[~.gca_model.Model]):
            List of Models in the requested page.
        next_page_token (str):
            A token to retrieve next page of results. Pass to
            ``ListModelsRequest.page_token``
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    models = proto.RepeatedField(proto.MESSAGE, number=1, message=gca_model.Model,)

    next_page_token = proto.Field(proto.STRING, number=2)


class UpdateModelRequest(proto.Message):
    r"""Request message for
    ``ModelService.UpdateModel``.

    Attributes:
        model (~.gca_model.Model):
            Required. The Model which replaces the
            resource on the server.
        update_mask (~.field_mask.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see

            [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask).
    """

    model = proto.Field(proto.MESSAGE, number=1, message=gca_model.Model,)

    update_mask = proto.Field(proto.MESSAGE, number=2, message=field_mask.FieldMask,)


class DeleteModelRequest(proto.Message):
    r"""Request message for
    ``ModelService.DeleteModel``.

    Attributes:
        name (str):
            Required. The name of the Model resource to be deleted.
            Format:
            ``projects/{project}/locations/{location}/models/{model}``
    """

    name = proto.Field(proto.STRING, number=1)


class ExportModelRequest(proto.Message):
    r"""Request message for
    ``ModelService.ExportModel``.

    Attributes:
        name (str):
            Required. The resource name of the Model to export. Format:
            ``projects/{project}/locations/{location}/models/{model}``
        output_config (~.model_service.ExportModelRequest.OutputConfig):
            Required. The desired output location and
            configuration.
    """

    class OutputConfig(proto.Message):
        r"""Output configuration for the Model export.

        Attributes:
            export_format_id (str):
                The ID of the format in which the Model must be exported.
                Each Model lists the [export formats it
                supports][google.cloud.aiplatform.v1beta1.Model.supported_export_formats].
                If no value is provided here, then the first from the list
                of the Model's supported formats is used by default.
            artifact_destination (~.io.GcsDestination):
                The Google Cloud Storage location where the Model artifact
                is to be written to. Under the directory given as the
                destination a new one with name
                "``model-export-<model-display-name>-<timestamp-of-export-call>``",
                where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601
                format, will be created. Inside, the Model and any of its
                supporting files will be written. This field should only be
                set when
                [Models.supported_export_formats.exportable_contents]
                contains ARTIFACT.
            image_destination (~.io.ContainerRegistryDestination):
                The Google Container Registry or Artifact Registry uri where
                the Model container image will be copied to. This field
                should only be set when
                [Models.supported_export_formats.exportable_contents]
                contains IMAGE.
        """

        export_format_id = proto.Field(proto.STRING, number=1)

        artifact_destination = proto.Field(
            proto.MESSAGE, number=3, message=io.GcsDestination,
        )

        image_destination = proto.Field(
            proto.MESSAGE, number=4, message=io.ContainerRegistryDestination,
        )

    name = proto.Field(proto.STRING, number=1)

    output_config = proto.Field(proto.MESSAGE, number=2, message=OutputConfig,)


class ExportModelOperationMetadata(proto.Message):
    r"""Details of
    ``ModelService.ExportModel``
    operation.

    Attributes:
        generic_metadata (~.operation.GenericOperationMetadata):
            The common part of the operation metadata.
        output_info (~.model_service.ExportModelOperationMetadata.OutputInfo):
            Output only. Information further describing
            the output of this Model export.
    """

    class OutputInfo(proto.Message):
        r"""Further describes the output of the ExportModel. Supplements
        ``ExportModelRequest.OutputConfig``.

        Attributes:
            artifact_output_uri (str):
                Output only. If the Model artifact is being
                exported to Google Cloud Storage this is the
                full path of the directory created, into which
                the Model files are being written to.
            image_output_uri (str):
                Output only. If the Model image is being
                exported to Google Container Registry or
                Artifact Registry this is the full path of the
                image created.
        """

        artifact_output_uri = proto.Field(proto.STRING, number=2)

        image_output_uri = proto.Field(proto.STRING, number=3)

    generic_metadata = proto.Field(
        proto.MESSAGE, number=1, message=operation.GenericOperationMetadata,
    )

    output_info = proto.Field(proto.MESSAGE, number=2, message=OutputInfo,)


class ExportModelResponse(proto.Message):
    r"""Response message of
    ``ModelService.ExportModel``
    operation.
    """


class GetModelEvaluationRequest(proto.Message):
    r"""Request message for
    ``ModelService.GetModelEvaluation``.

    Attributes:
        name (str):
            Required. The name of the ModelEvaluation resource. Format:

            ``projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}``
    """

    name = proto.Field(proto.STRING, number=1)


class ListModelEvaluationsRequest(proto.Message):
    r"""Request message for
    ``ModelService.ListModelEvaluations``.

    Attributes:
        parent (str):
            Required. The resource name of the Model to list the
            ModelEvaluations from. Format:
            ``projects/{project}/locations/{location}/models/{model}``
        filter (str):
            The standard list filter.
        page_size (int):
            The standard list page size.
        page_token (str):
            The standard list page token. Typically obtained via
            ``ListModelEvaluationsResponse.next_page_token``
            of the previous
            ``ModelService.ListModelEvaluations``
            call.
        read_mask (~.field_mask.FieldMask):
            Mask specifying which fields to read.
    """

    parent = proto.Field(proto.STRING, number=1)

    filter = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)

    read_mask = proto.Field(proto.MESSAGE, number=5, message=field_mask.FieldMask,)


class ListModelEvaluationsResponse(proto.Message):
    r"""Response message for
    ``ModelService.ListModelEvaluations``.

    Attributes:
        model_evaluations (Sequence[~.model_evaluation.ModelEvaluation]):
            List of ModelEvaluations in the requested
            page.
        next_page_token (str):
            A token to retrieve next page of results. Pass to
            ``ListModelEvaluationsRequest.page_token``
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    model_evaluations = proto.RepeatedField(
        proto.MESSAGE, number=1, message=model_evaluation.ModelEvaluation,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class GetModelEvaluationSliceRequest(proto.Message):
    r"""Request message for
    ``ModelService.GetModelEvaluationSlice``.

    Attributes:
        name (str):
            Required. The name of the ModelEvaluationSlice resource.
            Format:

            ``projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}/slices/{slice}``
    """

    name = proto.Field(proto.STRING, number=1)


class ListModelEvaluationSlicesRequest(proto.Message):
    r"""Request message for
    ``ModelService.ListModelEvaluationSlices``.

    Attributes:
        parent (str):
            Required. The resource name of the ModelEvaluation to list
            the ModelEvaluationSlices from. Format:

            ``projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}``
        filter (str):
            The standard list filter.

            -  ``slice.dimension`` - for =.
        page_size (int):
            The standard list page size.
        page_token (str):
            The standard list page token. Typically obtained via
            ``ListModelEvaluationSlicesResponse.next_page_token``
            of the previous
            ``ModelService.ListModelEvaluationSlices``
            call.
        read_mask (~.field_mask.FieldMask):
            Mask specifying which fields to read.
    """

    parent = proto.Field(proto.STRING, number=1)

    filter = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)

    read_mask = proto.Field(proto.MESSAGE, number=5, message=field_mask.FieldMask,)


class ListModelEvaluationSlicesResponse(proto.Message):
    r"""Response message for
    ``ModelService.ListModelEvaluationSlices``.

    Attributes:
        model_evaluation_slices (Sequence[~.model_evaluation_slice.ModelEvaluationSlice]):
            List of ModelEvaluations in the requested
            page.
        next_page_token (str):
            A token to retrieve next page of results. Pass to
            ``ListModelEvaluationSlicesRequest.page_token``
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    model_evaluation_slices = proto.RepeatedField(
        proto.MESSAGE, number=1, message=model_evaluation_slice.ModelEvaluationSlice,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


__all__ = tuple(sorted(__protobuf__.manifest))
