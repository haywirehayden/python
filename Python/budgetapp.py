
class Budget:

    def __init__(self,moneyvalue,balance):
        self.moneyvalue = moneyvalue
        self.balance = balance

    def depositmoney(self,amount):
        self.balance += amount
        return "You have deposited the amount of: " + self.moneyvalue 

    def withdrawmoney(self,amount):
        self.balance += amount
        return "You have withdrawn the amount of: " + self.moneyvalue

    def transfermoney(self,amount):
        self.balance += amount
        return "You have withdrawn the amount of: " + self.balance
  
food = Budget("Food", 400)
clothing = Budget("clothing", 50)
entertainment = Budget("entertainment", 75)

print(food.moneyvalue, food.balance)
print(clothing.moneyvalue, clothing.balance)
print(entertainment.moneyvalue, entertainment.balance)