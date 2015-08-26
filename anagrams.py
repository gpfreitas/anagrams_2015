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

Even though tests and other files were originally provided with this file, you
can use this file as a standalone script as follows. For usage instructions,
run

::
    ./anagrams.py -h

"""


def anagram_checker(target_word, anagram_signature=sorted):
    """Generates boolean function that checks if input is anagram of target_word

    Parameters
    ----------
    target_word: str (not bytes)
        This is the word we will use a comparison point. We want to test if
        other words are an anagram of this word.
    anagram_signature: function, optional
        This must satisfy ``anagram_signature(word) ==
        anagram_signature(target_word)`` if and only if ``word`` is an anagram of
        ``target_word``. Default is ``sorted``, but you can experiment with other
        functions, like ``collections.Counter`` if you want.

    Returns
    -------
    is_anagram: function
        ``is_anagram(word)`` is ``True`` if and only ``word`` is an anagram of
        ``target_word``.

    Examples
    --------

    >>> is_anagram = anagram_checker('lambs')
    >>> is_anagram('balms')
    True
    >>> is_anagram('lambs')
    True
    >>> is_anagram('_balms')
    False
    >>> is_anagram(' balms')
    False
    >>> is_anagram('Balms')
    False

    Using a different ``anagram_signature`` function:

    >>> from collections import Counter
    >>> is_anagram = anagram_checker('lambs', anagram_signature=Counter)
    >>> words = ['balms', 'lambs', '_balms', ' balms', 'Balms']
    >>> list(filter(is_anagram, words))
    ['balms', 'lambs']

    """
    target_word_signature = anagram_signature(target_word)

    def is_anagram(word):
        other_word_signature = anagram_signature(word)
        return target_word_signature == other_word_signature
    return is_anagram


if __name__ == "__main__":
    from itertools import takewhile
    import argparse

    parser = argparse.ArgumentParser(description='Find anagrams of target_word'
            ' in file fname')
    parser.add_argument(dest='target_word', type=str, help='Word against which'
            ' we will check anagrams')
    parser.add_argument(dest='fname', type=str, help='Input file with one word'
            ' per line where we will look for anagrams')
    args = parser.parse_args()

    # Change anagram_signature if you want to test some other function like
    # collections.Counter. In Python3.4, on my machine, collections.Counter is
    # slower than sorted.
    is_anagram = anagram_checker(args.target_word, anagram_signature=sorted)

    with open(args.fname) as f:
        words = takewhile(bool, (l.rstrip() for l in f))
        anagrams = filter(is_anagram, words)
        for word in anagrams:
            print(word)
