class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def handle_transaction(account, transaction_amount):
        new_balance = account.balance + transaction_amount
        if new_balance < 0:
            raise ValueError("sorry cannot go in debt!")
        account._transactions.append(transaction_amount)
        return f"New balance: {account.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        new_balance = self.balance + amount
        if new_balance < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transactions.append(amount)
        return f"New balance: {self.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return self._transactions[::-1]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        owner = f'{self.owner}&{other.owner}'
        amount = self.amount + other.amount
        result = Account(owner, amount)
        for tx in self:
            result.add_transaction(tx)
        for tx in other:
            result.add_transaction(tx)
        return result


