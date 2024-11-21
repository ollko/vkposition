from fastapi import FastAPI
from fastapi_app.web import vkgroup
app = FastAPI()

app.include_router(vkgroup.router)


@app.get("/")
def top():
    return "top here"


@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"
