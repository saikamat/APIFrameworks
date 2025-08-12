import strawberry
from typing import Optional, List
from uuid import uuid4

# In-memory "DB"
class BookModel:
    def __init__(self, title: str, author: str, year: Optional[int] = None):
        self.id = str(uuid4())
        self.title = title
        self.author = author
        self.year = year

DB: List[BookModel] = [
    BookModel(title="The Pragmatic Programmer", author="Andrew Hunt", year=1999)
]

# GraphQL types
@strawberry.type
class Book:
    id: str
    title: str
    author: str
    year: Optional[int]

# Query resolvers
@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> List[Book]:
        # Map our models to GraphQL type
        return [Book(id=b.id, title=b.title, author=b.author, year=b.year) for b in DB]

    @strawberry.field
    def book(self, id: str) -> Optional[Book]:
        for b in DB:
            if b.id == id:
                return Book(id=b.id, title=b.title, author=b.author, year=b.year)
        return None

# Mutation resolvers
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str, year: Optional[int] = None) -> Book:
        new_b = BookModel(title=title, author=author, year=year)
        DB.append(new_b)
        return Book(id=new_b.id, title=new_b.title, author=new_b.author, year=new_b.year)

schema = strawberry.Schema(query=Query, mutation=Mutation)
