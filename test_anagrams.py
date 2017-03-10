#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import anagrams
import sys
import os
import shlex
import subprocess

from nose.tools import with_setup


def test_anagrams():
        is_anagram = anagrams.anagram_checker("typical")

        assert is_anagram("lacipyt")
        assert is_anagram("typical")
        assert not is_anagram("Typical")
        assert not is_anagram("typicul")
        assert not is_anagram("typicall")
        assert not is_anagram("_typical")
        assert not is_anagram(" typical")

        is_anagram_sugar = anagrams.anagram_checker("açúcar")
        assert is_anagram_sugar("açúcar")

        is_anagram_hyphen = anagrams.anagram_checker("with-hyphen")
        assert is_anagram_hyphen("hyphen-with")

        is_anagram_pound = anagrams.anagram_checker("symbol#")
        assert is_anagram_pound("bol#sym")

        is_anagram_trademark = anagrams.anagram_checker("trademark®")
        assert is_anagram_trademark("®marktrade")


# data for test_anagrams_script
TEST_SCRIPT_PARAMS = {'base_word': 'lambs',
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

def setup_test_anagrams_script():
    # Create test data file
    lines = '\n'.join(TEST_SCRIPT_PARAMS['words'])
    with open(TEST_SCRIPT_PARAMS['test_data_fname'], 'w') as f:
        f.writelines(lines)

def teardown_test_anagrams_script():
    # Remove test data file.
    os.remove(TEST_SCRIPT_PARAMS['test_data_fname'])

@with_setup(setup_test_anagrams_script, teardown_test_anagrams_script)
def test_anagrams_script():
    """Test the execution of the anagrams module as a script.

    During setUp, we will create a test data file containing various words. We
    will then remove the file during tearDown.

    """
    cmd = ('{python_exe} {script_path} {base_word} {test_data_fname}'
           .format(**TEST_SCRIPT_PARAMS))
    cmd_split = shlex.split(cmd)
    output = subprocess.check_output(cmd_split).decode('utf-8').split()
    assert output == TEST_SCRIPT_PARAMS['anagrams']


if __name__ == "__main__":
    import nose
    nose.run()
