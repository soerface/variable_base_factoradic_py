from typing import Union
from logging import getLogger
from math import factorial

logger = getLogger(__name__)


def convert(n: Union[str, int]):
    """
    Converts either a number to a factoradic string or a factoradic string to a number, based on the rules
    outlined in https://xkcd.com/2835/
    """
    if isinstance(n, int):
        logger.debug("Converting %i to factoradic", n)
        return _to_factoradic(n)
    if isinstance(n, str):
        logger.debug("Converting %s from factoradic", n)
        return _from_factoradic(n)
    raise TypeError(f"Expected int or str, got {type(n)}")


def _to_factoradic(n: int) -> str:
    """
    Convert a number to a factoradic string
    """
    components = []
    while n > 0:
        n, d = divmod(n, len(components) + 2)
        components.append(d)
    logger.debug("Components: %s", components)
    return "".join([str(d) for d in components[::-1]])


def _from_factoradic(n: str) -> int:
    components = [(i+1, d) for i, d in enumerate(n[::-1])]
    logger.debug("Components: %s", components)
    return sum([int(d) * factorial(i) for i, d in components])