# Copyright (c) 2006-2011, 2013 LOGILAB S.A. (Paris, FRANCE) <contact@logilab.fr>
# Copyright (c) 2010 Daniel Harding <dharding@gmail.com>
# Copyright (c) 2014-2018 Claudiu Popa <pcmanticore@gmail.com>
# Copyright (c) 2014 Google, Inc.
# Copyright (c) 2015-2016 Ceridwen <ceridwenv@gmail.com>
# Copyright (c) 2016 Jared Garst <jgarst@users.noreply.github.com>
# Copyright (c) 2017 Ashley Whetter <ashley@awhetter.co.uk>
# Copyright (c) 2017 rr- <rr-@sakuya.pl>
# Copyright (c) 2018 Bryce Guinta <bryce.paul.guinta@gmail.com>

# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/master/COPYING.LESSER

"""Every available node class.

.. seealso::
    :doc:`ast documentation <green_tree_snakes:nodes>`

All nodes inherit from :class:`~astroid.node_classes.NodeNG`.
"""
# pylint: disable=unused-import,redefined-builtin

from astroid.node_classes import (
    NodeNG, Block, Arguments, AssignAttr, Assert, Assign, AnnAssign,
    AssignName, AugAssign, Repr, BinOp, BoolOp, Break, Call, Compare,
    Comprehension, Const, Continue, Decorators, DelAttr, DelName, Delete,
    Dict, Expr, Ellipsis, EmptyNode, ExceptHandler, Exec, ExtSlice, For,
    ImportFrom, Attribute, Global, If, IfExp, Import, Index, Keyword,
    List, Name, Nonlocal, Pass, Print, Raise, Return, Set, Slice, Starred, Subscript,
    TryExcept, TryFinally, Tuple, UnaryOp, While, With, Yield, YieldFrom,
    const_factory,
    AsyncFor, Await, AsyncWith,
    FormattedValue, JoinedStr,
    # Node not present in the builtin ast module.
    DictUnpack,
    Unknown,
)
from astroid.scoped_nodes import (
    LocalsDictNodeNG, Module, GeneratorExp, Lambda, DictComp,
    ListComp, SetComp, FunctionDef, ClassDef,
    AsyncFunctionDef,
)



ALL_NODE_CLASSES = (
    AsyncFunctionDef, AsyncFor, AsyncWith, Await,

    Arguments, AssignAttr, Assert, Assign, AnnAssign, AssignName, AugAssign,
    Repr, Block, BinOp, BoolOp, Break,
    Call, ClassDef, Compare, Comprehension, Const, Continue,
    Decorators, DelAttr, DelName, Delete,
    Dict, DictComp, DictUnpack, Expr,
    Ellipsis, EmptyNode, ExceptHandler, Exec, ExtSlice,
    For, ImportFrom, FunctionDef,
    Attribute, GeneratorExp, Global,
    If, IfExp, Import, Index,
    Keyword,
    Lambda, List, ListComp, LocalsDictNodeNG,
    Name, Nonlocal,
    Module,
    Pass, Print,
    Raise, Return,
    Set, SetComp, Slice, Starred, Subscript,
    TryExcept, TryFinally, Tuple,
    UnaryOp,
    While, With,
    Yield, YieldFrom,
    FormattedValue, JoinedStr,
    )
