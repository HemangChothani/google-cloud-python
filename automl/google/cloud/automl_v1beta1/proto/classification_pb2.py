# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/classification.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/classification.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_pb=_b(
        '\n6google/cloud/automl_v1beta1/proto/classification.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto")\n\x18\x43lassificationAnnotation\x12\r\n\x05score\x18\x01 \x01(\x02"\x9d\x05\n\x1f\x43lassificationEvaluationMetrics\x12\x0e\n\x06\x61u_prc\x18\x01 \x01(\x02\x12\x13\n\x0b\x62\x61se_au_prc\x18\x02 \x01(\x02\x12u\n\x18\x63onfidence_metrics_entry\x18\x03 \x03(\x0b\x32S.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry\x12\x66\n\x10\x63onfusion_matrix\x18\x04 \x01(\x0b\x32L.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix\x12\x1a\n\x12\x61nnotation_spec_id\x18\x05 \x03(\t\x1a\xac\x01\n\x16\x43onfidenceMetricsEntry\x12\x1c\n\x14\x63onfidence_threshold\x18\x01 \x01(\x02\x12\x0e\n\x06recall\x18\x02 \x01(\x02\x12\x11\n\tprecision\x18\x03 \x01(\x02\x12\x10\n\x08\x66\x31_score\x18\x04 \x01(\x02\x12\x12\n\nrecall_at1\x18\x05 \x01(\x02\x12\x15\n\rprecision_at1\x18\x06 \x01(\x02\x12\x14\n\x0c\x66\x31_score_at1\x18\x07 \x01(\x02\x1a\xaa\x01\n\x0f\x43onfusionMatrix\x12\x1a\n\x12\x61nnotation_spec_id\x18\x01 \x03(\t\x12]\n\x03row\x18\x02 \x03(\x0b\x32P.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.Row\x1a\x1c\n\x03Row\x12\x15\n\rexample_count\x18\x01 \x03(\x05*Y\n\x12\x43lassificationType\x12#\n\x1f\x43LASSIFICATION_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nMULTICLASS\x10\x01\x12\x0e\n\nMULTILABEL\x10\x02\x42\x97\x01\n\x1f\x63om.google.cloud.automl.v1beta1B\x13\x43lassificationProtoZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1b\x06proto3'
    ),
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)

_CLASSIFICATIONTYPE = _descriptor.EnumDescriptor(
    name="ClassificationType",
    full_name="google.cloud.automl.v1beta1.ClassificationType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CLASSIFICATION_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="MULTICLASS", index=1, number=1, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MULTILABEL", index=2, number=2, options=None, type=None
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=832,
    serialized_end=921,
)
_sym_db.RegisterEnumDescriptor(_CLASSIFICATIONTYPE)

ClassificationType = enum_type_wrapper.EnumTypeWrapper(_CLASSIFICATIONTYPE)
CLASSIFICATION_TYPE_UNSPECIFIED = 0
MULTICLASS = 1
MULTILABEL = 2


_CLASSIFICATIONANNOTATION = _descriptor.Descriptor(
    name="ClassificationAnnotation",
    full_name="google.cloud.automl.v1beta1.ClassificationAnnotation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="score",
            full_name="google.cloud.automl.v1beta1.ClassificationAnnotation.score",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=117,
    serialized_end=158,
)


_CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY = _descriptor.Descriptor(
    name="ConfidenceMetricsEntry",
    full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="confidence_threshold",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.confidence_threshold",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="recall",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.recall",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="precision",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.precision",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="f1_score",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.f1_score",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="recall_at1",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.recall_at1",
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="precision_at1",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.precision_at1",
            index=5,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="f1_score_at1",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.f1_score_at1",
            index=6,
            number=7,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=485,
    serialized_end=657,
)

_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW = _descriptor.Descriptor(
    name="Row",
    full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.Row",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="example_count",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.Row.example_count",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=802,
    serialized_end=830,
)

_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX = _descriptor.Descriptor(
    name="ConfusionMatrix",
    full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="annotation_spec_id",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.annotation_spec_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="row",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.row",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=660,
    serialized_end=830,
)

_CLASSIFICATIONEVALUATIONMETRICS = _descriptor.Descriptor(
    name="ClassificationEvaluationMetrics",
    full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="au_prc",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.au_prc",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="base_au_prc",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.base_au_prc",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confidence_metrics_entry",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.confidence_metrics_entry",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confusion_matrix",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.confusion_matrix",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="annotation_spec_id",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.annotation_spec_id",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY,
        _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=161,
    serialized_end=830,
)

_CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY.containing_type = (
    _CLASSIFICATIONEVALUATIONMETRICS
)
_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW.containing_type = (
    _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX
)
_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX.fields_by_name[
    "row"
].message_type = _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW
_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX.containing_type = (
    _CLASSIFICATIONEVALUATIONMETRICS
)
_CLASSIFICATIONEVALUATIONMETRICS.fields_by_name[
    "confidence_metrics_entry"
].message_type = _CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY
_CLASSIFICATIONEVALUATIONMETRICS.fields_by_name[
    "confusion_matrix"
].message_type = _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX
DESCRIPTOR.message_types_by_name["ClassificationAnnotation"] = _CLASSIFICATIONANNOTATION
DESCRIPTOR.message_types_by_name[
    "ClassificationEvaluationMetrics"
] = _CLASSIFICATIONEVALUATIONMETRICS
DESCRIPTOR.enum_types_by_name["ClassificationType"] = _CLASSIFICATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassificationAnnotation = _reflection.GeneratedProtocolMessageType(
    "ClassificationAnnotation",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CLASSIFICATIONANNOTATION,
        __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
        __doc__="""Contains annotation details specific to classification.
  
  
  Attributes:
      score:
          Output only. A confidence estimate between 0.0 and 1.0. A
          higher value means greater confidence that the annotation is
          positive. If a user approves an annotation as negative or
          positive, the score value remains unchanged. If a user creates
          an annotation, the score is 0 for negative or 1 for positive.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationAnnotation)
    ),
)
_sym_db.RegisterMessage(ClassificationAnnotation)

ClassificationEvaluationMetrics = _reflection.GeneratedProtocolMessageType(
    "ClassificationEvaluationMetrics",
    (_message.Message,),
    dict(
        ConfidenceMetricsEntry=_reflection.GeneratedProtocolMessageType(
            "ConfidenceMetricsEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY,
                __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
                __doc__="""Metrics for a single confidence threshold.
    
    
    Attributes:
        confidence_threshold:
            Output only. The confidence threshold value used to compute
            the metrics.
        recall:
            Output only. Recall under the given confidence threshold.
        precision:
            Output only. Precision under the given confidence threshold.
        f1_score:
            Output only. The harmonic mean of recall and precision.
        recall_at1:
            Output only. The recall when only considering the label that
            has the highest prediction score and not below the confidence
            threshold for each example.
        precision_at1:
            Output only. The precision when only considering the label
            that has the highest predictionscore and not below the
            confidence threshold for each example.
        f1_score_at1:
            Output only. The harmonic mean of [recall\_at1][google.cloud.a
            utoml.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetric
            sEntry.recall\_at1] and [precision\_at1][google.cloud.automl.v
            1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.
            precision\_at1].
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)
            ),
        ),
        ConfusionMatrix=_reflection.GeneratedProtocolMessageType(
            "ConfusionMatrix",
            (_message.Message,),
            dict(
                Row=_reflection.GeneratedProtocolMessageType(
                    "Row",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW,
                        __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
                        __doc__="""Output only. A row in the confusion matrix.
      
      
      Attributes:
          example_count:
              Output only. Value of the specific cell in the confusion
              matrix. The number of values each row is equal to the size of
              annotatin\_spec\_id.
      """,
                        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.Row)
                    ),
                ),
                DESCRIPTOR=_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX,
                __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
                __doc__="""Confusion matrix of the model running the classification.
    
    
    Attributes:
        annotation_spec_id:
            Output only. IDs of the annotation specs used in the confusion
            matrix.
        row:
            Output only. Rows in the confusion matrix. The number of rows
            is equal to the size of ``annotation_spec_id``.
            ``row[i].value[j]`` is the number of examples that have ground
            truth of the ``annotation_spec_id[i]`` and are predicted as
            ``annotation_spec_id[j]`` by the model being evaluated.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix)
            ),
        ),
        DESCRIPTOR=_CLASSIFICATIONEVALUATIONMETRICS,
        __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
        __doc__="""Model evaluation metrics for classification problems. Visible only to
  v1beta1
  
  
  Attributes:
      au_prc:
          Output only. The Area under precision recall curve metric.
      base_au_prc:
          Output only. The Area under precision recall curve metric
          based on priors.
      confidence_metrics_entry:
          Output only. Metrics that have confidence thresholds.
          Precision-recall curve can be derived from it.
      confusion_matrix:
          Output only. Confusion matrix of the evaluation. Only set for
          MULTICLASS classification problems where number of labels is
          no more than 10. Only set for model level evaluation, not for
          evaluation per label.
      annotation_spec_id:
          Output only. The annotation spec ids used for this evaluation.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics)
    ),
)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics.ConfidenceMetricsEntry)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics.ConfusionMatrix)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics.ConfusionMatrix.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b(
        "\n\037com.google.cloud.automl.v1beta1B\023ClassificationProtoZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1"
    ),
)
# @@protoc_insertion_point(module_scope)
