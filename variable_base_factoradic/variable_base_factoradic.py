"""
Implementation of https://xkcd.com/2835/
"""

from typing import Union
from logging import getLogger
from math import factorial
import warnings

logger = getLogger(__name__)


def convert(n: Union[str, int]):
    """
    Converts either a number to a factoradic string or a factoradic string to a number,
    based on the rules outlined in https://xkcd.com/2835/

    Deprecated, will be removed in 2.0: Use to_factoradic or from_factoradic instead
    """
    warnings.warn(
        "This function is deprecated and will be dropped in 2.0. "
        "Use to_factoradic or from_factoradic instead", DeprecationWarning
    )
    if isinstance(n, int):
        logger.debug("Converting %i to factoradic", n)
        return to_factoradic(n)
    if isinstance(n, str):
        logger.debug("Converting %s from factoradic", n)
        return from_factoradic(n)
    raise TypeError(f"Expected int or str, got {type(n)}")


def to_factoradic(n: int) -> str:
    """
    Convert a number to a factoradic string
    """
    components = []
    if n == 0:
        return "0"
    while n > 0:
        base = len(components) + 2
        if base > 10:
            raise ValueError("Numbers larger than 3628799 are simply illegal")
        n, d = divmod(n, base)
        components.append(d)
    logger.debug("Components: %s", components)
    return "".join([str(d) for d in components[::-1]])


def from_factoradic(n: str) -> int:
    """
    Convert a factoradic string to a number
    """
    components = [(i+2, d) for i, d in enumerate(n[::-1])]
    logger.debug("Components: %s", components)

    def to_factoradic_digit(digit: str, base: int) -> int:
        if base > 10:
            raise ValueError("Numbers larger than 3628799 are simply illegal")
        try:
            return int(digit, base=base) * factorial(base-1)
        except ValueError as err:
            raise ValueError(
                f"Invalid input: Digit at position {base - 2} must be in base {base}") from err

    return sum((to_factoradic_digit(d, i) for i, d in components))
