"""Multicode System: conversión y traducción entre texto y distintos formatos."""

from multicode.core.translator import DecodeError, EncodeError, decode, encode

__all__ = ["encode", "decode", "EncodeError", "DecodeError"]
