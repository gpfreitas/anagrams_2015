#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hypothesis import given, example
from hypothesis.strategies import text
import anagrams
from random import shuffle


@given(text())
def test_anagram_checker(s):
    def permute_characters(a):
        la = list(a)
        shuffle(la)
        return ''.join(la)
    is_anagram = anagrams.anagram_checker(s)
    assert is_anagram(permute_characters(s))


if __name__ == '__main__':
    test_anagram_checker()
