# coding: utf-8
"""
Relational database domain.

:copyright: 2016 Yasushi Masuda.
:license: BSD
"""

from docutils.parsers.rst import directives
from sphinx.directives import ObjectDescription


class RDBDirective(ObjectDescription):

    required_arguments = 1
    has_content = True

    @property
    def get_option_spec(self):
        return dict(noindex=directives.flag)
    option_spec = property(get_option_spec)


class Database(RDBDirective):
    """
    Description of an rdbms database.
    """
    pass


class Table(RDBDirective):
    """
    Description of an rdbms table.
    """
    pass


class Column(RDBDirective):
    """
    Description of an rdbms column.
    """
    pass


class Index(RDBDirective):
    """
    Description of an rdbms index.
    """
    pass
