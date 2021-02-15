from PiggyAccount import PiggyAccount


def login():
    username = input("Enter username: ")
    init_funds = input("Enter initial funds in account: ")
    return username, init_funds


if __name__ == "__main__":
    u, init = login()
    account1 = PiggyAccount(u, init)
    account1.add_folder("House", 100000)
    account1.add_folder("Macbook", 2500)
    print(account1.print_folder_values())

    print("\nNumber of months to house value, given a deposit of $2000 per month: ")
    print(str(account1.get_folder("House").calculate_time_to_completion(2000, 1)) + " months.")

    print("\nNumber of $250 deposits to get a Macbook in 6 months: ")
    print(str(account1.get_folder("Macbook").calculate_deposit_freq(6, 250)) + " deposits per month.")

    print("\nAmount to deposit 4 times a month to get a house in 5 years: ")
    print("$" + str(account1.get_folder("House").calculate_deposit_amt(60, 4)) + " per deposit.")

