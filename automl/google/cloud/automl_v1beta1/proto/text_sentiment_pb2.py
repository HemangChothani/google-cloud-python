# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/text_sentiment.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1beta1.proto import (
    classification_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2,
)
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/text_sentiment.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.automl.v1beta1B\022TextSentimentProtoZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1"
    ),
    serialized_pb=_b(
        '\n6google/cloud/automl_v1beta1/proto/text_sentiment.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x36google/cloud/automl_v1beta1/proto/classification.proto\x1a\x1cgoogle/api/annotations.proto",\n\x17TextSentimentAnnotation\x12\x11\n\tsentiment\x18\x01 \x01(\x05"\xc5\x02\n\x1eTextSentimentEvaluationMetrics\x12\x11\n\tprecision\x18\x01 \x01(\x02\x12\x0e\n\x06recall\x18\x02 \x01(\x02\x12\x10\n\x08\x66\x31_score\x18\x03 \x01(\x02\x12\x1b\n\x13mean_absolute_error\x18\x04 \x01(\x02\x12\x1a\n\x12mean_squared_error\x18\x05 \x01(\x02\x12\x14\n\x0clinear_kappa\x18\x06 \x01(\x02\x12\x17\n\x0fquadratic_kappa\x18\x07 \x01(\x02\x12\x66\n\x10\x63onfusion_matrix\x18\x08 \x01(\x0b\x32L.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix\x12\x1e\n\x12\x61nnotation_spec_id\x18\t \x03(\tB\x02\x18\x01\x42\x96\x01\n\x1f\x63om.google.cloud.automl.v1beta1B\x12TextSentimentProtoZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_TEXTSENTIMENTANNOTATION = _descriptor.Descriptor(
    name="TextSentimentAnnotation",
    full_name="google.cloud.automl.v1beta1.TextSentimentAnnotation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="sentiment",
            full_name="google.cloud.automl.v1beta1.TextSentimentAnnotation.sentiment",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=173,
    serialized_end=217,
)


_TEXTSENTIMENTEVALUATIONMETRICS = _descriptor.Descriptor(
    name="TextSentimentEvaluationMetrics",
    full_name="google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="precision",
            full_name="google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics.precision",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="recall",
            full_name="google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics.recall",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="f1_score",
            full_name="google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics.f1_score",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="mean_absolute_error",
            full_name="google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics.mean_absolute_error",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="mean_squared_error",
            full_name="google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics.mean_squared_error",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="linear_kappa",
            full_name="google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics.linear_kappa",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="quadratic_kappa",
            full_name="google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics.quadratic_kappa",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confusion_matrix",
            full_name="google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics.confusion_matrix",
            index=7,
            number=8,
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="annotation_spec_id",
            full_name="google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics.annotation_spec_id",
            index=8,
            number=9,
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
            serialized_options=_b("\030\001"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=220,
    serialized_end=545,
)

_TEXTSENTIMENTEVALUATIONMETRICS.fields_by_name[
    "confusion_matrix"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2._CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX
)
DESCRIPTOR.message_types_by_name["TextSentimentAnnotation"] = _TEXTSENTIMENTANNOTATION
DESCRIPTOR.message_types_by_name[
    "TextSentimentEvaluationMetrics"
] = _TEXTSENTIMENTEVALUATIONMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextSentimentAnnotation = _reflection.GeneratedProtocolMessageType(
    "TextSentimentAnnotation",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TEXTSENTIMENTANNOTATION,
        __module__="google.cloud.automl_v1beta1.proto.text_sentiment_pb2",
        __doc__="""Contains annotation details specific to text sentiment.
  
  
  Attributes:
      sentiment:
          Output only. The sentiment with the semantic, as given to the 
          [AutoMl.ImportData][google.cloud.automl.v1beta1.AutoMl.ImportD
          ata] when populating the dataset from which the model used for
          the prediction had been trained. The sentiment values are
          between 0 and
          Dataset.text\_sentiment\_dataset\_metadata.sentiment\_max
          (inclusive), with higher value meaning more positive
          sentiment. They are completely relative, i.e. 0 means least
          positive sentiment and sentiment\_max means the most positive
          from the sentiments present in the train data. Therefore e.g.
          if train data had only negative sentiment, then
          sentiment\_max, would be still negative (although least
          negative). The sentiment shouldn't be confused with "score" or
          "magnitude" from the previous Natural Language Sentiment
          Analysis API.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextSentimentAnnotation)
    ),
)
_sym_db.RegisterMessage(TextSentimentAnnotation)

TextSentimentEvaluationMetrics = _reflection.GeneratedProtocolMessageType(
    "TextSentimentEvaluationMetrics",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TEXTSENTIMENTEVALUATIONMETRICS,
        __module__="google.cloud.automl_v1beta1.proto.text_sentiment_pb2",
        __doc__="""Model evaluation metrics for text sentiment problems.
  
  
  Attributes:
      precision:
          Output only. Precision.
      recall:
          Output only. Recall.
      f1_score:
          Output only. The harmonic mean of recall and precision.
      mean_absolute_error:
          Output only. Mean absolute error. Only set for the overall
          model evaluation, not for evaluation of a single annotation
          spec.
      mean_squared_error:
          Output only. Mean squared error. Only set for the overall
          model evaluation, not for evaluation of a single annotation
          spec.
      linear_kappa:
          Output only. Linear weighted kappa. Only set for the overall
          model evaluation, not for evaluation of a single annotation
          spec.
      quadratic_kappa:
          Output only. Quadratic weighted kappa. Only set for the
          overall model evaluation, not for evaluation of a single
          annotation spec.
      confusion_matrix:
          Output only. Confusion matrix of the evaluation. Only set for
          the overall model evaluation, not for evaluation of a single
          annotation spec.
      annotation_spec_id:
          Output only. The annotation spec ids used for this evaluation.
          Deprecated .
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextSentimentEvaluationMetrics)
    ),
)
_sym_db.RegisterMessage(TextSentimentEvaluationMetrics)


DESCRIPTOR._options = None
_TEXTSENTIMENTEVALUATIONMETRICS.fields_by_name["annotation_spec_id"]._options = None
# @@protoc_insertion_point(module_scope)
