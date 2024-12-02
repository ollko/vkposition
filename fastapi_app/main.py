from fastapi import FastAPI
from fastapi_app.web import vkgroup, user, create_user
app = FastAPI()

app.include_router(vkgroup.router)
app.include_router(user.router)
app.include_router(create_user.router)


@app.get("/")
def top():
    return "top here"


@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"
