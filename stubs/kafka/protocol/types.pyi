from kafka.protocol.abstract import AbstractType as AbstractType
from typing import Any

class Int8(AbstractType):
    @classmethod
    def encode(cls, value: Any): ...
    @classmethod
    def decode(cls, data: Any): ...

class Int16(AbstractType):
    @classmethod
    def encode(cls, value: Any): ...
    @classmethod
    def decode(cls, data: Any): ...

class Int32(AbstractType):
    @classmethod
    def encode(cls, value: Any): ...
    @classmethod
    def decode(cls, data: Any): ...

class Int64(AbstractType):
    @classmethod
    def encode(cls, value: Any): ...
    @classmethod
    def decode(cls, data: Any): ...

class String(AbstractType):
    encoding: Any = ...
    def __init__(self, encoding: str = ...) -> None: ...
    def encode(self, value: Any): ...
    def decode(self, data: Any): ...

class Bytes(AbstractType):
    @classmethod
    def encode(cls, value: Any): ...
    @classmethod
    def decode(cls, data: Any): ...
    @classmethod
    def repr(cls, value: Any): ...

class Boolean(AbstractType):
    @classmethod
    def encode(cls, value: Any): ...
    @classmethod
    def decode(cls, data: Any): ...

class Schema(AbstractType):
    def __init__(self, *fields: Any) -> None: ...
    def encode(self, item: Any): ...
    def decode(self, data: Any): ...
    def __len__(self): ...
    @classmethod
    def repr(cls, value: Any): ...

class Array(AbstractType):
    array_of: Any = ...
    def __init__(self, *array_of: Any) -> None: ...
    def encode(self, items: Any): ...
    def decode(self, data: Any): ...
    @classmethod
    def repr(cls, value: Any): ...
