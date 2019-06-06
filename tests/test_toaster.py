import os
import sys
import pytest

syspath = sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flying_toaster.toaster import Toaster

def test_create_toaster_with_colour():
    slots = 2
    colour = 'orange'
    new_toaster = Toaster(slots, colour)

    assert new_toaster is not None
    assert len(new_toaster.slots) is slots
    assert new_toaster.colour is colour

def test_create_toaster_wo_colour():
    slots = 3
    new_toaster = Toaster(slots)

    assert new_toaster is not None
    assert len(new_toaster.slots) is slots
    assert new_toaster.colour is 'silver'

def test_add_toasts():
    toasts = 2
    bread_type = 'Bread'
    new_toaster = Toaster(2)

    new_toaster.add_toasts(toasts, bread_type)

    for slot in new_toaster.slots:
        assert slot.toast is not None
        assert slot.toast.bread_type is bread_type

def test_add_toasts_more_toasts_than_slots():
    new_toaster = Toaster(2)

    with pytest.raises(Exception):
        new_toaster.add_toasts(3, 'Bread')

def test_add_toasts_wo_removing_toasted_slices():
    new_toaster = Toaster(5)
    new_toaster.add_toasts(2, 'Bread')

    new_toaster.set_timer(3)
    new_toaster.toast()

    with pytest.raises(Exception) as exception:
        new_toaster.add_toasts(2, 'Vollkorn')
        
        assert isinstance(exception, ValueError)

def test_add_toasts_not_enough_empty_slots():
    new_toaster = Toaster(4)
    new_toaster.add_toasts(2, 'Bread')

    with pytest.raises(Exception) as exception:
        new_toaster.add_toasts(3, 'Bread')
        
        assert isinstance(exception, ValueError)

def test_remove_toasts():
    new_toaster = Toaster(2)
    new_toaster.add_toasts(2, 'Bread')

    new_toaster.remove_toasts()

    for slot in new_toaster.slots:
        assert slot.toast is None

def test_toast():
    new_toaster = Toaster(2)
    new_toaster.add_toasts(2, 'Bread')

    new_toaster.set_timer(3)

    new_toaster.toast()

    for slot in new_toaster.slots:
        assert slot.toast.roast_level > 0

def test_toast_wo_toasting_time():
    new_toaster = Toaster(2)
    new_toaster.add_toasts(2, 'Bread')

    with pytest.raises(Exception) as exception:
        new_toaster.toast()
        
        assert isinstance(exception, ValueError) 