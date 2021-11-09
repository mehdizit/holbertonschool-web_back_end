#!/usr/bin/env python3
""" Basic auth, Base64 part, Base64 decode, User credentials, User object,
    Overload current_user - and BOOM!, Allow password with ":" """

from api.v1.auth.auth import Auth
import base64


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
