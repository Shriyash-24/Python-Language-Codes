"""
Take user input to show balance, withdraw or deposit money in the account. And more.
"""
import random
balance = 0.0
kyc_documents = {}
rewards_received = 0.0

def check_balance():
    print("Checking Balance...")
    print("Your balance is: $", balance)

def deposit(amount):
    print("Processing..")
    global balance
    if amount > 0:
        balance = balance + amount
        print("Transaction Successful!")
        print("Your balance is: $", balance)
    else:
        print("Can't deposit the amount.")

def withdraw(amount):
    print("Processing..")
    global balance
    if amount > balance:
        print("Can't withdraw the amount. Insufficient balance. ")
        print("Your balance is: $", balance)
    elif amount <= 0:
        print("Can't withdraw negative or zero amount.")
    else:
        balance = balance - amount
        print("Transaction Successful!")
        print("Your balance is: $", balance)

def update_kyc(kyc_dict):
    global kyc_documents
    kyc_documents.update(kyc_dict)

def check_kyc():
    if len(kyc_documents) == 0:
        print("Can't find any KYC documents.")
    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")

def is_lucky():
    num = [0,0,0,0,0,0,0,1]
    lucky = random.choice(num)
    if lucky:
        reward()
    else:
        print("Reward:- Better Luck Next Time!")

def reward():
    global balance
    global rewards_received
    num = [1,2,3,4,5]
    reward_amount = random.choice(num)
    print(f"Congratulations! You received ${reward_amount} for using our bank.")
    rewards_received = rewards_received + reward_amount
    balance = balance + reward_amount
    print("The reward is successfully added in your account. Please continue using our services.")

def rewards_page():
    print("Our bank rewards you for using our services.")
    print(f"You received ${rewards_received} in rewards for using our bank.")
    print("Thank you.")

if __name__ == "__main__":
    print("============")
    print("Welcome To ABC Bank")
    print("============")
    print()
    while True:
        print("Options: ")
        print("1. Check Balance")
        print("2. Deposit An Amount")
        print("3. Withdraw An Amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Check Rewards")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            print("We provide rewards if you deposit money with us, try your luck.")
            amt = float(input("Enter the amount to deposit: "))
            deposit(amt)
            is_lucky()
        elif choice == '3':
            amt = float(input("Enter the amount to withdraw: "))
            withdraw(amt)
        elif choice == '4':
            check_kyc()
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to add: "))
            for i in range(n_documents):
                key = input("Enter the document type: ")
                value = input("Enter the document verification number: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print("KYC Successfully completed.")
        elif choice == '6':
            rewards_page()
        elif choice == '7':
            break
        else:
            print("Please enter a valid choice.")
print()
print("Thank you for banking with us.")