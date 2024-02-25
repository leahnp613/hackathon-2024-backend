from pydantic import BaseModel


class Music(BaseModel): 
  message: str
  href: str
  limit: int
  next: str
  offset: int
  previous: str
  total: int
  items: list
