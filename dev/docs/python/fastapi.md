# FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to be easy to use and highly efficient, making it a popular choice for developers looking to create RESTful APIs.

## Features

FastAPI offers several powerful features:

- **Fast Development**: Write less code and quickly build APIs.
- **High Performance**: Built on top of Starlette and Pydantic, it delivers high performance.
- **Type Safety**: Leverages Python type hints for automatic validation and documentation.
- **Interactive Documentation**: Automatically generates Swagger UI and ReDoc documentation.

## Getting Started

To start using FastAPI, you need to install it. Use the following command:

```bash
pip install fastapi[all]
```

### Example Code

Below is a simple example of a FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

Save this code in a file (e.g., `main.py`) and run it using Uvicorn:

```bash
uvicorn main:app --reload
```

Once the server is running, you can access the API documentation at:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs){:target="_blank"}
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc){:target="_blank"}

## Key Concepts

### Path Parameters

FastAPI allows you to define path parameters easily. For example:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

### Query Parameters

You can also define optional query parameters:

```python
@app.get("/search/")
def search_items(query: str = None):
    return {"query": query}
```

### Request Body

FastAPI uses Pydantic models for request validation:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
```

### Dependency Injection

FastAPI supports dependency injection for reusable logic:

```python
from fastapi import Depends

def common_dependency():
    return {"key": "value"}

@app.get("/dependencies/")
def read_dependencies(dep=Depends(common_dependency)):
    return {"dependency": dep}
```

## Resources

Here are some useful resources to learn more about FastAPI:

- [FastAPI Documentation](https://fastapi.tiangolo.com/){:target="_blank"}
- [GitHub Repository](https://github.com/tiangolo/fastapi){:target="_blank"}
- [Uvicorn Documentation](https://www.uvicorn.org/){:target="_blank"}

## Conclusion

FastAPI is an excellent choice for building APIs quickly and efficiently. Its modern design, type safety, and built-in documentation make it a favorite among Python developers. Start building your next API with FastAPI today!
