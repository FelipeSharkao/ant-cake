from bson.objectid import ObjectId
from .contracts import EntityContract, UserContract


class UserDocument(EntityContract, UserContract):
  _password: str