# Data Validation, Exception Handling, Status Codes, Swagger Configuration, Python Request Objects
#from BookRequest import BookRequest
from pydantic import BaseModel, Field
from fastapi import FastAPI, Body, Path,Query, HTTPException
from typing import Optional
from starlette import status
from fastapi.responses import JSONResponse

app = FastAPI(docs_url="/documentation", redoc_url="/redoc")


class Book:
    id: Optional[int] 
    title: str
    author: str
    description: str
    rating: int
    published_date: int


    def __init__(self,id,title,author, description, rating, published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date

class BookRequest(BaseModel):
    id: Optional[int]= Field(title="id not needed")
    title: str=Field(min_length=3)
    author: str= Field(min_length=1)
    description: str=Field(min_length=1, max_length=100)
    rating: int=Field(gt=0,lt=5)
    published_date: int

    class Config:
        json_schema_extra= {
            "example":{
                "title": "A new book",
                "author": "coding",
                "description": "blaa",
                "rating": 5,
                "published_date":2005
            }
        }


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id== book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")
        
        

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_rating(book_rating:int=Query(g=0, lt=6)):
    books_to_return=[]
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
            return books_to_return

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_published_date(published_date:int):
    books_to_return=[]
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
            return books_to_return        

@app.post("/create-book" status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book= Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    # Return a response with information about the created book
    return JSONResponse(content={"message": "Book created successfully"})

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book:BookRequest):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i]= book
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)

async def delete_book(book_id:int=Path(gt=0)):
    book_changed= False
    for i in range(len(BOOKS)):
        if BOOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed= True
            break 
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")

    

def find_book_id(book:Book):
    book.id =BOOKS[-1].id +1 if len(BOOKS)>0 else 1


BOOKS=[ Book(1,'Computer Science Pro', 'codingwithrob', "very nice", 5,2000),
       Book(2,'Physics Pro 2', 'codingwithrob', "very bad", 1,2023),
       Book(3,'Bio Pro', 'codingwithrob', "not so good", 3,2022)
]