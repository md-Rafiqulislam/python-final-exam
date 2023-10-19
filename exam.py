

###################################### import functions
import random

###################################### variables
ac_sv = 'saving account'
ac_cr = 'current account'
wrong_input = '\nyou have enter a wrong input\n'
end_note = '\nThanks for visiting the bank\n'
cr_account = None


####################################### all extra def

# welcome note
def welcome():
    print('\n--------------------------------------------------------------------------------------------------------')
    print('                                           WELCOME TO BANK                                              ')
    print('--------------------------------------------------------------------------------------------------------\n')

# first page
def first_page():
    print('\nHere is your option:\n\t1. Enter 1 for admin\n\t2. Enter 2 for user\n\t3. Enter 3 for quit\n')
    option = (input('Enter your choice: '))
    print()
    return option

# admin information
def admin_information():
    admin_account = Account.all_accounts[0]
    print('all the information about admin:')
    print(f'\tname              : {admin_account.name}')
    print(f'\taccount type      : {admin_account.account_type}')
    print(f'\taddress           : {admin_account.address}')
    print(f'\temail             : {admin_account.email}')
    print(f'\taccount number    : {admin_account.account_number}')


# input name and email
def input_ne():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    return name, email

# input address
def input_ad():
    address = input('Enter your address: ')
    return address

# admin options
def admin_option():
    print('Here is all the options for admin:')
    print("\t1. Create account")
    print("\t2. see all the accounts")
    print("\t3. see all the loan money")
    print("\t4. see all available money")
    print("\t5. delete any account")
    print("\t6. see admin information")
    print("\t7. go back")
    print("\t8. exit\n")

    option = input('Enter your choice: ')
    print()
    return option

# user option
def user_option():
    print('Here is all the options for user:')
    print("\t1  : Create account")
    print("\t2  : see balance")
    print("\t3  : see loan money")
    print("\t4  : see all transaction")
    print("\t5  : transfer money")
    print("\t6  : see user information")
    print("\t7  : go back")
    print("\t8  : exit")
    print("\t9  : take loan")
    print("\t10 : deposit money")
    print("\t11 : withdraw money\n")

    option = input('Enter your choice: ')
    print()
    return option



# show account type
def show_account_type():
    print('\nHere is two kinds of account:')
    print(f'\t1. {ac_sv}')
    print(f'\t2. {ac_cr}')
    print()
    option = input('Enter your option: ')
    
    return option

# show name, email, address, account type
def s_info(name, email, address, ac_t):
    print('\nhere you entered:')
    print(f'\tname          : {name}')
    print(f'\temail         : {email}')
    print(f'\taddress       : {address}')
    print(f'\taccount type  : {ac_t}\n')



# account class
class Account:
    all_accounts = []
    all_loan_money = 0
    all_bank_balance = 0

    def __init__(self, name, email, address, account_type) -> None:
        # self.all_accounts = []

        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type

        # self.all_accounts.append(self)
        Account.all_accounts.append(self)

        self.balance = 0
        self.transactions_history = []
        self.account_number = self.generate_account_number()


    
    # account number auto generate
    def generate_account_number(self):
        return f"{self.name}-{random.randint(1000, 9999)}"


    # money deposit
    def deposit_money(self, amount):
        if amount > 0 and isinstance(amount, int):
            self.balance += amount
            Account.all_bank_balance += amount
            self.transactions_history.append(f'Deposit: {amount}')
            print(f'\nyou have deposit {amount}')
        else:
            print(wrong_input)


    # withdraw money
    def withdraw_money(self, amount):
        if amount < 0 and amount > self.balance and isinstance(amount, int):
            if Account.all_bank_balance >= amount:
                self.balance -= amount
                Account.all_bank_balance -= amount
                self.transactions_history.append(f'Withdraw: {amount}')
                print(f'\nyou have withdraw {amount}')
            else:
                print('The bank is bankrupt')
        else:
            print('Withdrawal amount exceeded')



    # see balance
    def see_balance(self):
        return self.balance
    



    # print account class for checking
    def __repr__(self) -> str:
        print(f'name: {self.name}, email: {self.email}, address: {self.address}, account type: {self.account_type} the balance: {self.balance}, account number: {self.account_number}')
        return ''
    




# user class
class User(Account):
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address, account_type)

        self.loan_taken = 0
        self.loan_limit = 2
        self.loan_money = 0




    # show information of a user
    def account_info(self):
        print('All the information of your account:')
        print(f"\t name                 : {self.name}")
        print(f'\t email                : {self.email}')
        print(f'\t address              : {self.address}')
        print(f'\t balance              : {self.balance}')
        print(f'\t account type         : {self.account_type}')
        print(f'\t account number       : {self.account_number}')
        print(f'\t total loan money     : {self.loan_money}')
        print(f'\t total loan taken     : {self.loan_taken} times')
        print(f'\t total loan available : {self.loan_limit - self.loan_taken} times')




    # loan take
    def take_loan(self, amount):
        # if self.loan_permit == 1:
        if self.loan_taken < self.loan_limit:
            self.balance += amount
            self.loan_money += amount
            self.loan_taken += 1
            Account.all_loan_money += amount
            Account.all_bank_balance -= amount
            self.transactions_history.append(f'Loan: {amount}')
        else:
            print('you have no loan limit.')
        # else:
        #     print('you can not take loan.')



    # see loan money
    def see_loan_mony(self):
        return self.loan_money



    # see all the transaction
    def see_transaction_history(self):
        print('All the transactions is below:')
        for i, information in enumerate(self.transactions_history):
            print(f"\t{i + 1}. {information}")
        return ''
        

    # print user class for checking
    def __repr__(self) -> str:
        print(f'name: {self.name}, email: {self.email}, address: {self.address}, account type: {self.account_type} the balance: {self.balance}, account number: {self.account_number}')
        return ''
    


# admin class
class Admin(User):
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address, account_type)



    # create new account
    def create_account(self, name, email, address, account_type):
        self.account_name = name
        self.account_name = User(name, email, address, account_type)

        # self.all_accounts.append(self.account_name)
        Account.all_accounts.append(self.account_name)
        return self.account_name
    



    # delete user account
    def delete_account(self, account):
        if account in Account.all_accounts:
            Account.all_accounts.remove(account)
            print('your given account is deleted...')
        else:
            print('you have entered wrong account...')
    


    # see all the account in bank
    def see_all_account(self):
        print('All the available accounts in bank is below:')
        for i, account in enumerate(Account.all_accounts):
            print('\t', i + 1, '-', account)


    # see the length of all accounts
    def len_of_all_account(self):
        return len(Account.all_accounts)


    # see all the loan balance
    def see_all_loan_balance(self):
        return Account.all_loan_money
    
    

    # see all the available balance
    def see_all_balance(self):
        return Account.all_bank_balance


# admin
admin = Admin('admin', 'admin@admin.com', 'admin', 'admin')

# main function
welcome()

while True:

    # admin user option to chose
    a_u = first_page()

    # admin login
    if a_u == '1':
        admin_name, admin_email = input_ne()
        if admin_name == admin.name and admin_email == admin.email:
            print('\nwelcome admin to your bank...\n')

            run_inner_loop = True
            while run_inner_loop:
                a_o = admin_option()

                # Create account for user
                if a_o == '1':
                    user_name, user_email = input_ne()
                    user_address = input_ad()
                    ac_t = show_account_type()

                    # saving account
                    if ac_t == '1':
                        s_info(user_name, user_email, user_address, ac_sv)
                        user_account = (user_name, user_email, user_address, ac_sv)
                        if user_account not in Account.all_accounts:
                            userAccount = admin.create_account(user_name, user_email, user_address, ac_sv)
                            print('\naccount created successfully.\n')
                        else:
                            print('\nthis account is already in the list.\n')

                    # current account   
                    elif ac_t == '2':
                        s_info(user_name, user_email, user_address, ac_cr)
                        user_account = admin.create_account(user_name, user_email, user_address, ac_cr)
                        if user_account not in Account.all_accounts:
                            userAccount = admin.create_account(user_name, user_email, user_address, ac_sv)
                            print('\naccount created successfully.\n')
                        else:
                            print('\nthis account is already in the list.\n')

                    # wrong input
                    else:
                        print(wrong_input)

                # see all the accounts
                elif a_o == '2':
                    print()
                    admin.see_all_account()
                    print()


                # see all the loan money
                elif a_o == '3':
                    print()
                    print(admin.see_all_loan_balance())
                    print()
                    


                # see all the available money
                elif a_o == '4':
                    print()
                    print(admin.see_all_balance())
                    print()


                # delete any account
                elif a_o == '5':
                    accountType = ''
                    print()
                    user_name, user_email = input_ne()
                    user_address = input_ad()
                    print()
                    acT = show_account_type()
                    if acT == '1':
                        accountType = ac_sv
                    elif acT == '2':
                        accountType = ac_cr
                    account = (user_name, user_email, user_address, accountType)
                    admin.delete_account(account)
 

                # see about admin
                elif a_o == '6':
                    admin_information()
                    print()

                # go back from admin
                elif a_o == '7':
                    run_inner_loop = False

                # exit from the bank
                elif a_o == '8':
                    print(end_note)
                    exit()

                # for wrong input
                else:
                    print(wrong_input)
        else:
            print('\nyour name and email was not match...\n')
    
    # user options
    elif a_u == '2':
        print()
        u_o = user_option()
        run_inner_user_loop = True
        while run_inner_user_loop:

            # create account
            if u_o == '1':
                user_name, user_email = input_ne()
                user_address = input_ad()
                ac_t = show_account_type()

                # saving account
                if ac_t == '1':
                    s_info(user_name, user_email, user_address, ac_sv)
                    user_account = (user_name, user_email, user_address, ac_sv)
                    if user_account not in Account.all_accounts:
                        userAccount = admin.create_account(user_name, user_email, user_address, ac_sv)
                        cr_account = userAccount
                        print('\naccount created successfully.\n')
                        break
                    else:
                        print('\nthis account is already in the list.\n')

                # current account   
                elif ac_t == '2':
                    s_info(user_name, user_email, user_address, ac_cr)
                    user_account = admin.create_account(user_name, user_email, user_address, ac_cr)
                    if user_account not in Account.all_accounts:
                        userAccount = admin.create_account(user_name, user_email, user_address, ac_sv)
                        cr_account = userAccount
                        print('\naccount created successfully.\n')
                        break
                    else:
                        print('\nthis account is already in the list.\n')
                        break

                # wrong input
                else:
                    print(wrong_input)
                    break


            # see balance
            elif u_o == '2':
                if len(Account.all_accounts) <= 1:
                    print('\ncreate account first\n')
                    break
                else:
                    print()
                    print(cr_account.see_balance())
                    print()
                    break


            # see loan money
            elif u_o == '3':
                if len(Account.all_accounts) <= 1:
                    print('\ncreate account first\n')
                    break
                else:
                    print()
                    print(cr_account.see_loan_mony())
                    print()
                    break


            # see all transaction
            elif u_o == '4':
                if len(Account.all_accounts) <= 1:
                    print('\ncreate account first\n')
                    break
                else:
                    print()
                    print(cr_account.see_transaction_history())
                    print()
                    break


            # transfer money
            elif u_o == '5':
                pass


            # see user information
            elif u_o == '6':
                if len(Account.all_accounts) <= 1:
                    print('\ncreate account first\n')
                    break
                else:
                    print()
                    print(cr_account.account_info())
                    print()
                    break


            # go back
            elif u_o == '7':
                run_inner_user_loop = False

            
            # exit
            elif u_o == '8':
                print(end_note)
                exit()

            
            elif u_o == '9':
                if len(Account.all_accounts) <= 1:
                    print('\ncreate account first\n')
                    break
                else:
                    amount = int(input('Enter your loan amount: '))
                    cr_account.take_loan(amount)
                    break
            
            # deposit money
            elif u_o == '10':
                if len(Account.all_accounts) <= 1:
                    print('\ncreate account first\n')
                    break
                else:
                    amount = int(input('Enter your deposit amount: '))
                    cr_account.deposit_money(amount)
                    break


            # withdraw money
            elif u_o == '11':
                if len(Account.all_accounts) <= 1:
                    print('\ncreate account first\n')
                    break
                else:
                    amount = int(input('Enter your withdraw amount: '))
                    cr_account.withdraw_money(amount)
                    break



            # wrong_input
            else:
                print(wrong_input)


    # quit the programme
    elif a_u == '3':
        print(end_note)
        exit()


    # for wrong input
    else:
        print(wrong_input)