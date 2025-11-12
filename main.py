import uuid
from datetime import datetime,timezone


class Transaction:
    def __init__(self,id: uuid.UUID,
        type:str,
        sender_name:str,
        receiver_name:str,
        amount:int,
        status:str,
        datetime: datetime
        )->None:
        self.id=id
        self.type=type
        self.sender_name=sender_name
        self.receiver_name=receiver_name
        self.amount=amount
        self.stutus=status
        self.datetime=datetime

    def __str__(self):
        return f"Transaction<id={str(self.id)}>"

class BankAccount:



    def __init__(self,
                id:uuid.UUID, 
                name:str, 
                balance: int,
                account_number:int,
                created_at:datetime)->None:
        self.id=id
        self.name=name
        self.balance=balance
        self.account_number=account_number
        self.created_at=created_at


    def __str__(self):
        return f"name:{self.name}"
    

    # def deposit(self,amount:int):
    #     self.balance+=amount 
    
    
        

    def withdraw(self,amount):
        pass

    def view_transactions():
        pass

    def delete_account():
        pass



accounts: list[Transaction]=[]
menu_text:str="""
=== Bank System Menu ===
1. Create New Account
2. View All Accounts
3. Search Account
4. Deposit
5. Withdraw
6. View Transactions
7. Delete Account
8. Exit
========================
"""
current_account=None

#======================= core logic

def create_account():
    print("siz yangi akkaunt ochmoqchchisiz. quyidagi malumotlarni kiriting: ")

    name: str=input("F.I.SH: ")
    account_number:str=input("akkaunt raqamingiz: ")
    balance: int= int(input("mavjud blansingiz: "))
    

    id: uuid.UUID=uuid.uuid4()
    created_at: datetime=datetime.now(timezone.utc)

    new_account: BankAccount=BankAccount(
        id=id,
        name=name,
        account_number=account_number,
        balance=balance,
        created_at=created_at

    )
    return new_account

def view_all_accounts():
    print("Barcha akkauntlar ro'yxati:")
    for i, account in enumerate(accounts):
        print(f"{i+1}. {account.name} - {account.balance}")
    
    is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
    if is_end == '\n':
        return None

def search_account():
    searched_name = input("Qidirilayotgan account egasini kiriting: ")
    
    print("===== Natijalar =====")
    for i, account in enumerate(accounts):
        if searched_name.lower() in account.name.lower():
            print(f"{i+1}. {str(account.id)} - {account.name} - {account.account_number}")

    is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
    if is_end == '\n':
        return None

# def deposit():
#     pass

# def withdraw():
#     pass

# def view_transactions():
#     pass

# def delete_account():
#     pass






def main_menu() -> None:
    while True:        
        print(menu_text)
        choice: int = int(input("Enter your choice: "))
        
        if choice == 1:
            global current_account
            current_account = create_account()
            
            print("Akkaunt muvaffaqiyatli yaratildi.")
        elif choice == 2:
            view_all_accounts()
        elif choice == 3:
            search_account()
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        else:
            print("Exit")
            break


if __name__ == "__main__":
    main_menu()
