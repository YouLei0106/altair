import os
import json
from .core import FunctionExpression


class ExprFunc(object):
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc
        self.__doc__ = """{0}(*args)\n    {1}""".format(name, doc)

    def __call__(self, *args):
        return FunctionExpression(self.name, args)

    def __repr__(self):
        return "<function expr.{0}(*args)>".format(self.name)


def _populate_namespace():
    all_ = []
    with open(os.path.join(os.path.dirname(__file__), 'func_listing.json')) as f:
        func_listing = json.load(f)
    for name, doc in func_listing.items():
        globals()[name] = ExprFunc(name, doc)
        all_.append(name)
    return all_


__all__ = _populate_namespace()
