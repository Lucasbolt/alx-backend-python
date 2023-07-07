#!/usr/bin/env python3
"""
More involved type annotations
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Default = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Default = None) -> Res:
    '''Retrieves a value from a dict using a given key.
    '''
    if key in dct:
        return dct[key]
    return default
