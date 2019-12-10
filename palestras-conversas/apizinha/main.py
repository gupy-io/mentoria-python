from fastapi import FastAPI
from todos import router as todo_router


app = FastAPI()


@app.get("/")
def home():
    """
    View Home
    Return {"classic": "A lua cheia ..."}
    """


app.include_router(todo_router, prefix="/todo", tags=["TODO"])
