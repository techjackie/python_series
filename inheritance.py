class JamesPotter:
    def __init__(self, power):
        print('My Power is ',power)
        self.name = "JamesPotter"

    def magic_power(self):
        print('I have magic powers!..')


class HarryPotter(JamesPotter):
    def __init__(self):
        super().__init__('invisible')
        JamesPotter.__init__(self, 'invisible')

hp = HarryPotter()
hp.magic_power()
print(hp.name)