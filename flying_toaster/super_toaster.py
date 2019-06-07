from flying_toaster.toaster import Toaster


class SuperToaster(Toaster):
    _temperature = 0

    _flying = False

    def __init__(self, number_of_slots, alias, colour='gold'):
        super().__init__(number_of_slots, colour)

        self.alias = alias

    def toast(self):
        self._temperature = 0

        if not self._flying:
            super().toast(self._temperature_callback)

        else:
            print(f'You cannot toast any more, because {self.alias} flew away to save the world.')
    
    def super_boost_toast(self):
        self._temperature = 0

        if not self._flying:
            super().toast(self._boost_callback)

    def fly(self):
        self._flying = True

        print(f'Is it a bird? Is it a plane? No, it is {self.alias}!')

    def _temperature_callback(self, second):
        self._temperature = _linear_increase(second)

        if self._temperature > 500:
            raise Exception('Temperature of toaster exceeded 500 °C. Toasting aborted.')

    def _boost_callback(self, second):
        self._temperature = second ** 2

        if self._temperature > 1000:
            raise Exception('Splendid, you made the toaster angry. Its skin is turning green and he is going to smash you.')       
    
    def _linear_increase(self, x):
        return 10 * x