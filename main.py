from flying_toaster.toaster import Toaster

if __name__ == "__main__":
    new_toaster = Toaster(5, "pink")

    for slot in new_toaster.slots:
        print(slot.slot_number, slot.is_empty())
    print(new_toaster.colour)

    new_toaster.add_toasts(1, "Bread")

    for slot in new_toaster.slots:
        print(slot.is_empty())

    new_toaster.add_toasts(4, "Vollkorn")

    for slot in new_toaster.slots:
        print(slot.toast.bread_type)

    new_toaster.set_timer(3)
    new_toaster.toast()