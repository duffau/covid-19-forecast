import preproc.normalize as normz


def test__strip_whitespace():
    cases = [
        ('xyzabc', 'xyzabc'),
        ('xyz \t\n\r\f\vabc \t\n\r\f\v', 'xyz \t\n\r\f\vabc'),
    ]
    for with_ws, stripped in cases:
        output_stripped = normz._strip_whitespace(with_ws)
        assert output_stripped == stripped


def test__camel_case_to_snake_case():
    cases = [
        ('something_in_camel_case', 'something_in_camel_case'),
        ('SomethingInCamelCase', 'something_in_camel_case'),
        ('somethingInCamelCase', 'something_in_camel_case'),
        ('something_mixedCamelCase_and_snake_case', 'something_mixed_camel_case_and_snake_case')
    ]
    for camel, snake in cases:
        output_snake = normz._camel_case_to_snake_case(camel)
        assert output_snake == snake


def test__replace_whitespace_with_underscore():
    cases = [
        ('xyzabc', 'xyzabc'),
        ('xyz abc', 'xyz_abc'),
        ('xyz  abc', 'xyz_abc'),
        ('xyzabc', 'xyzabc'),
        ('xyz\t\n\r\f\vabc', 'xyz_abc'),
    ]
    for with_ws, with_underscores in cases:
        out_with_underscores = normz._replace_whitespace_with_underscore(with_ws)
        assert out_with_underscores == with_underscores

