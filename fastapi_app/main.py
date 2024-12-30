import os
from fastapi import FastAPI, HTTPException, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi_app.web import (
    position,
    tables,
    vkgroup,
    query,
    user,
    create_user,
)
templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "templates")
)
app = FastAPI()

app.include_router(tables.router)
app.include_router(vkgroup.router)
app.include_router(query.router)
app.include_router(user.router)
app.include_router(create_user.router)
app.include_router(position.router)


@app.get("/")
def top(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/echo/{thing}")
# def echo(thing):
#     return f"echoing {thing}"
