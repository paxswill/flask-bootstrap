from __future__ import unicode_literals, absolute_import

import sys

def public(dec):
    """Use a decorator to avoid retyping function/class names.

    * Based on an idea by Duncan Booth:
    http://groups.google.com/group/comp.lang.python/msg/11cbb03e09611b8a
    * Improved via a suggestion by Dave Angel:
    http://groups.google.com/group/comp.lang.python/msg/3d400fb22d8a42e1
    * Finally copied from http://code.activestate.com/recipes/576993-public-decorator-adds-an-item-to-__all__/
    """
    all = sys.modules[dec.__module__].__dict__.setdefault('__all__', [])
    if dec.__name__ not in all:
        all.append(dec.__name__)
    return dec
public(public)


def require_class(classes, kwargs):
    if 'class' in kwargs:
        kwargs['class'] += ' ' + classes
    else:
        kwargs['class'] = classes


from . import fields, widgets
from .fields import *
from .widgets import *

__all__.extend(fields.__all__)
__all__.extend(widgets.__all__)
