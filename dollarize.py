# import moneyfmt
class Money:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'The value is {self.value}'

    def dollarize(self):
        return('The value in dollar format ${:0,.2f}'.format(self.value))

    def update(self, new_value):
        self.new_value = new_value
        self.value = self.new_value
        return f'The new value is {self.value}'
        


cash = Money(12345656)
print(cash)
print(cash.dollarize())
print(cash.update(67895678990))
print(cash.dollarize())

