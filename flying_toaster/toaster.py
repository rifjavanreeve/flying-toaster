from flying_toaster.slot import Slot

class Toaster():
    _slots = []
    
    def __init__(self, number_of_slots, colour):
        self._colour = colour

        self._add_slots(number_of_slots)
    
    def _add_slots(self, number_of_slots):
        for number in range(number_of_slots):
            new_slot = Slot(number+1)

            self._slots.append(new_slot)