# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/todo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/todo.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10proto/todo.proto\"5\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\ttask_todo\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\"\x1f\n\x08\x41llTasks\x12\x13\n\x04task\x18\x01 \x03(\x0b\x32\x05.Task\"\x07\n\x05\x45mpty2\xdf\x01\n\x04Todo\x12\x19\n\x07\x41\x64\x64Task\x12\x05.Task\x1a\x05.Task\"\x00\x12#\n\x0cListAllTasks\x12\x06.Empty\x1a\t.AllTasks\"\x00\x12\x1a\n\x08\x45\x64itTask\x12\x05.Task\x1a\x05.Task\"\x00\x12\x1c\n\nRemoveTask\x12\x05.Task\x1a\x05.Task\"\x00\x12\x1e\n\x0cUpdateStatus\x12\x05.Task\x1a\x05.Task\"\x00\x12\"\n\rListAllStream\x12\x06.Empty\x1a\x05.Task\"\x00\x30\x01\x12\x19\n\x07GetTask\x12\x05.Task\x1a\x05.Task\"\x00\x62\x06proto3'
)




_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Task.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_todo', full_name='Task.task_todo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='Task.status', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=20,
  serialized_end=73,
)


_ALLTASKS = _descriptor.Descriptor(
  name='AllTasks',
  full_name='AllTasks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='AllTasks.task', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=75,
  serialized_end=106,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=108,
  serialized_end=115,
)

_ALLTASKS.fields_by_name['task'].message_type = _TASK
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['AllTasks'] = _ALLTASKS
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'proto.todo_pb2'
  # @@protoc_insertion_point(class_scope:Task)
  })
_sym_db.RegisterMessage(Task)

AllTasks = _reflection.GeneratedProtocolMessageType('AllTasks', (_message.Message,), {
  'DESCRIPTOR' : _ALLTASKS,
  '__module__' : 'proto.todo_pb2'
  # @@protoc_insertion_point(class_scope:AllTasks)
  })
_sym_db.RegisterMessage(AllTasks)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'proto.todo_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)



_TODO = _descriptor.ServiceDescriptor(
  name='Todo',
  full_name='Todo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=118,
  serialized_end=341,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddTask',
    full_name='Todo.AddTask',
    index=0,
    containing_service=None,
    input_type=_TASK,
    output_type=_TASK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListAllTasks',
    full_name='Todo.ListAllTasks',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_ALLTASKS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EditTask',
    full_name='Todo.EditTask',
    index=2,
    containing_service=None,
    input_type=_TASK,
    output_type=_TASK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveTask',
    full_name='Todo.RemoveTask',
    index=3,
    containing_service=None,
    input_type=_TASK,
    output_type=_TASK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateStatus',
    full_name='Todo.UpdateStatus',
    index=4,
    containing_service=None,
    input_type=_TASK,
    output_type=_TASK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListAllStream',
    full_name='Todo.ListAllStream',
    index=5,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_TASK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTask',
    full_name='Todo.GetTask',
    index=6,
    containing_service=None,
    input_type=_TASK,
    output_type=_TASK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODO)

DESCRIPTOR.services_by_name['Todo'] = _TODO

# @@protoc_insertion_point(module_scope)