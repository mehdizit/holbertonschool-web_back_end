#!/usr/bin/env python3
""" Hash password """

import bcrypt
from db import DB
from user import User

def _hash_password(password: str) -> str:
    """ returns a string The returned string is a salted hash of the input password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())