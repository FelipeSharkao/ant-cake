#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x70152f67

# Compiled with Coconut version 1.5.0 [Fish License]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop, annotations
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get("__coconut__")
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules["__coconut__"]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

import strawberry  # line 1: import strawberry

@strawberry.type  # line 3: @strawberry.type
class Book:  # line 4: class Book:
    title: str  # line 5:   title: str
    author: str  # line 6:   author: str

@strawberry.type  # line 8: @strawberry.type
class Query:  # line 9: class Query:
    @strawberry.field  # line 10:   @strawberry.field
    def books(self) -> list[Book]:  # line 11:   def books(self) -> list[Book]:
        return [Book(title='The Great Gatsby', author='F. Scott Fitzgerald')]  # line 12:     return [ Book(title='The Great Gatsby', author='F. Scott Fitzgerald') ]

schema = strawberry.Schema(query=Query)  # line 14: schema = strawberry.Schema(query=Query)
