from pydantic import BaseModel


class EntityContract(BaseModel):
  id: str
