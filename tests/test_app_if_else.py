from app import parse_guess


def test_parse_guess_none_returns_enter_prompt():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_guess_empty_returns_enter_prompt():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_guess_non_numeric_returns_error():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_float_is_converted_to_int():
    ok, value, err = parse_guess("12.7")
    assert ok is True
    assert value == 12
    assert err is None
