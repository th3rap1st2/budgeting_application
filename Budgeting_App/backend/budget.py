from datetime import datetime
from typing import Dict, Any

class User:
    """
    A User class to keep track of name and email.
    """
    name: str
    email: str

    def __init__(self, name: str, email: str) -> None:
        self._name = name
        self._email = email

    def get_name(self) -> str:
        return self._name
    
    def to_dict(self) -> Dict[str, Any]:
        return {"name": self._name, "email": self._email}
    
    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "User":
        return User(d["name"], d["email"])


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

    def __init__(self, user: User, current_balance: float, monthly_budget: float) -> None:
        self.user = user
        self.current_balance = current_balance
        self.monthly_budget = monthly_budget
        self.transactions = []
        self.total_transactions = 0

        if self.current_balance < self.monthly_budget:
            self.monthly_budget = self.current_balance  


    def update_balance(self, amount: float, type_transaction: str):
        """
        updates the user's balance
        """
        amount = float(amount)
        if self.current_balance - amount < 0:
            raise ValueError("Insufficient funds!")

        self.current_balance -= amount
        self.monthly_budget = max(0.0, self.monthly_budget - amount)
        self.total_transactions += 1

        date_str = datetime.today().strftime('%Y-%m-%d')
        self.transactions.append({"type": type_transaction, "amount": amount, "date": date_str})

        return self.get_transaction_summary(amount, type_transaction, date_str)

    def get_transaction_summary(self, transaction_amount: float, type_trans: str, date_str: str):
        """
        returns the summary of the transaction
        """

        return {
            "date": date_str,
            "message": f"Your recorded transaction: ${transaction_amount:.2f} on {type_trans.lower()}",
            "remaining_budget": round(self.monthly_budget, 2),
            "current_balance": round(self.current_balance, 2),
            "total_transactions": self.total_transactions
        }