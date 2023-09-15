class Budget:

    deposit = 100
    withdraw = 30

    def __init__(self,deposit,withdraw):
        self.deposit = deposit
        self.withdraw = withdraw

    def deposit(self,amount):
        return self.deposit

    def withdraw(self,amount):
        return self.withdraw

    def transfer(self,amount):
        return self.transfer
  
food = Budget("Food", 400, 50)
clothing = Budget("clothing", 50, 10)
entertainment = Budget("entertainment", 75, 25)

print(food.money,food.balance)
print(clothing.money,clothing.balance)
print(entertainment.money,entertainment.balance)






"""
Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, 
and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well 
computing category balances and transferring balance amounts between categories”
"""
