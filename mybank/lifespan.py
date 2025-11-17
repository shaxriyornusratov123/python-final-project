import json 
import pathlib

from mybank.settings import DATA_DIR,accounts,transactions



def load_accounts():
    global accounts

    with open (DATA_DIR/"accounts.json",mode="r") as f:
        res=json.load(f)

        accounts["records"]=res["records"]
        accounts["count"]=len(accounts["records"])

        print("accounts.json fayldan muvoffaqiyatli o'qildi ")
        print(accounts)

        return True 
    

def save_accounts():
    global accounts

    with open (DATA_DIR/ "accounts_tmp.json", "w") as f:
        json.dump(accounts,f,indent=4)

    pathlib.Path.unlink(DATA_DIR/"accounts.json")
    pathlib.Path.rename(DATA_DIR/"accounts_tmp.json",DATA_DIR/"accounts.json")

    print("Akkountlar saqlandi! ")

    return True 


def load_transactions():
    global transactions

    with open (DATA_DIR/"transactions.json",mode="r") as f:
        res=json.load(f)

        transactions["records"]=res["records"]
        transactions["count"]=len(transactions["records"])

        print("transactions.json fayldan muvoffaqiyatli o'qildi ")
        # print(transactions)

        return True 
    

def save_transactions():
    global transactions

    with open (DATA_DIR/ "transactions_tmp.json", "w") as f:
        json.dump(transactions,f,indent=4)

    pathlib.Path.unlink(DATA_DIR/"transactions.json")
    pathlib.Path.rename(DATA_DIR/"transactions_tmp.json",DATA_DIR/"transactions.json")

    print("Tranzaksiyalar saqlandi! ")

    return True 
