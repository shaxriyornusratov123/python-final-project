import uuid
from datetime import datetime

class Transaction:
    def __init__(
        self,
        account_id: uuid.UUID,
        type: str,
        amount: int,
        status: str,
        datetime: datetime,
    ) -> None:
        self.id = uuid.uuid4()
        self.account_id=account_id
        self.type = type
        self.amount = amount
        self.status = status
        self.datetime = datetime

    def to_dict(self):
        return {
            "id": str(self.id),
            "account_id":str(self.id),
            "type":self.type,
            "amount":self.amount,
            "status":self.status,
            "created_at":self.datetime
        }

    def __str__(self) -> str:
        return f"{self.sender_name}-{self.receiver_name}-{self.amount}-{self.status}-{self.datetime}"


