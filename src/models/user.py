from pydantic import BaseModel #BASE MODEL 
from typing import Optional #TYPE OF DATA

class User(BaseModel): #CREATE A CLASS INHERTITNG FROM BaseModel
    id: Optional[str]
    name: str
    email: str
    password: str