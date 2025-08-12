from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from uuid import UUID, uuid4

app = FastAPI(title="Books API", version="0.1.0")

# ----- Models -----
class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=100)
    year: Optional[int] = Field(None, ge=0, le=2100)
    pages: Optional[int] = Field(None, ge=1)

class Book(BookCreate):
    id: UUID

# ----- In-memory "DB" -----
DB: Dict[UUID, Book] = {}

# Seed a sample book so GET /books returns something
sample_id = uuid4()
DB[sample_id] = Book(id=sample_id, title="The Pragmatic Programmer", author="Andrew Hunt", year=1999, pages=352)

# ----- Routes -----
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/books", response_model=List[Book])
def list_books() -> List[Book]:
    return list(DB.values())

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: UUID) -> Book:
    book = DB.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=Book, status_code=201)
def create_book(payload: BookCreate) -> Book:
    new_id = uuid4()
    book = Book(id=new_id, **payload.model_dump())
    DB[new_id] = book
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: UUID, payload: BookCreate) -> Book:
    if book_id not in DB:
        raise HTTPException(status_code=404, detail="Book not found")
    updated = Book(id=book_id, **payload.model_dump())
    DB[book_id] = updated
    return updated

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: UUID):
    if DB.pop(book_id, None) is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return
