# coding: utf-8
"""
Relational database domain.

:copyright: 2016 Yasushi Masuda.
:license: BSD
"""
from sphinx.domains import Domain, ObjType
from sphinx.locale import l_, _
from sphinx.roles import XRefRole

from directives import Database, Table, Column, Index


class RdbDomain(Domain):
    """
    Relational database domain.
    """
    name = 'rdb'
    label = 'Relational'
    object_types = {
        'database': ObjType(l_('database'), 'database', 'db'),
        'table': ObjType(l_('table'), 'table', 'tbl'),
        'column': ObjType(l_('column'), 'column', 'col'),
        'index': ObjType(l_('index'), 'index', 'idx'),
    }

    directives = {
        'database': Database,
        'table': Table,
        'column': Column,
        'index': Index,
    }
    
    roles = {
        'database': XRefRole(),
        'db': XRefRole(),
        'table': XRefRole(),
        'tbl': XRefRole(),
        'column': XRefRole(),
        'col': XRefRole(),
        'index'
        'idx': XRefRole()
    }
    
    initial_data = {}
    indices = []


