from fastapi_app.forms.user import UserCreateForm
from fastapi.templating import Jinja2Templates
from fastapi import status
from fastapi import responses
from fastapi import Request
from fastapi import Depends
from fastapi import APIRouter

from fastapi_app.service import create_user as service
import asyncio


templates = Jinja2Templates(directory="fastapi_app/templates")
router = APIRouter(include_in_schema=False)


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
async def register(request: Request):
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        print("in form")
        try:
            user = service.create_new_user(
                name=form.name, password=form.password)
            return responses.RedirectResponse(
                "/?msg=Successfully-Registered", status_code=status.HTTP_302_FOUND
            )  # default is post request, to use get request added status code 302"
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append("Duplicate username or email")
            return templates.TemplateResponse("register.html", form.__dict__)
    return templates.TemplateResponse("register.html", form.__dict__)
