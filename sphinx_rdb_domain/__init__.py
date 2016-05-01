# coding: utf-8
import directives
import domain


def setup(app):
    app.add_domain(domain.RdbDomain)
