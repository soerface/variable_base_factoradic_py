# Variable-base Factoradic numbers

Implementation of https://xkcd.com/2835/

## Installation

https://pypi.org/project/variable-base-factoradic/

```bash
pip install variable-base-factoradic
```

## Usage

```python
from variable_base_factoradic import from_factoradic, to_factoradic

# Convert from decimal to factoradic
to_factoradic(5038)
# Out: "654320"

# Convert from factoradic to decimal
from_factoradic("654320")
# Out: 5038
```