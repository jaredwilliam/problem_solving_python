class BankAccount:
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        self.amount -= withdraw_amount

    def transfer(self, other, transfer_amount):
        pass


class CheckingAccount(BankAccount):
    def __init__(self, name, amount=0):
        super(CheckingAccount, name).__init__(name, amount)


class SavingsAccount(BankAccount):
    def __init__(self, name, amount=0):
        super(SavingsAccount, name).__init__(name, amount)

        self.interest_rate = None

    def get_interest_rate(self):
        return self.interest_rate


class InvestmentAccount(BankAccount):
    def __init__(self, name, invested_amount, cash):
        super(InvestmentAccount, name).__init__(name)
        self.invested_amount = invested_amount
        self.cash = cash
        self.investments = None

    def get_invested_amount(self):
        return self.invested_amount

    def get_cash(self):
        return self.cash

    def get_investments(self):
        return self.investments

    def buy_stock(self, amount_to_buy):
        if self.cash >= amount_to_buy:
            self.invested_amount += amount_to_buy
            self.cash -= amount_to_buy
        else:
            raise RuntimeError(
                "Amount to buy cannot be less than cash available. Add cash."
            )

    def sell_stock(self, amount_to_sell):
        if amount_to_sell <= self.invested_amount:
            self.invested_amount -= amount_to_sell
            self.cash += amount_to_sell
        else:
            raise RuntimeError("Amount to sell cannot be more than amount invested.")

    def deposit_cash(self, cash_to_add):
        self.cash += cash_to_add

    def withdraw_cash(self, cash_to_withdraw):
        if cash_to_withdraw <= self.cash:
            self.cash -= cash_to_withdraw
        else:
            raise RuntimeError(
                "Amount to withdraw cannot be more than what is available."
            )


class Transfer:
    def __init__(self, from_account, to_account):
        self.from_account = from_account
        self.to_account = to_account

    def get_from_account(self):
        return self.from_account

    def get_to_account(self):
        return self.to_account
