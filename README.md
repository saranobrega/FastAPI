# FastAPI
# Bank Note Authentication API

This FastAPI-based web API provides functionality to authenticate bank notes. It uses a trained machine learning model to predict whether a given set of measurements corresponds to a genuine or fake bank note.

## Getting Started

To run this API locally or deploy it to a server, follow these instructions:

### Prerequisites

- Python 3.x
- FastAPI
- Uvicorn
- BankNotes (Python package)
- Numpy
- Pickle
- Pandas

### API Endpoints
- /: The root endpoint that returns a welcome message.
- /{name}: An endpoint that accepts a parameter and returns a personalized message.
- /predict: POST endpoint to make predictions on bank notes. Send a JSON object with measurements (variance, skewness, curtosis, entropy) to get a prediction.
You can install the required dependencies using pip:

### Bash
pip install fastapi uvicorn numpy pickle pandas

### Running the API
To start the API, run the following command in your terminal:

uvicorn app:app --host 127.0.0.1 --port 8000 --reload

### Example Usage
To make a prediction, send a POST request to http://127.0.0.1:8000/predict with JSON data like this:

{
  "variance": 2.0,
  "skewness": 3.0,
  "curtosis": 1.0,
  "entropy": 0.5
}


# FastAPI Books API
This is a simple FastAPI project for managing books. It includes endpoints for creating, reading, updating, and deleting books.

## Features
- Get All Books: Retrieve a list of all books.
- Get a Specific Book: Retrieve information about a specific book using its ID.
- Get Books by Rating: Filter books by their rating.
- Get Books by Published Date: Filter books by their published date.
- Create a Book: Add a new book to the collection.
- Update a Book: Modify the details of an existing book.
- Delete a Book: Remove a book from the collection.

## Requirements
- Python 3.7+
- FastAPI
- Uvicorn (optional, for running the server)
  
## Installation
Clone the repository:

```bash
git clone https://github.com/your-username/fastapi-books-api.git
```



## Usage
Run the FastAPI server:
```bash
uvicorn main:app --reload
```


## Open the documentation:

Visit http://127.0.0.1:8000/documentation in your browser to access the Swagger documentation.

## Explore and test the API using the provided endpoints.

### API Endpoints
- GET /books: Get all books.
- GET /books/{book_id}: Get information about a specific book.
- GET /books/: Get books by rating.
- GET /books/publish/: Get books by published date.
- POST /create-book: Create a new book.
- PUT /books/update_book: Update a book.
- DELETE /books/{book_id}: Delete a book.

