#!/usr/bin/env python3
""" Basic auth, Base64 part, Base64 decode, User credentials, User object,
    Overload current_user - and BOOM!, Allow password with ":" """

from api.v1.auth.auth import Auth


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
