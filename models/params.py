from collections import namedtuple
SIRParams = namedtuple('SIRParams', ['beta', 'gamma', 'S0', 'I0', 'R0'])
SIRParams.__new__.__defaults__ = (None,) * len(SIRParams._fields)

SEIRParams = namedtuple('SEIRParams', ['beta', 'gamma', 'alpha', 'S0', 'E0', 'I0', 'R0'])
SEIRParams.__new__.__defaults__ = (None,) * len(SEIRParams._fields)
