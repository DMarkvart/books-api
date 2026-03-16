from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    year: int

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: int