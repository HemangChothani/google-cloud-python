# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/model_evaluation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.automl_v1beta1.proto import classification_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2
from google.cloud.automl_v1beta1.proto import translation_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/automl_v1beta1/proto/model_evaluation.proto',
  package='google.cloud.automl.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n8google/cloud/automl_v1beta1/proto/model_evaluation.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x36google/cloud/automl_v1beta1/proto/classification.proto\x1a\x33google/cloud/automl_v1beta1/proto/translation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe8\x02\n\x0fModelEvaluation\x12i\n!classification_evaluation_metrics\x18\x08 \x01(\x0b\x32<.google.cloud.automl.v1beta1.ClassificationEvaluationMetricsH\x00\x12\x63\n\x1etranslation_evaluation_metrics\x18\t \x01(\x0b\x32\x39.google.cloud.automl.v1beta1.TranslationEvaluationMetricsH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12\x61nnotation_spec_id\x18\x02 \x01(\t\x12/\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x17\x65valuated_example_count\x18\x06 \x01(\x05\x42\t\n\x07metricsBf\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automlb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2.DESCRIPTOR,google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_MODELEVALUATION = _descriptor.Descriptor(
  name='ModelEvaluation',
  full_name='google.cloud.automl.v1beta1.ModelEvaluation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classification_evaluation_metrics', full_name='google.cloud.automl.v1beta1.ModelEvaluation.classification_evaluation_metrics', index=0,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='translation_evaluation_metrics', full_name='google.cloud.automl.v1beta1.ModelEvaluation.translation_evaluation_metrics', index=1,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.automl.v1beta1.ModelEvaluation.name', index=2,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotation_spec_id', full_name='google.cloud.automl.v1beta1.ModelEvaluation.annotation_spec_id', index=3,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.automl.v1beta1.ModelEvaluation.create_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evaluated_example_count', full_name='google.cloud.automl.v1beta1.ModelEvaluation.evaluated_example_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='metrics', full_name='google.cloud.automl.v1beta1.ModelEvaluation.metrics',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=262,
  serialized_end=622,
)

_MODELEVALUATION.fields_by_name['classification_evaluation_metrics'].message_type = google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2._CLASSIFICATIONEVALUATIONMETRICS
_MODELEVALUATION.fields_by_name['translation_evaluation_metrics'].message_type = google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2._TRANSLATIONEVALUATIONMETRICS
_MODELEVALUATION.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MODELEVALUATION.oneofs_by_name['metrics'].fields.append(
  _MODELEVALUATION.fields_by_name['classification_evaluation_metrics'])
_MODELEVALUATION.fields_by_name['classification_evaluation_metrics'].containing_oneof = _MODELEVALUATION.oneofs_by_name['metrics']
_MODELEVALUATION.oneofs_by_name['metrics'].fields.append(
  _MODELEVALUATION.fields_by_name['translation_evaluation_metrics'])
_MODELEVALUATION.fields_by_name['translation_evaluation_metrics'].containing_oneof = _MODELEVALUATION.oneofs_by_name['metrics']
DESCRIPTOR.message_types_by_name['ModelEvaluation'] = _MODELEVALUATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelEvaluation = _reflection.GeneratedProtocolMessageType('ModelEvaluation', (_message.Message,), dict(
  DESCRIPTOR = _MODELEVALUATION,
  __module__ = 'google.cloud.automl_v1beta1.proto.model_evaluation_pb2'
  ,
  __doc__ = """Evaluation results of a model.
  
  
  Attributes:
      metrics:
          Output only. Problem type specific evaluation metrics.
      classification_evaluation_metrics:
          Evaluation metrics for models on classification problems
          models.
      translation_evaluation_metrics:
          Evaluation metrics for models on translation models.
      name:
          Output only. Resource name of the model evaluation. Format:  `
          `projects/{project_id}/locations/{location_id}/models/{model_i
          d}/modelEvaluations/{model_evaluation_id}``
      annotation_spec_id:
          Output only. The ID of the annotation spec that the model
          evaluation applies to. The ID is empty for overall model
          evaluation. NOTE: Currently there is no way to obtain the
          display\_name of the annotation spec from its ID. To see the
          display\_names, review the model evaluations in the UI.
      create_time:
          Output only. Timestamp when this model evaluation was created.
      evaluated_example_count:
          Output only. The number of examples used for model evaluation.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ModelEvaluation)
  ))
_sym_db.RegisterMessage(ModelEvaluation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl'))
# @@protoc_insertion_point(module_scope)
