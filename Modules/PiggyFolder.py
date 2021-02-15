class PiggyFolder:
    def __init__(self, name, total_funds_to_completion):
        self.name = name
        self.funds = 0
        self.risk_tolerance = 5  # 1-10
        self.total_funds_to_completion = total_funds_to_completion
        self.deposit_frequency = -1
        self.time_to_completion = -1

    def deposit(self, amount):
        self.funds += amount

    def withdraw(self, amount):
        if amount > self.funds:
            print("Cannot withdraw more than is in account.")
            return False
        self.funds -= amount

    def rename(self, new_name):
        self.name = new_name

    """ GETTERS """

    def get_value(self):
        return self.funds

    def get_name(self):
        return self.name

    def get_risk_tolerance(self):
        return self.risk_tolerance

    def set_risk_tolerance(self, level):
        self.risk_tolerance = level

    def calculate_time_to_completion(self, deposit_amount, deposit_frequency):
        """ Returns time (in months) to achieve goal given a deposit amount and frequency (per month)"""
        # TODO: Add interest into time equation
        """ Equation: months to goal = (total_funds - init) / (deposit_amt * deposits-per-months)"""

        amount_left = self.total_funds_to_completion - self.funds
        deposit_per_month = deposit_amount * deposit_frequency
        time_to_completion = amount_left / deposit_per_month

        return time_to_completion

    def calculate_deposit_amt(self, time_to_completion, deposit_frequency):
        """ Returns amount to deposit at specified interval to achieve goal in X months"""
        """ Equation: amount_to_deposit = (total_funds - init) / (deposits-per-month * months)"""
        amount_left = self.total_funds_to_completion - self.funds
        number_of_deposits = deposit_frequency * time_to_completion
        deposit_amt_per_freq = amount_left / number_of_deposits
        return deposit_amt_per_freq

    def calculate_deposit_freq(self, time_to_completion, deposit_amount):
        """ Returns how often to deposit a given amount to compelte in X months"""
        """ Equation: deposit_freq = (total_funds - init) / (deposit_amount * months)"""
        amount_left = self.total_funds_to_completion - self.funds
        freq_of_deposits = deposit_amount * time_to_completion
        deposit_freq = amount_left / freq_of_deposits
        return deposit_freq
