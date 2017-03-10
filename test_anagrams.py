#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import anagrams
import sys
import os
import shlex
import subprocess
from nose.tools import with_setup, assert_true, assert_false, assert_equal


def test_anagrams():
    is_anagram = anagrams.anagram_checker("typical")
    true_anagrams = ['lacipyt', 'typical', 'picalty']
    for true_anagram in true_anagrams:
        assert_true(is_anagram(true_anagram))
    false_anagrams = ['Typical', 'typicul', 'typicall', '_typical', ' typical']
    for false_anagram in false_anagrams:
        assert_false(is_anagram(false_anagram))

    is_anagram_unicode_char = anagrams.anagram_checker("açúcar")
    assert_true(is_anagram_unicode_char("açúcar"))

    is_anagram_hyphen = anagrams.anagram_checker("with-hyphen")
    assert_true(is_anagram_hyphen("hyphen-with"))

    is_anagram_pound = anagrams.anagram_checker("symbol#")
    assert_true(is_anagram_pound("bol#sym"))

    is_anagram_trademark = anagrams.anagram_checker("trademark®")
    assert_true(is_anagram_trademark("®marktrade"))


class TestAnagramsScript:
    "Test the anagrams.py as a script."
    def setup(self):
        self.params = {'base_word': 'lambs',
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

        # Create test data file
        lines = '\n'.join(self.params['words'])
        with open(self.params['test_data_fname'], 'w') as f:
            f.writelines(lines)

    def teardown(self):
        # Remove test data file.
        os.remove(self.params['test_data_fname'])

    def test_anagrams_script(self):
        """Test the execution of the anagrams module as a script.

        During setUp, we will create a test data file containing various words. We
        will then remove the file during tearDown.

        """
        cmd = ('{python_exe} {script_path} {base_word} {test_data_fname}'
               .format(**self.params))
        cmd_split = shlex.split(cmd)
        output = subprocess.check_output(cmd_split).decode('utf-8').split()
        assert_equal(output, self.params['anagrams'])


if __name__ == "__main__":
    import nose
    nose.run(argv=[__file__, '-vv', '--exe', '--with-doctest'])
