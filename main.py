from flying_toaster.toaster import Toaster
from flying_toaster.super_toaster import SuperToaster

def print_toaster(toaster):
    print('model: ', type(toaster).__name__)
    if isinstance(toaster, SuperToaster):    
        print('alias: ', toaster.alias)
    print('colour: ', toaster.colour)
    print('number of slots: ', len(toaster.slots))

def get_toaster(toaster_type):
    try:
        slots = input('\nHow many slots?: ')
        colour= input('\nWhich colour?: ')
        
        toaster = None

        if toaster_type == str(1):
            toaster = Toaster(int(slots), colour)

        elif toaster_type == str(2):
            alias = input('\nWhat is the alias of your toaster?: ')
            
            toaster = SuperToaster(int(slots), alias, colour)

        print('\nHere is your wonderful toaster!\n')
        print_toaster(toaster)

        toasts = input('\nHow many toasts would you like?: ')
        bread = input('\nWhich bread?: ')
        toaster.add_toasts(int(toasts), bread)

        time = input('\nHow many seconds?: ')
        toaster.set_timer(int(time))

        toaster.toast()
    
    except:
        exit(1)

def main():
    print('What toaster do you want?\n')
    print('Toaster: press [1]')
    print('SuperToaster: press [2]')

    toaster = input('\nToaster: ')
    
    if toaster in [str(1), str(2)]:
        get_toaster(toaster)

    else:
        print('\nInvalid input!')

    end_loop = input('\nExit program? [y/n]: ')

    if end_loop == 'n' or end_loop == 'N':
        main()


if __name__ == '__main__':
    main()