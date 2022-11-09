from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/user/register")
def register_user():
    """
    API Question 1:
    Write an endpoint to register a user for a given name, phone number, email address and password
    and return the user object along with the token.
    Write an authentication middleware to encode and decode tokens. You should be able to extract
    the token from either the header or the cookie.
    :return: user object
    """
    pass


@app.get("/user/login")
def login_user():
    """
    API Question 2:
    Write an endpoint that checks for a registered user for a given phone number/email and password
    and returns with a token.
    :return: user object
    """
    pass


@app.get('/user/get')
def get_user():
    """
    API Question 3:
    Write an endpoint to return with the user context for a given token.
    :return: user object
    """
    pass