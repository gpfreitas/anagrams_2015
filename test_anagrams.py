#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import doctest
import anagrams
import sys
import os
import shlex
import subprocess

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(anagrams))
    return tests

class TestAnagrams(unittest.TestCase):
    """Test the functions in the anagrams module."""
    def test_anagram_checker(self):
        is_anagram = anagrams.anagram_checker("typical")
        self.assertTrue(is_anagram("lacipyt"))

        is_anagram_sugar = anagrams.anagram_checker("açúcar")
        self.assertTrue(is_anagram_sugar("açúcar"))

        is_anagram_hyphen = anagrams.anagram_checker("with-hyphen")
        self.assertTrue(is_anagram_hyphen("hyphen-with"))


class TestAnagramsScript(unittest.TestCase):
    """Test the execution of the anagrams module as a script.

    During setUp, we will create a test data file containing various words. We
    will then remove the file during tearDown.

    """
    pass


if __name__ == '__main__':
    unittest.main()
