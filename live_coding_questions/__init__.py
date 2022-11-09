from pydantic import BaseModel


class UserAsset(BaseModel):
    """
    Write a user asset model class with the following attributes and methods
    Attributes
    ---------------------
    package_name: This should be a custom attribute and accept strings like
    "package://bucket/resource/<filename>" only
    """


class User(BaseModel):
    """
    Write a user model class with the following attributes and methods
    Attributes
    -----------------------
    Name
    Phone No
    Email
    Password
    (Advanced/Optional - List of User Assets)

    Methods
    ------------------------
    Login / Authenticate
    Get from Mongo DB
    Save to Mongo DB
    Register
    Delete
    Update
    """

