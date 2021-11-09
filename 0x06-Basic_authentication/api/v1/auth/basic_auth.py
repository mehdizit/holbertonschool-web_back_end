#!/usr/bin/env python3
""" Basic auth, Base64 part, Base64 decode, User credentials, User object,
    Overload current_user - and BOOM!, Allow password with ":" """

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        base = authorization_header.split(' ')
        return base[1]
        
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ returns the decoded value of a Base64 string """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            b64_bytes = base64_authorization_header.encode('utf-8')
            string_bytes = base64.b64decode(b64_bytes)
            return string_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """ returns tuple of email and password for users """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(':')
        return credentials[0], credentials[1]
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a request """
        try:
            header = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(header)
            decodeValue = self.decode_base64_authorization_header(base64Header)
            credentials = self.extract_user_credentials(decodeValue)
            user = self.user_object_from_credentials(credentials[0], credentials[1])
            return user
        except Exception:
            return None
