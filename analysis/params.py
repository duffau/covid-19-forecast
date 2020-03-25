from collections import namedtuple

Params = namedtuple('Params', ['beta', 'gamma', 'S0', 'E0', 'I0', 'R0'])
Params.__new__.__defaults__ = (None,) * len(Params._fields)
