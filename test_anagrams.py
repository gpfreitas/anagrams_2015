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
    """Loads the tests in the documentation of anagrams.py"""
    tests.addTests(doctest.DocTestSuite(anagrams))
    return tests


class TestAnagrams(unittest.TestCase):
    """Test the functions in the anagrams module."""

    def test_anagram_checker(self):
        # I chose to repeat the code for every "assertTrue/assertFalse" because
        # if something fails, I _think_ it will be easier to see which word is
        # generating the problem without a debugger.
        is_anagram = anagrams.anagram_checker("typical")
        self.assertTrue(is_anagram("lacipyt"))
        self.assertTrue(is_anagram("typical"))
        self.assertFalse(is_anagram("Typical"))
        self.assertFalse(is_anagram("typicul"))
        self.assertFalse(is_anagram("typicall"))
        self.assertFalse(is_anagram("_typical"))
        self.assertFalse(is_anagram(" typical"))

        is_anagram_sugar = anagrams.anagram_checker("açúcar")
        self.assertTrue(is_anagram_sugar("açúcar"))

        is_anagram_hyphen = anagrams.anagram_checker("with-hyphen")
        self.assertTrue(is_anagram_hyphen("hyphen-with"))

        is_anagram_pound = anagrams.anagram_checker("symbol#")
        self.assertTrue(is_anagram_pound("bol#sym"))

        is_anagram_trademark = anagrams.anagram_checker("trademark®")
        self.assertTrue(is_anagram_trademark("®marktrade"))


class TestAnagramsScript(unittest.TestCase):
    """Test the execution of the anagrams module as a script.

    During setUp, we will create a test data file containing various words. We
    will then remove the file during tearDown.

    """
    params = {'base_word': 'lambs',
              'words': ['blams',
                        'rock',
                        'lambs',
                        'mlabs',
                        'Lambs',
                        '_lambs',
                        ' lambs'],
              'anagrams': ['blams', 'lambs', 'mlabs'],
              'test_data_fname': 'test_data_823492kwjsl347216.txt',
              'python_exe': sys.executable,
              'script_path': anagrams.__file__}

    def setUp(self):
        # Create test data file
        lines = '\n'.join(self.params['words'])
        with open(self.params['test_data_fname'], 'w') as f:
            f.writelines(lines)

    def tearDown(self):
        # Remove test data file.
        os.remove(self.params['test_data_fname'])

    def test_anagrams_script(self):
        cmd = ('{python_exe} {script_path} {base_word} {test_data_fname}'
               .format(**self.params))
        cmd_split = shlex.split(cmd)
        output = subprocess.check_output(cmd_split).decode('utf-8').split()
        self.assertTrue(output == self.params['anagrams'])


if __name__ == '__main__':
    unittest.main()
