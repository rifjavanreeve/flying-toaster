import os
import sys
import pytest

syspath = sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flying_toaster.toast import Toast

def test_get_roast_level_0():
    new_toast = Toast('Bread')
    seconds = 0

    new_toast.get_roast_level(seconds)

    assert new_toast.roast_level is 0
    assert new_toast.roast_levels[new_toast.roast_level] == 'not toasted'

def test_get_roast_level_1():
    new_toast = Toast('Bread')
    seconds = 13

    new_toast.get_roast_level(seconds)

    assert new_toast.roast_level is 1
    assert new_toast.roast_levels[new_toast.roast_level] == 'slightly toasted'

def test_get_roast_level_2():
    new_toast = Toast('Bread')
    seconds = 20

    new_toast.get_roast_level(seconds)

    assert new_toast.roast_level is 2
    assert new_toast.roast_levels[new_toast.roast_level] == 'well toasted'

def test_get_roast_level_3():
    new_toast = Toast('Bread')
    seconds = 31

    new_toast.get_roast_level(seconds)

    assert new_toast.roast_level is 3
    assert new_toast.roast_levels[new_toast.roast_level] == 'heavily toasted'

def test_get_roast_level_4():
    new_toast = Toast('Bread')
    seconds = 50

    new_toast.get_roast_level(seconds)

    assert new_toast.roast_level is 4
    assert new_toast.roast_levels[new_toast.roast_level] == 'burned'