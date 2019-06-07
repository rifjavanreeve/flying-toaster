import os
import sys
import pytest

syspath = sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flying_toaster.super_toaster import SuperToaster

test_toaster = SuperToaster(2, 'Super-Toaster')

def test_create_super_toaster():
    slots = 4
    alias = 'Black Toaster'
    colour = 'black'

    super_toaster = SuperToaster(slots, alias, colour)

    assert super_toaster is not None
    assert isinstance(super_toaster, SuperToaster)
    assert len(super_toaster.slots) == slots
    assert super_toaster.alias == alias
    assert super_toaster.colour == colour

def test_create_super_toaster_wo_colour():
    slots = 4
    alias = 'Black Toaster'

    super_toaster = SuperToaster(slots, alias)

    assert super_toaster is not None
    assert isinstance(super_toaster, SuperToaster)
    assert len(super_toaster.slots) == slots
    assert super_toaster.alias == alias
    assert super_toaster.colour == 'gold'

def test_super_toaster_toast():
    test_toaster.remove_toasts()

    test_toaster.add_toasts(2, 'Kryptonite')
    test_toaster.set_timer(3)

    test_toaster.toast()

    for slot in test_toaster.slots:
        assert slot.toast.roast_level > 0


def test_super_toaster_toast_when_flying():
    flying_toaster = SuperToaster(2, 'Captain Toaster')

    flying_toaster.add_toasts(2, 'Corned Beef')
    flying_toaster.set_timer(3)

    flying_toaster.fly()
    
    with pytest.raises(Exception) as exception:
        flying_toaster.toast()

def test_super_toaster_toast_overheat():
    test_toaster.remove_toasts()

    test_toaster.add_toasts(2, 'Bread')
    test_toaster.set_timer(51)

    with pytest.raises(Exception) as exception:
        test_toaster.toast()

def test_super_boost_toast():
    test_toaster.remove_toasts()

    test_toaster.add_toasts(2, 'Bread')
    test_toaster.set_timer(3)

    test_toaster.super_boost_toast()

    for slot in test_toaster.slots:
        assert slot.toast.roast_level > 0

def test_super_boost_toast_when_flying():
    flying_toaster = SuperToaster(2, 'DareToaster', 'red')
    
    flying_toaster.add_toasts(2, 'Bread?')
    flying_toaster.set_timer(3)

    flying_toaster.fly()
    
    with pytest.raises(Exception) as exception:
        flying_toaster.super_boost_toast()

def test_super_boost_toast_make_angry():
    test_toaster.remove_toasts()

    test_toaster.add_toasts(2, 'Crunchy Stones')
    test_toaster.set_timer(11)

    with pytest.raises(Exception) as exception:
        test_toaster.super_boost_toast()

def test_add_toasts_when_flying():
    flying_toaster = SuperToaster(2, 'Spider-Toaster')

    flying_toaster.fly()

    with pytest.raises(Exception) as exception:
        flying_toaster.add_toasts(2, 'Bread')

def test_remove_toasts_when_flying():
    flying_toaster = SuperToaster(2, 'Moon Toaster')
    flying_toaster.add_toasts(2, 'Moonbread')

    flying_toaster.fly()

    with pytest.raises(Exception) as exception:
        flying_toaster.remove_toasts()

def test_set_timer_when_flying():
    flying_toaster = SuperToaster(2, 'Agent Toaster')

    flying_toaster.fly()

    with pytest.raises(Exception) as exception:
        flying_toaster.set_timer(30)