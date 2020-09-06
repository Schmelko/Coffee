class Coffee:
    def __init__(self, name, coffee_type, coffee_price, coffee_balance, min_coffee_balance):

        self.name = name
        self.coffee_type = coffee_type
        self.coffee_price = coffee_price
        self.coffee_balance = coffee_balance
        self.min_coffee_balance = min_coffee_balance

    def inputmoney(self, amount):
        self.coffee_balance += amount

    def moneyout(self, amount):
        if self.coffee_balance - amount >= 490:
            self.coffee_balance -= amount

    def statement(self):                                                             
        if self.coffee_balance >= 4800:
            print("your member coffee_balance is less than the minimum member balance, so you cannot drink mespresso but you can drink the other coffees at normal price!".format(self.coffee_balance))
        elif self.coffee_balance >= 700:
           print("your current coffee balance is: HUF {}, you can drink a capuccino!".format(self.coffee_balance))
        elif self.coffee_balance >= 600:
           print("your current coffee balance is: HUF {}, you can drink a doppio!".format(self.coffee_balance))
        elif self.coffee_balance >= 490:
            print("your current coffee balance is: HUF {}, you can drink an espresso!".format(self.coffee_balance))
        else:
            print("your current coffee balance is: HUF {}, you cannot drink any coffee at the moment!".format(self.coffee_balance))

    def coffee_price(self, coffee_price, coffee_type,member_coffee_type, member_coffee_price):
       if self.coffee_type == "capuccino":
            self.coffee_price = 700
       elif self.coffee_type == "doppio":
            self.coffee_price = 600
       elif self.coffee_type =="espresso":
            self.coffee_price =490
       else:
            self.coffee_type == "mespresso"
            self.coffee_price =450
   
class Member(Coffee):
    def __init__(self, name, coffee_type, coffee_price, coffee_balance, min_coffee_balance):
         super().__init__(name, coffee_type, coffee_price, coffee_balance, min_coffee_balance = 4900)

    def __str__(self):
        return"{}, your current coffee balance is: HUF {}, pay the minimum member coffee balance {} to drink member coffee!".format(self.name, coffee_balance, min_coffee_balance)                                                                                     
