from flying_toaster.slot import Slot

class Toaster():
    #TODO Toaster class
    slots = []
    toasting_time = None
    
    def __init__(self, number_of_slots, colour):
        self.colour = colour

        self._add_slots(number_of_slots)
    
    def _add_slots(self, number_of_slots):
        for number in range(number_of_slots):
            new_slot = Slot(number+1)

            self.slots.append(new_slot)

    def add_toasts(self, number_of_toasts):
        pass

    def remove_toasts(self):
        pass

    def toast(self):
        pass

    def set_timer(self, seconds):
        pass
