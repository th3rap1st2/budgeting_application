# import json
# import os
from datetime import datetime



    A User class to keep track of name and email.
    """
    name: str
    email: str

    def __init__(self) -> None:
        self._name = input("What's your full name: ")
        self._email = input("What's your email: ")

    def get_name(self) -> str:
        return self._name


class DebitCard:
    pass


class CreditCard:
    pass


class BudgetApp:
    """
    A class that keeps tracks of user's budgeting details including their name, monthly budget, current balance,
    and total number of transactions.
    """
    user: User
    monthly_budget: float
    current_balance: float
    transactions: list
    total_transactions: int

    def __init__(self, user: User) -> None:
        self.user = user
        self.current_balance = float(input("What is your current balance: "))
        self.monthly_budget = float(input("What is your monthly budget: "))
        self.transactions = []

        while self.current_balance < self.monthly_budget:
            print("Your monthly budget is over what you currently have! Please try again...")
            self.monthly_budget = float(input("What is your monthly budget: "))

        self.total_transactions = 0

    def get_transaction_summary(self, transaction_amount: float, type_trans: str):
        print(datetime.today().strftime('%Y-%m-%d'))
        print(f"Your recorded transaction: ${transaction_amount:.2f} on {type_trans.lower()}")
        print(f"Your remaining budget: ${self.monthly_budget:.2f}")
        print(f"Your current balance: ${self.current_balance:.2f}")
        print(f"Total transactions: {self.total_transactions}")

        self.transactions.append([type_trans, transaction_amount])

    def update_balance(self):
        deduction = float(input("How much was your transaction: "))
        type_transaction = input("What is the type of transaction (Food/Rent/Entertainment): ")

        while self.current_balance - deduction < 0:
            print("Insufficient funds! Please try again...")
            deduction = float(input("How much was your transaction: "))

        self.current_balance -= deduction
        self.monthly_budget -= deduction
        self.total_transactions += 1

        if self.monthly_budget < 0:
            self.monthly_budget = 0
            print(f"{self.user.get_name().split(' ', 1)[0]}, you went over your monthly budget"
                  f"... make smarter decisions!")

        self.get_transaction_summary(deduction, type_transaction)

    def get_transactions(self):
        return self.transactions


user = User()
budget = BudgetApp(user)
budget.update_balance()
budget.update_balance()
budget.get_transactions()
