# July 23, 2018
# redesigned-computing-machine
# the basic game loop
class BankAccount(object):
    def __init__(self, label, balance, withdraw, deposit, rename):
        self.label = label
        self.balance = balance
        self.withdraw = withdraw
        self.deposit = deposit
        self.rename = rename
