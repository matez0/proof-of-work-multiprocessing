# Calculating proof of work suffix with multiprocessing

Given an input data as an utf-8 string and a difficulty number,
a suffix is a [proof of work](https://en.wikipedia.org/wiki/Proof_of_work) (PoW) of the input data,
if the hex dump of the SHA1 hash of the concatenation of the input data and the suffix
starts with difficulty number of zeros.

The search for PoW suffix is distributed among the CPU cores using the multiprocessing python module.
For higher performance, the search process is implemented in C.


## Build

Dependencies:
- openssl-dev
- python
- pytest

Build the library for finding suffixes:
```
make
```


## Usage

```python
from pow_calculator import calculate_pow

suffix = calculate_pow('input data', difficulty=5)
```


## Acknowledgement

[Exasol](https://www.exasol.com/)
