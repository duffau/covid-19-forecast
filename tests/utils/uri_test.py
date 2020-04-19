import utils.uri as uri


def test_clean_uri():
    fixtures = [
        ('AbC', 'abc'),
        ('AbC def', 'abc-def'),
        ('AbC def,hij', 'abc-def-hij'),
        ('AbC def,hij*', 'abc-def-hij')
    ]
    for _in, expected_out in fixtures:
        out = uri.clean(_in)
        assert out == expected_out
