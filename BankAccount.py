#Method one with If-else statements
def main():  
    F_NAME = ''
    L_NAME = ''
    PHONE = ''
    BALANCE = 0.0

    while True:
        print()
        print('''--- Jovan Orient Vocational Enterprise Bank ---
    1. Create an account
    2. Deposit money
    3. Withdraw money
    4. Display account
    5. Exit
    ''') 
        choice = int(input("Enter a choice 1-4: "))

        if choice == 1:
            F_NAME = input("\nEnter your first name: ")
            L_NAME = input("Enter your last name: ")
            PHONE = input("Enter your phone number: ")
            BALANCE= 0.00

            print("\nAccount created.")
            print(f"{'Welcome to Jovan Orient Vocational Enterprise Bank':^50}\n")
            print(f"Account name: {F_NAME} {L_NAME}" +
                f"\nPhone number: {PHONE}\nNew Account Balance: {BALANCE}")

        elif choice == 2:
            depo = float(input("Enter the amount to deposit: "))
            BALANCE += depo
            print(f"\nAccount Balance now: {BALANCE:.2f}")

        elif choice == 3:
            draw = float(input("Enter amount to withdraw: "))
            BALANCE -= draw
            print(f"\nWithdrawn: {draw}\nAccount Balance: {BALANCE}")

        elif choice == 4:
            print("\n----------------------------")
            print(f"Account name: {F_NAME} {L_NAME}" +
                f"\nPhone number: {PHONE}\nAccount Balance: {BALANCE}")
            print("----------------------------")

        elif choice == 5:
            print("\nThank you for using Jovan Orient Vocational Enterprise Bank.Good bye")
            break

        else:
            print("\nError. Choice not in options.")
    
main()

"---------------------------------------------------------------------------------------"

#Method two with functions
def print_menu():
    print()
    print('''
            --- Jovan Orient Vocational Enterprise Bank ---
1. Create an account
2. Deposit money
3. Withdraw money
4. Display account
5. Exit
''')
def create_account():
    F_NAME = input("\nEnter your first name: ")
    L_NAME = input("Enter your last name: ")
    PHONE = input("Enter your phone number: ")
    BALANCE= 0.00
    return F_NAME, L_NAME, PHONE, BALANCE

def deposit():
    deposit = float(input("Enter the amount to deposit: "))
    return deposit

def withdraw(BALANCE):
    draw = float(input("Enter amount to withdraw: "))
    current = BALANCE - draw
    return  draw, current

def display(first, last, phone, balance):
    print("\n----------------------------")
    print(f"Account name: {first} {last}" +
        f"\nPhone number: {phone}\nAccount Balance: {balance}")
    print("----------------------------")

def main():  
    F_NAME = ''
    L_NAME = ''
    PHONE = ''
    BALANCE = 0.0

    while True:
        print_menu()

        choice = int(input("Enter a choice 1-4: "))
        if choice == 1:
            F_NAME, L_NAME, PHONE, BALANCE = create_account()

            print("\nAccount created.")
            print(f"{'Welcome to Jovan Orient Vocational Enterprise Bank':^50}\n")
            print(f"Account name: {F_NAME} {L_NAME}" +
                f"\nPhone number: {PHONE}\nNew Account Balance: {BALANCE}")

        elif choice == 2:
            BALANCE += deposit()
            print(f"\nAccount Balance now: {BALANCE:.2f}")

        elif choice == 3:
            draw, BALANCE = withdraw(BALANCE)
            print(f"\nWithdrawn: {draw}\nAccount Balance: {BALANCE}")

        elif choice == 4:
            display(F_NAME, L_NAME, PHONE, BALANCE)

        elif choice == 5:
            print("\nThank you for using Jovan Orient Vocational Enterprise Bank.Good bye")
            break

        else:
            print("\nError. Choice not in options.")


if __name__ == '__main__':
    main()
