from pydantic import BaseModel


class UserContract(BaseModel):
  name: str
  email: str
  