from pydantic import BaseModel, ConfigDict
from typing import List


class Credentials(BaseModel):
    model_config = ConfigDict(strict=True)
    login: str
    pincode: int


class UserData(BaseModel):
    model_config = ConfigDict(strict=True)
    data: List[Credentials]


usr = UserData(
    data=[
        Credentials(login="Vasya", pincode=123),
        Credentials(login="Prtya", pincode=456),
    ]
)


jsondict = {
    "data": [{"login": "Vasya", "pincode": 123}, {"login": "Prtya", "pincode": 456}]
}

usr2 = UserData(**jsondict)
