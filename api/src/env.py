import os
from dotenv import load_dotenv


def required(key: str) -> str:
  if key not in os.environ:
    raise ValueError(f'{key} is required')
  return os.environ[key]


load_dotenv()

class Mongo:
  URI = required('MONGO_URI')
  DB_NAME = required('MONGO_DB')