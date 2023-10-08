import pytest
from variable_base_factoradic import from_factoradic, to_factoradic

xkcd_examples = [
    (0, "0"),
    (1, "1"),
    (2, "10"),
    (3, "11"),
    (4, "20"),
    (5, "21"),
    (6, "100"),
    (7, "101"),
    (21, "311"),
    (22, "320"),
    (23, "321"),
    (24, "1000"),
    (25, "1001"),
    (5038, "654320"),
    (5039, "654321"),
    (5040, "1000000"),
    (999998, "266251210"),
    (999999, "266251211"),
    (1000000, "266251220"),
    (1000001, "266251221"),
]


@pytest.mark.parametrize("base_10, factoradic", xkcd_examples)
def test_xkcd_examples_from_factoradic(base_10, factoradic):
    """
    Test that the examples from https://xkcd.com/2835/ can be converted from factoradic to base 10
    """
    assert from_factoradic(factoradic) == base_10


@pytest.mark.parametrize("base_10, factoradic", xkcd_examples)
def test_xkcd_examples_to_factoradic(base_10, factoradic):
    """
    Test that the examples from https://xkcd.com/2835/ can be converted from base 10 to factoradic
    """
    assert to_factoradic(base_10) == factoradic


def test_from_maximum_factoradic():
    assert from_factoradic("987654321") == 3628799


def test_to_maximum_factoradic():
    assert to_factoradic(3628799) == "987654321"


def test_from_too_large_factoradic():
    with pytest.raises(ValueError, match="Numbers larger than 3628799 are simply illegal"):
        from_factoradic("1000000000")


def test_to_too_large_factoradic():
    with pytest.raises(ValueError, match="Numbers larger than 3628799 are simply illegal"):
        to_factoradic(3628800)


@pytest.mark.parametrize("pseudo_factoradic, idx, expected_base", [
    ("2", 0, 2),
    ("30", 1, 3),
    ("400", 2, 4),
    ("404", 0, 2),
    ("A", 0, 2),
])
def test_invalid_base(pseudo_factoradic, idx, expected_base):
    with pytest.raises(
            ValueError,
            match=f"Invalid input: Digit at position {idx} must be in base {expected_base}"
    ):
        from_factoradic(pseudo_factoradic)
