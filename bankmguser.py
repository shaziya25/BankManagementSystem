from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_no, balance):
        self.__account_no = account_no
        self.__balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance

    def masked_accountno(self):
        return "*****" + str(self.__account_no)[-4:]

    def _update_balance(self, amount):   # protected
        self.__balance += amount

#class1
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit can't be zero or negative!")
            return
        self._update_balance(amount)
        print(f"Deposited {amount} in Savings Account")

    def withdraw(self, amount):
        if amount > self.get_balance():
            print("Insufficient balance")
            return
        self._update_balance(-amount)
        print(f"Withdrawn {amount} from Savings Account")

#class2
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self._update_balance(amount)
        print(f"Deposited {amount} in Current Account")

    def withdraw(self, amount):
        if amount > self.get_balance() + 10000:  # overdraft limit
            print("Overdraft limit exceeded")
            return
        self._update_balance(-amount)
        print(f"Withdrew {amount} from Current Account")


# ----userinput--
def main():
    print("Welcome to bank management system")

    acc_type =input("Enter your account type:")
    acc_no=int(input("Enter your account no details:"))
    acc_balance=float(input("enter your balance amount:"))


    if acc_type == "savings":
        account= SavingsAccount(acc_no,acc_balance)
    elif acc_type == "current":
        account= CurrentAccount(acc_no,acc_balance)

    else:
     print("Invalid account type!!")   
     return


    print(f"\nAccount created Successfully! Account No :{account.masked_accountno()}") 

    while True:
        print("\n--- MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Check Account Number")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)

        elif choice == "2":
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)

        elif choice == "3":
            print("Current Balance:", account.get_balance())

        elif choice == "4":
          print("Your Account No (masked):", account.masked_accountno())

        elif choice == "5":
         print("Thank you for using our service!")
         break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
     main()