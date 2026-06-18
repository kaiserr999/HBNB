#!/usr/bin/env python3

from HBNB.app.services.facade import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name, last_name, email):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def email(self):
        return self.__email
    
    @first_name.setter
    def first_name(self, value):
        if value is None:
            raise ValueError("Enter a valid first name")
        self.__first_name = value
    
    @last_name.setter
    def last_name(self, value):
        if value is None:
            raise ValueError("Enter a valid last name")
        self.__last_name = value

    @email.setter
    def email(self, value):
        email_validate_pattern = r"^\S+@\S+\.\S+$"
        valid = re.match(email_validate_pattern, value)
        if valid is True:
            self.__email = value
        else:
            raise ValueError("The email doesnt match the standard form")
