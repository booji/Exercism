import threading

class BankAccount(object):
    def locking(func):
        """
        Given a method returns a method that uses lock calls the given method
        and then releases the lock
        """
        def wrapper(self, *args):
            with self.lock:
                return func(self, *args)
        return wrapper

    def is_open(func):
        """
        Given a method that checks to see if open state is True and then runs
        the given method
        """
        def wrapper(self, *args):
            if not(self.openState):
                raise ValueError(f"Account is not open. openState: {self.openState}")
            return func(self, *args)
        return wrapper

    def is_positive_amount(func):
        """
        Check if amount is postive
        """
        def wrapper(self,  amount):
            if  amount < 0:
                raise ValueError(f"Cannot have negative amount: {amount}")
            else:
                func(self, amount)
        return wrapper


    def __init__(self):
        self.balance = None
        self.openState = False
        self.lock = threading.Lock()

    @locking
    @is_open
    def get_balance(self):
        return self.balance

    @locking
    def open(self):
        if self.openState:
            raise ValueError(f"Account already open. openState: {self.openState}")
        self.balance = 0
        self.openState = True

    @locking
    @is_open
    @is_positive_amount
    def deposit(self, amount):
        self.balance += amount

    @locking
    @is_open
    @is_positive_amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"Withdraw amount ({amount}) is greater than balance amount ({self.balance})")
        self.balance -= amount

    @locking
    @is_open
    def close(self):
        self.balance=None
        self.openState=False
