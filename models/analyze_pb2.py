# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analyze.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='analyze.proto',
  package='analysis',
  syntax='proto3',
  serialized_options=b'\n\023com.decomp.analysisB\rAnalysisProtoP\001\242\002\003JAD',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ranalyze.proto\x12\x08\x61nalysis\"\xa8\x03\n\x06\x43lass_\x12\x13\n\x0bisInterface\x18\x01 \x01(\x08\x12\x12\n\nisImplicit\x18\x02 \x01(\x08\x12\x13\n\x0bisAnonymous\x18\x03 \x01(\x08\x12\x12\n\nsimpleName\x18\x04 \x01(\t\x12\x10\n\x08\x66ullName\x18\x05 \x01(\t\x12\x10\n\x08\x66ilePath\x18\x06 \x01(\t\x12\x17\n\x0freferencedTypes\x18\x07 \x03(\t\x12\x12\n\nfieldTypes\x18\x08 \x03(\t\x12\x16\n\x0eparameterTypes\x18\t \x03(\t\x12\x13\n\x0breturnTypes\x18\n \x03(\t\x12\x13\n\x0bnestedTypes\x18\x0b \x03(\t\x12\x16\n\x0einheritedTypes\x18\x0c \x03(\t\x12)\n\nfieldCalls\x18\r \x03(\x0b\x32\x15.analysis.Invocation_\x12\x14\n\x0c\x63onstructors\x18\x0e \x03(\t\x12\x14\n\x0ctextAndNames\x18\x0f \x03(\t\x12\x0f\n\x07methods\x18\x10 \x03(\t\x12\x0f\n\x07\x61ppName\x18\x11 \x01(\t\x12\x18\n\x0bserviceName\x18\x12 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_serviceName\"\xf7\x02\n\x07Method_\x12\x10\n\x08isLambda\x18\x01 \x01(\x08\x12\x15\n\risConstructor\x18\x02 \x01(\x08\x12\x12\n\nparentName\x18\x03 \x01(\t\x12\x12\n\nsimpleName\x18\x04 \x01(\t\x12\x10\n\x08\x66ullName\x18\x05 \x01(\t\x12\x12\n\nreturnType\x18\x06 \x01(\t\x12/\n\x10localInvocations\x18\x07 \x03(\x0b\x32\x15.analysis.Invocation_\x12*\n\x0binvocations\x18\x08 \x03(\x0b\x32\x15.analysis.Invocation_\x12\x16\n\x0eparameterNames\x18\t \x03(\t\x12\x16\n\x0eparameterTypes\x18\n \x03(\t\x12\x17\n\x0freferencedTypes\x18\x0b \x03(\t\x12\x14\n\x0ctextAndNames\x18\x0c \x03(\t\x12\x0f\n\x07\x61ppName\x18\r \x01(\t\x12\x18\n\x0bserviceName\x18\x0e \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_serviceName\"\xb5\x01\n\x0bInvocation_\x12\r\n\x05local\x18\x01 \x01(\x08\x12\x16\n\x0einvokingMethod\x18\x02 \x01(\t\x12\x16\n\x0einvokingObject\x18\x03 \x01(\t\x12\x15\n\rinvokedMethod\x18\x04 \x01(\t\x12\x15\n\rinvokedObject\x18\x05 \x01(\t\x12\x0f\n\x07\x61ppName\x18\x06 \x01(\t\x12\x18\n\x0bserviceName\x18\x07 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_serviceName\"3\n\x0e\x43lassContainer\x12!\n\x07\x63lasses\x18\x01 \x03(\x0b\x32\x10.analysis.Class_\"5\n\x0fMethodContainer\x12\"\n\x07methods\x18\x01 \x03(\x0b\x32\x11.analysis.Method_\"A\n\x13InvocationContainer\x12*\n\x0binvocations\x18\x01 \x03(\x0b\x32\x15.analysis.Invocation_\".\n\nAstRequest\x12\x0f\n\x07\x61ppName\x18\x01 \x01(\t\x12\x0f\n\x07\x61ppRepo\x18\x02 \x01(\t\"\x1b\n\x08\x41stReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xfa\x01\n\x08\x41nalyzer\x12\x36\n\x08initRepo\x12\x14.analysis.AstRequest\x1a\x12.analysis.AstReply\"\x00\x12\x38\n\ngetClasses\x12\x14.analysis.AstRequest\x1a\x10.analysis.Class_\"\x00\x30\x01\x12\x39\n\ngetMethods\x12\x14.analysis.AstRequest\x1a\x11.analysis.Method_\"\x00\x30\x01\x12\x41\n\x0egetInvocations\x12\x14.analysis.AstRequest\x1a\x15.analysis.Invocation_\"\x00\x30\x01\x42,\n\x13\x63om.decomp.analysisB\rAnalysisProtoP\x01\xa2\x02\x03JADb\x06proto3'
)




_CLASS_ = _descriptor.Descriptor(
  name='Class_',
  full_name='analysis.Class_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isInterface', full_name='analysis.Class_.isInterface', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isImplicit', full_name='analysis.Class_.isImplicit', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isAnonymous', full_name='analysis.Class_.isAnonymous', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='simpleName', full_name='analysis.Class_.simpleName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fullName', full_name='analysis.Class_.fullName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filePath', full_name='analysis.Class_.filePath', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='referencedTypes', full_name='analysis.Class_.referencedTypes', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fieldTypes', full_name='analysis.Class_.fieldTypes', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameterTypes', full_name='analysis.Class_.parameterTypes', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='returnTypes', full_name='analysis.Class_.returnTypes', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nestedTypes', full_name='analysis.Class_.nestedTypes', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inheritedTypes', full_name='analysis.Class_.inheritedTypes', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fieldCalls', full_name='analysis.Class_.fieldCalls', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constructors', full_name='analysis.Class_.constructors', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='textAndNames', full_name='analysis.Class_.textAndNames', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='methods', full_name='analysis.Class_.methods', index=15,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='appName', full_name='analysis.Class_.appName', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceName', full_name='analysis.Class_.serviceName', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_serviceName', full_name='analysis.Class_._serviceName',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=28,
  serialized_end=452,
)


_METHOD_ = _descriptor.Descriptor(
  name='Method_',
  full_name='analysis.Method_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isLambda', full_name='analysis.Method_.isLambda', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isConstructor', full_name='analysis.Method_.isConstructor', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parentName', full_name='analysis.Method_.parentName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='simpleName', full_name='analysis.Method_.simpleName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fullName', full_name='analysis.Method_.fullName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='returnType', full_name='analysis.Method_.returnType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localInvocations', full_name='analysis.Method_.localInvocations', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invocations', full_name='analysis.Method_.invocations', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameterNames', full_name='analysis.Method_.parameterNames', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameterTypes', full_name='analysis.Method_.parameterTypes', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='referencedTypes', full_name='analysis.Method_.referencedTypes', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='textAndNames', full_name='analysis.Method_.textAndNames', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='appName', full_name='analysis.Method_.appName', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceName', full_name='analysis.Method_.serviceName', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_serviceName', full_name='analysis.Method_._serviceName',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=455,
  serialized_end=830,
)


_INVOCATION_ = _descriptor.Descriptor(
  name='Invocation_',
  full_name='analysis.Invocation_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='local', full_name='analysis.Invocation_.local', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invokingMethod', full_name='analysis.Invocation_.invokingMethod', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invokingObject', full_name='analysis.Invocation_.invokingObject', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invokedMethod', full_name='analysis.Invocation_.invokedMethod', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invokedObject', full_name='analysis.Invocation_.invokedObject', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='appName', full_name='analysis.Invocation_.appName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceName', full_name='analysis.Invocation_.serviceName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_serviceName', full_name='analysis.Invocation_._serviceName',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=833,
  serialized_end=1014,
)


_CLASSCONTAINER = _descriptor.Descriptor(
  name='ClassContainer',
  full_name='analysis.ClassContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classes', full_name='analysis.ClassContainer.classes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1016,
  serialized_end=1067,
)


_METHODCONTAINER = _descriptor.Descriptor(
  name='MethodContainer',
  full_name='analysis.MethodContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='methods', full_name='analysis.MethodContainer.methods', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1069,
  serialized_end=1122,
)


_INVOCATIONCONTAINER = _descriptor.Descriptor(
  name='InvocationContainer',
  full_name='analysis.InvocationContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='invocations', full_name='analysis.InvocationContainer.invocations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1124,
  serialized_end=1189,
)


_ASTREQUEST = _descriptor.Descriptor(
  name='AstRequest',
  full_name='analysis.AstRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='appName', full_name='analysis.AstRequest.appName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='appRepo', full_name='analysis.AstRequest.appRepo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1191,
  serialized_end=1237,
)


_ASTREPLY = _descriptor.Descriptor(
  name='AstReply',
  full_name='analysis.AstReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='analysis.AstReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1239,
  serialized_end=1266,
)

_CLASS_.fields_by_name['fieldCalls'].message_type = _INVOCATION_
_CLASS_.oneofs_by_name['_serviceName'].fields.append(
  _CLASS_.fields_by_name['serviceName'])
_CLASS_.fields_by_name['serviceName'].containing_oneof = _CLASS_.oneofs_by_name['_serviceName']
_METHOD_.fields_by_name['localInvocations'].message_type = _INVOCATION_
_METHOD_.fields_by_name['invocations'].message_type = _INVOCATION_
_METHOD_.oneofs_by_name['_serviceName'].fields.append(
  _METHOD_.fields_by_name['serviceName'])
_METHOD_.fields_by_name['serviceName'].containing_oneof = _METHOD_.oneofs_by_name['_serviceName']
_INVOCATION_.oneofs_by_name['_serviceName'].fields.append(
  _INVOCATION_.fields_by_name['serviceName'])
_INVOCATION_.fields_by_name['serviceName'].containing_oneof = _INVOCATION_.oneofs_by_name['_serviceName']
_CLASSCONTAINER.fields_by_name['classes'].message_type = _CLASS_
_METHODCONTAINER.fields_by_name['methods'].message_type = _METHOD_
_INVOCATIONCONTAINER.fields_by_name['invocations'].message_type = _INVOCATION_
DESCRIPTOR.message_types_by_name['Class_'] = _CLASS_
DESCRIPTOR.message_types_by_name['Method_'] = _METHOD_
DESCRIPTOR.message_types_by_name['Invocation_'] = _INVOCATION_
DESCRIPTOR.message_types_by_name['ClassContainer'] = _CLASSCONTAINER
DESCRIPTOR.message_types_by_name['MethodContainer'] = _METHODCONTAINER
DESCRIPTOR.message_types_by_name['InvocationContainer'] = _INVOCATIONCONTAINER
DESCRIPTOR.message_types_by_name['AstRequest'] = _ASTREQUEST
DESCRIPTOR.message_types_by_name['AstReply'] = _ASTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Class_ = _reflection.GeneratedProtocolMessageType('Class_', (_message.Message,), {
  'DESCRIPTOR' : _CLASS_,
  '__module__' : 'analyze_pb2'
  # @@protoc_insertion_point(class_scope:analysis.Class_)
  })
_sym_db.RegisterMessage(Class_)

Method_ = _reflection.GeneratedProtocolMessageType('Method_', (_message.Message,), {
  'DESCRIPTOR' : _METHOD_,
  '__module__' : 'analyze_pb2'
  # @@protoc_insertion_point(class_scope:analysis.Method_)
  })
_sym_db.RegisterMessage(Method_)

Invocation_ = _reflection.GeneratedProtocolMessageType('Invocation_', (_message.Message,), {
  'DESCRIPTOR' : _INVOCATION_,
  '__module__' : 'analyze_pb2'
  # @@protoc_insertion_point(class_scope:analysis.Invocation_)
  })
_sym_db.RegisterMessage(Invocation_)

ClassContainer = _reflection.GeneratedProtocolMessageType('ClassContainer', (_message.Message,), {
  'DESCRIPTOR' : _CLASSCONTAINER,
  '__module__' : 'analyze_pb2'
  # @@protoc_insertion_point(class_scope:analysis.ClassContainer)
  })
_sym_db.RegisterMessage(ClassContainer)

MethodContainer = _reflection.GeneratedProtocolMessageType('MethodContainer', (_message.Message,), {
  'DESCRIPTOR' : _METHODCONTAINER,
  '__module__' : 'analyze_pb2'
  # @@protoc_insertion_point(class_scope:analysis.MethodContainer)
  })
_sym_db.RegisterMessage(MethodContainer)

InvocationContainer = _reflection.GeneratedProtocolMessageType('InvocationContainer', (_message.Message,), {
  'DESCRIPTOR' : _INVOCATIONCONTAINER,
  '__module__' : 'analyze_pb2'
  # @@protoc_insertion_point(class_scope:analysis.InvocationContainer)
  })
_sym_db.RegisterMessage(InvocationContainer)

AstRequest = _reflection.GeneratedProtocolMessageType('AstRequest', (_message.Message,), {
  'DESCRIPTOR' : _ASTREQUEST,
  '__module__' : 'analyze_pb2'
  # @@protoc_insertion_point(class_scope:analysis.AstRequest)
  })
_sym_db.RegisterMessage(AstRequest)

AstReply = _reflection.GeneratedProtocolMessageType('AstReply', (_message.Message,), {
  'DESCRIPTOR' : _ASTREPLY,
  '__module__' : 'analyze_pb2'
  # @@protoc_insertion_point(class_scope:analysis.AstReply)
  })
_sym_db.RegisterMessage(AstReply)


DESCRIPTOR._options = None

_ANALYZER = _descriptor.ServiceDescriptor(
  name='Analyzer',
  full_name='analysis.Analyzer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1269,
  serialized_end=1519,
  methods=[
  _descriptor.MethodDescriptor(
    name='initRepo',
    full_name='analysis.Analyzer.initRepo',
    index=0,
    containing_service=None,
    input_type=_ASTREQUEST,
    output_type=_ASTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getClasses',
    full_name='analysis.Analyzer.getClasses',
    index=1,
    containing_service=None,
    input_type=_ASTREQUEST,
    output_type=_CLASS_,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getMethods',
    full_name='analysis.Analyzer.getMethods',
    index=2,
    containing_service=None,
    input_type=_ASTREQUEST,
    output_type=_METHOD_,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getInvocations',
    full_name='analysis.Analyzer.getInvocations',
    index=3,
    containing_service=None,
    input_type=_ASTREQUEST,
    output_type=_INVOCATION_,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANALYZER)

DESCRIPTOR.services_by_name['Analyzer'] = _ANALYZER

# @@protoc_insertion_point(module_scope)
