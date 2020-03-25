from models import SEIR, SEIRParams


def test_init():
    params = SEIRParams
    SEIR(params=params)
