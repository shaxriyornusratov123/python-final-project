import time 

from mybank.lifespan import load_accounts,load_transactions,save_accounts,save_transactions
from mybank.settings import current_account,accounts,transactions
from mybank.account import login, search_account,view_all_accounts, create_account

menu_text: str = """=== Bank System Menu ===
0. Log In 
1. Create New Account
2. View All Accounts
3. Search Account
4. Deposit
5. Withdraw
6. View Transactions
7. Log Out
8. Delete Account
-1. Exit
========================"""




def main_menu() -> None:
    load_accounts()
    load_transactions()

    while True:        
        print(menu_text)
        choice: int = int(input("Enter your choice: ")) 

        if choice==0:
            login()
        elif choice == 1:
            global current_account
            current_account = create_account()
            
            print("Akkaunt muvaffaqiyatli yaratildi.")
        elif choice == 2:
            view_all_accounts()
        elif choice == 3:
            search_account()
        elif choice == 4:
            while True:
                amnt = int(input("Kiritmoqchi bo'lgan summangizni kiriting: "))
                if amnt <= 0:
                    print("Manfiy sonni kirita olmaysiz!")
                    continue
                break
            current_account.deposit(amount=amnt)
        elif choice == 5:
            while True:
                amnt=int(input("Yechmoqchi  bo'lgan summangizni kiriting: "))
                if amnt<=0:
                    print("Siz manfiy son kirita olmaysiz!  ")
                    continue
                break 
            current_account.withdraw(amount=amnt)
        elif choice == 6:
            current_account.view_transactions()

        elif choice == 7:
            current_account.logout()
        elif choice == 8:
            is_confirmed=input("Rostdan akkountingizni o'chimoqchimisiz? (Ha(1)/Yo'q(0)): ")
            if is_confirmed!="1":
                continue
            current_account.delete_account()
        else:
            save_accounts()
            save_transactions()
            print("Exit")
            break
