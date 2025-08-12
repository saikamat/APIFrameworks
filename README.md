# FastAPI Books REST API

Simple CRUD API to practice REST basics.

FastAPI is a modern, high-performance Python web framework for building APIs.

## What is FastAPI?
Framework: Lets you build RESTful APIs quickly and easily in Python.
Based on: Starlette (for web parts) and Pydantic (for data validation).
Async support: Natively supports asynchronous code for high performance.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Verify
Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

### Example requests
List
`curl http://127.0.0.1:8000/books`

### Create
```bash
curl -X POST http://127.0.0.1:8000/books \
-H "Content-Type: application/json" \
-d '{"title":"Clean Code","author":"Robert C. Martin","year":2008,"pages":464}'
```

### Copy an ID from list output, then:
```bash
curl http://127.0.0.1:8000/books/<ID>
```
Example:-
`curl http://127.0.0.1:8000/books/b9a6b3e3-39f4-44a6-88da-56c98e429f4d`


```bash
curl -X PUT http://127.0.0.1:8000/books/<ID> \
-H "Content-Type: application/json" \
-d '{"title":"Clean Code (Updated)","author":"Robert C. Martin","year":2008,"pages":464}'
```
Example
```bash
curl -X PUT http://127.0.0.1:8000/books/962f7893-02f5-4f6b-8383-c8c326b24c1f -H "Content-Type: application/json" -d '{"title":"Clean Code (Updated)","author":"Robert C. Martin","year":2008,"pages":464}'
```


```bash
curl -X DELETE http://127.0.0.1:8000/books/<ID>
```