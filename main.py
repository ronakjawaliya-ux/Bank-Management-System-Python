#  Project--02 || Bank Management System
#  using Python

import json


def save_accounts():
    with open('accounts.json', 'w') as f:
        json.dump(accounts, f, indent=4)

def load_accounts():
    try:
        with open('accounts.json', 'r') as f:
           return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

accounts = load_accounts()


while True:
    print('\n===== Bank Management System =====\n')
    print('1. Create Account')
    print('2. View All Accounts')
    print('3. Search Account')
    print('4. Deposit Money')
    print('5. Withdraw Money')
    print('6. Transfer Money')
    print('7. Check Balance')
    print('8. Delete Account')
    print('9. Total Accounts')
    print('10. Exit')

    choice = input('Enter your choice: ')

    # 1. CREATE-ACCOUNT :
    if choice == '1':
        account_id = int(input('Enter account ID: '))
        name =input('Enter your name: ')
        age = input('Enter your age: ')
        phone_no = input('Enter your phone number: ')
        initial_balance = input('Enter your initial balance: ')


        account = {
                  'id': account_id,
                  'name': name,
                  'age': age,
                  'phone_no': phone_no,
                  'initial_balance': initial_balance
        }


        found = False

        for existing_account in accounts:
            if existing_account['id'] == account_id:
                  found = True
                  print(f'Account {existing_account["name"]} already exists')
                  break

        if not found:
            accounts.append(account)
            print('Account created successfully')
            save_accounts()

    # 2. VIEW-ALL-ACCOUNTS :
    elif choice == '2':
        if len(accounts) == 0:
            print('No accounts found')
        else:
            print('\nAccounts List:\n')
            for account in accounts:
                print("------------------------------------")
                print("Account ID:",account ["id"])
                print("Name:", account["name"])
                print("Age:", account["age"])
                print("Phone Number:", account["phone_no"])
                print("Initial Balance:", account["initial_balance"])



    # 3. SEARCH-ACCOUNTS :
    elif choice == '3':
        search_id = int(input('Enter account ID search: '))

        found = False

        for account in accounts:
            if account['id'] == search_id:
                print('\nAccount Found')
                print('Account ID:', account['id'])
                print('Name:', account['name'])
                print('Age:', account['age'])
                print('Phone Number:', account['phone_no'])
                print('Initial Balance:', account['initial_balance'])
                found = True
                break

        if not found:
            print('\nAccount not found')


    # 4.  DEPOSIT-MONEY :
    elif choice == '4':

