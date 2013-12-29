# -*- coding: utf-8 -*-
"""
Part of the astor library for Python AST manipulation.

License: BSD

Copyright 2012 (c) Patrick Maupin
Copyright 2013 (c) Berker Peksag

"""

__version__ = '0.4-dev'

from astor.misc import iter_node, dump, all_symbols, get_anyop
from astor.misc import get_boolop, get_binop, get_cmpop, get_unaryop
from astor.misc import ExplicitNodeVisitor
from astor.misc import parsefile, CodeToAst, codetoast
from astor.codegen import to_source
from astor.treewalk import TreeWalk
