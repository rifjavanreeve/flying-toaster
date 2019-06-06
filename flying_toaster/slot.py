from flying_toaster.toast import Toast


class Slot():

    toast = None

    def __init__(self, slot_number):
        self.slot_number = slot_number

    def is_empty(self):
        return self.toast == None

    def add_toast(self, bread_type):
        self.toast = Toast(bread_type)

    def remove_toast(self):
        self.toast = None