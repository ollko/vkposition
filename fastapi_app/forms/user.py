from fastapi import Request


class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: list = []
        self.name: str | None = None
        self.password: str | None = None

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get("name")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.name or not len(self.name) > 3:
            self.errors.append("Имя должно быть > 3 символов")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("Пароль должен быть более 4 символов")
        if not self.errors:
            return True
        return False
