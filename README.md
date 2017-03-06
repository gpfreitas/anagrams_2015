[![Build Status](https://travis-ci.org/gpfreitas/anagrams_2015.svg?branch=master)](https://travis-ci.org/gpfreitas/anagrams_2015)
[![Coverage Status](https://coveralls.io/repos/github/gpfreitas/anagrams_2015/badge.svg?branch=master)](https://coveralls.io/github/gpfreitas/anagrams_2015?branch=master)

# Anagrams

A string is a sequence of characters. A string `x` is an anagram of string
`y` if and only if the characters of `x` are a permutation of the
characters of `y`.

The script `anagrams.py` allows the user to extract anagrams of a given input
word from a file containing one word per line. For usage information, run

```bash
python3 anagrams.py -h
```

The script `test_anagrams.py` contains tests for the script `anagrams.py`.
To run the tests, run 

```bash
python3 /test_anagrams.py
```

This tests both the routines inside `anagrams.py` and the execution of
`anagrams.py` as a script.

For more information, read the documentation in `anagrams.py` and/or inspect
its source code.


## Data

A compressed datafile `words.txt.zip` is included for experimentation. It can
be decompressed with

```bash
python -m zipfile -e words.txt.zip
```
Once decompressed, `words.txt` has one word per line.

