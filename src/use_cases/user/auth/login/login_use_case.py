from repositories.user_repository import UsersRepository
from fastapi import FastAPI, Request, Response
from use_cases.user.auth.login.login_dto import LoginDTO
from entities.user import User
import datetime
import jwt
import os

class LoginUseCase:
    user_repository: UsersRepository

    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):
        check_exists = self.user_repository.find_by_email(email=login_dto.email)

        if (len(check_exists) == 0):
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar um usuário com o email fornecido"}

        user = check_exists[0]

        if (not user.check_password_matches(login_dto.password)):
            response.status_code = 400
            return {"status": "error", "message": "Senha incorreta, tente novamente mais tarde."}
        
        expiration = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=90)

        token = jwt.encode({"email": user.email, "id": str(user.id)}, os.getenv("USER_JWT_SECRET"))
        
        response.set_cookie(
            key="user_auth_token",
            value=f"Bearer {token}",
            httponly=True,
            expires=expiration,
            secure=False,
            samesite="None"  
        )


        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}