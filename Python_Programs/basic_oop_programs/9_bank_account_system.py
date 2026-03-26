class Account:
    def __init__(self, name, acc_no, acc_type, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. Current Balance: {self.balance}")

    def display_balance(self):
        print(f"Balance: {self.balance}")

class sav_acct(Account):
    def __init__(self, name, acc_no, balance=0):
        super().__init__(name, acc_no, "Saving", balance)
        self.interest_rate = 0.05 # 5% compound interest

    def compute_and_deposit_interest(self, time):
        # Compound interest = P(1 + r/n)^(nt) - P
        # Simplified: Interest = P * r * t (assuming simple for this example or direct deposit)
        interest = self.balance * self.interest_rate * time
        self.balance += interest
        print(f"Interest added: {interest}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance")

class cur_acct(Account):
    MIN_BALANCE = 500
    PENALTY = 50

    def __init__(self, name, acc_no, balance=0):
        super().__init__(name, acc_no, "Current", balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
            self.check_min_balance()
        else:
            print("Insufficient balance")

    def check_min_balance(self):
        if self.balance < self.MIN_BALANCE:
            self.balance -= self.PENALTY
            print(f"Balance below minimum! Penalty of {self.PENALTY} imposed. New Balance: {self.balance}")

if __name__ == "__main__":
    print("--- Saving Account ---")
    s = sav_acct("Alice", 1001, 1000)
    s.display_balance()
    s.deposit(500)
    s.compute_and_deposit_interest(1)
    s.withdraw(200)

    print("\n--- Current Account ---")
    c = cur_acct("Bob", 2001, 1000)
    c.display_balance()
    c.withdraw(600) # Balance becomes 400, should trigger penalty
