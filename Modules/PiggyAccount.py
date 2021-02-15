from PiggyFolder import PiggyFolder


class PiggyAccount:
    def __init__(self, acct_name, init_value):
        self.name = acct_name
        self.folders = []
        self.folders.append(PiggyFolder("default", 0))
        self.get_folder("default").funds = init_value

    def add_folder(self, folder_name, amount_to_completion):
        if self.get_folder(folder_name):
            print("Account with that name already exists.")
            return

        self.folders.append(PiggyFolder(folder_name, amount_to_completion))

    def delete_folder(self, folder_name):
        if not self.get_folder(folder_name):
            print("No account with that name exists.")

        print("\nsending all funds from account to 'default' before deletion")
        self.get_folder("default").deposit(self.get_folder(folder_name).funds)
        self.folders.remove(self.get_folder(folder_name))
        return

    def rename_folder(self, old_name, new_name):
        folder = self.get_folder(old_name)
        if folder:
            folder.name = new_name
            return
        else:
            print("No Folder with name " + old_name)
            return

    def get_folder(self, name):
        for a in self.folders:
            if a.name == name:
                return a
        return False


    def deposit(self, amount, acct_name):
        if not self.get_folder(acct_name):
            print("Invalid Folder name. Cannot deposit")
            return

        self.get_folder(acct_name).deposit(amount)

    def withdraw(self, amount, acct_name):
        if not self.get_folder(acct_name):
            print("Invalid Folder name. Cannot withdraw")
            return

        # if amount > self.get_folder(acct_name).funds:
        #     print("Cannot withdraw, the amount specified is greater than the folder value.")
        #     return

        self.get_folder(acct_name).withdraw(amount)

    def transfer(self, amount, from_acct, to_acct):
        if not self.get_folder(from_acct) or not self.get_folder(to_acct):
            print("At least one invalid folder name. Cannot transfer")
            return

        self.get_folder(from_acct).withdraw(amount)
        self.get_folder(to_acct).deposit(amount)

    def get_folder_value(self, acct_name):
        if not self.get_folder(acct_name):
            print("No valid folder with that name.")
            return
        return self.get_folder(acct_name).get_value

    def print_folder_values(self):
        for acct in self.folders:
            print(acct.name + " Folder Value: $" + str(acct.get_value()))

    def get_total_value(self):
        total = 0
        for folder in self.folders:
            total += folder.funds
        return total


if __name__ == "__main__":
    a1 = PiggyAccount(1000000)
    a1.add_folder("House")
    a1.add_folder("Vacation")
    a1.transfer(2000, "default", "House")
    a1.transfer(10000, "default", "Vacation")
    a1.print_folder_values()
    a1.delete_folder("Vacation")
    a1.print_folder_values()
