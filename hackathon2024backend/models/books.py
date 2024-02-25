from pydantic import BaseModel


class Books(BaseModel): 
  id: int
  comment: str
  bookTitle: str
