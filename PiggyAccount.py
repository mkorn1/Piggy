class PiggyAccount:
    def __init__(self, name):
        self.name = name
        self.funds = 0
        self.risk_tolerance = 5  # 1-10

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