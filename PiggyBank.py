from PiggyAccount import PiggyAccount


class PiggyBank:
    def __init__(self, init_value):
        self.accounts = []
        self.accounts.append(PiggyAccount("default"))
        self.get_account("default").funds = init_value

    def add_account(self, acct_name):
        if self.get_account(acct_name):
            print("Account with that name already exists.")
            return

        self.accounts.append(PiggyAccount(acct_name))

    def delete_account(self, acct_name):
        if not self.get_account(acct_name):
            print("No account with that name exists.")

        print("\nsending all funds from account to 'default' before deletion")
        self.get_account("default").deposit(self.get_account(acct_name).funds)
        self.accounts.remove(self.get_account(acct_name))
        return

    def rename_account(self, old_name, new_name):
        acct = self.get_account(old_name)
        if acct:
            acct.name = new_name
            return
        else:
            print("No account with name " + old_name)
            return

    def get_account(self, name):
        for a in self.accounts:
            if a.name == name:
                return a
        return False


    def deposit(self, amount, acct_name):
        if not self.get_account(acct_name):
            print("Invalid account name. Cannot deposit")
            return

        self.get_account(acct_name).deposit(amount)

    def withdraw(self, amount, acct_name):
        if not self.get_account(acct_name):
            print("Invalid account name. Cannot withdraw")
            return

        # if amount > self.get_account(acct_name).funds:
        #     print("Cannot withdraw, the amount specified is greater than the account value.")
        #     return

        self.get_account(acct_name).withdraw(amount)

    def transfer(self, amount, from_acct, to_acct):
        if not self.get_account(from_acct) or not self.get_account(to_acct):
            print("At least one invalid account name. Cannot transfer")
            return

        self.get_account(from_acct).withdraw(amount)
        self.get_account(to_acct).deposit(amount)

    def get_account_value(self, acct_name):
        if not self.get_account(acct_name):
            print("No valid account with that name.")
            return
        return self.get_account(acct_name).get_value

    def print_all_account_values(self):
        for acct in self.accounts:
            print(acct.name + " Account Value: $" + str(acct.get_value()))

    def get_total_value(self):
        sum = 0
        for acct in self.accounts:
            sum += acct.funds
        return sum


if __name__ == "__main__":
    a1 = PiggyBank(1000000)
    a1.add_account("House")
    a1.add_account("Vacation")
    a1.transfer(2000, "default", "House")
    a1.transfer(10000, "default", "Vacation")
    a1.print_all_account_values()
    a1.delete_account("Vacation")
    a1.print_all_account_values()
