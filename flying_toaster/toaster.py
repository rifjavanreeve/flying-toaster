from collections import deque
import time
from numbers import Number
from flying_toaster.slot import Slot
from flying_toaster.toast import Toast

class Toaster():
    
    slots = []
    _toasting_time = None
    
    def __init__(self, number_of_slots, colour):
        self.colour = colour

        self._add_slots(number_of_slots)
    
    def _add_slots(self, number_of_slots):
        for number in range(number_of_slots):
            new_slot = Slot(number+1)

            self.slots.append(new_slot)

    def add_toasts(self, number_of_toasts, bread_type):
        empty_slots = [slot for slot in self.slots if slot.is_empty()]
        
        empty_deque = deque(empty_slots)

        if [slot for slot in self.slots if not slot.is_empty() and slot.toast.is_toasted()]:
            raise Exception('There are still toasted toasts in the slots. Empty toaster first.')
        
        if number_of_toasts > len(self.slots):
            raise ValueError('Cannot toast more toasts than number of slots at once.')
        
        if len(empty_slots) is 0 or len(empty_slots) < number_of_toasts:
            raise ValueError('There are not enough empty slots available. Empty toaster first.') 

        while number_of_toasts > 0:
            empty_slot = empty_deque.popleft()

            empty_slot.toast = Toast(bread_type)

            number_of_toasts -= 1      
        
    def remove_toasts(self):
        if len(self.slots) > 0:
            self.slots = []

    def toast(self):
        if self._toasting_time is None:
            raise ValueError('Cannot toast because time has not been set yet.')

        for second in range(self._toasting_time+1):
            print('Toasting... [%d seconds]\r'%second, end="")
            time.sleep(1)

        print('Finished toasting. Please remove toasts and enjoy.')

    def set_timer(self, seconds):
        self._toasting_time = seconds
