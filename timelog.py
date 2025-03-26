from fastapi import FastAPI, Request
import time

app = FastAPI()

# Middleware for logging and execution time
@app.middleware("http")
async def log_and_time_request(request: Request, call_next):
    start_time = time.time()
    print(f"Incoming request: {request.method} {request.url}")

    response = await call_next(request)  # Process the request
    execution_time = time.time() - start_time

    print(f"Request completed in {execution_time:.4f} seconds")
    return response

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}
