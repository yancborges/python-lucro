class Value:

    def __init__(self, day, value):

        self.day = day
        self.price = value


    def __str__(self):
        return 'Day #{}, price: ${}'.format(self.day, self.price)
