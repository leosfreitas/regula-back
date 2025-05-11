from fastapi import Request
import jwt 
import os 

def get_user_id(request: Request) -> str:
    """
    Get the user ID from the request cookies.
    """
    token = request.cookies.get("user_auth_token")
    payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
    user_id = payload.get("id")
    return user_id

def get_user_email(request: Request) -> str: 
    """
    Get the user email from the request cookies.
    """
    token = request.cookies.get("user_auth_token")
    payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
    user_email = payload.get("email")
    return user_email

def get_user_cpf(request: Request) -> str:
    """
    Get the user CPF from the request cookies.
    """
    token = request.cookies.get("user_auth_token")
    payload = jwt.decode(token.split(" ")[1], os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
    user_cpf = payload.get("cpf")
    return str(user_cpf)

def get_admin_id(request: Request) -> str:
    """
    Get the admin ID from the request cookies.
    """
    token = request.cookies.get("admin_auth_token")
    payload = jwt.decode(token.split(" ")[1], os.getenv("ADMIN_JWT_SECRET"), algorithms=["HS256"])
    admin_id = payload.get("id")
    return admin_id

def get_admin_email(request: Request) -> str:
    """
    Get the admin email from the request cookies.
    """
    token = request.cookies.get("admin_auth_token")
    payload = jwt.decode(token.split(" ")[1], os.getenv("ADMIN_JWT_SECRET"), algorithms=["HS256"])
    admin_email = payload.get("email")
    return admin_email