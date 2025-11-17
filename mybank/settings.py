import pathlib 

accounts: dict = {
    "count":0,
    "records":[]
}
transactions: dict = {
    "count": 0,
    "records":[]
}
DATA_DIR=pathlib.Path.cwd()/ "data"
current_account=None 