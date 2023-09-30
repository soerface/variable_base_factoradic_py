import pytest
from variable_base_factoradic import convert


@pytest.mark.parametrize("base_10, factoradic", [
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
])
@pytest.mark.parametrize("to_factoradic", [
    True, False
], ids=["to_factoradic", "from_factoradic"])
def test_xkcd_examples(base_10, factoradic, to_factoradic):
    """
    Test that the examples from https://xkcd.com/2835/ work
    """
    if to_factoradic:
        assert convert(base_10) == factoradic
    else:
        assert convert(factoradic) == base_10
