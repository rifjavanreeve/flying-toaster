from flying_toaster.toaster import Toaster

if __name__ == "__main__":
    new_toaster = Toaster(2, "pink")

    for slot in new_toaster._slots:
        print(slot.slot_number)
    print(new_toaster._colour)