from flying_toaster.toaster import Toaster

if __name__ == "__main__":
    new_toaster = Toaster(2, "pink")

    for slot in new_toaster.slots:
        print(slot.slot_number)
    print(new_toaster.colour)