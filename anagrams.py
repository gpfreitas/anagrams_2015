#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Anagrams
========

A string is a sequence of characters. A string ``x`` is an anagram of string
``y`` if and only if the characters of ``x`` are a permutation of the
characters of ``y``.

This script allows the user to extract anagrams of a given input word from a
file containing one word per line. For more details, see the documentation of
the ``anagram_checker`` function.

"""


def anagram_checker(target_word):
    """Generates boolean function that checks if input is anagram of base_word

    Parameters
    ----------
    base_word: str

    Returns
    -------
    is_anagram: function
        ``is_anagram(word)`` is ``True`` if and only ``word`` is an anagram of
        ``base_word``.

    Examples
    --------

    >>> is_anagram = anagram_checker('lambs')
    >>> is_anagram('balms')
    True

    """
    pass


if __name__ == "__main__":
    import sys
    from itertools import takewhile

    input_file = sys.argv[2]
    target_word = sys.argv[1]

    is_anagram = anagram_checker(target_word)

    with open(input_file) as f:
        words = takewhile(bool, (l.rstrip() for l in f))
        anagrams = filter(is_anagram, words)
        for word in anagrams:
            print(word)
