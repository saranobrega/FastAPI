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

You can install the required dependencies using pip:

```bash
pip install fastapi uvicorn numpy pickle pandas

### Running the API
To start the API, run the following command in your terminal:

uvicorn app:app --host 127.0.0.1 --port 8000 --reload

### API Endpoints
- /: The root endpoint that returns a welcome message.
- /{name}: An endpoint that accepts a parameter and returns a personalized message.
- /predict: POST endpoint to make predictions on bank notes. Send a JSON object with measurements (variance, skewness, curtosis, entropy) to get a prediction.

### Example Usage
To make a prediction, send a POST request to http://127.0.0.1:8000/predict with JSON data like this:

{
  "variance": 2.0,
  "skewness": 3.0,
  "curtosis": 1.0,
  "entropy": 0.5
}
