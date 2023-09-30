# Variable-base Factoadic numbers

Implementation of https://xkcd.com/2835/

## Installation

https://pypi.org/project/variable-base-factoradic/

```bash
pip install variable-base-factoradic
```

## Usage

```python
from variable_base_factoradic import convert

# Convert from decimal to factoradic
convert(5038)
# Out: "654320"

# Convert from factoradic to decimal
convert("654320")
# Out: 5038
```