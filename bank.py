class Account:
    def __init__(self, owner, balance=0):
        """Initialize an account with an owner name and an optional starting balance.

        Args:
            owner (str): The name of the account owner.
            balance (float): The initial balance of the account (default is 0).
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit a positive amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is not positive.

        Returns:
            float: The new balance after the deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw a positive amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is not positive or exceeds the balance.

        Returns:
            float: The new balance after the withdrawal.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """Get the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self.balance

    def transfer(self, amount, to_account):
        """Transfer a positive amount to another account.

        Args:
            amount (float): The amount to transfer.
            to_account (Account): The account to which the amount is transferred.

        Raises:
            ValueError: If the transfer amount is not positive or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.withdraw(amount)
        to_account.deposit(amount)