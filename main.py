from bank_account import BankAccount

def main():
    a1 = BankAccount("Alex", 1000)
    print(a1.balance)
    print(a1._balance)
    print(a1.get_balance())

    a1.balance = a1.balance + 1000
    print(a1.balance)
    del a1.balance

main()
