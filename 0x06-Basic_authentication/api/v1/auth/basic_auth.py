#!/usr/bin/env python3
""" Basic auth, Base64 part, Base64 decode, User credentials, User object,
    Overload current_user - and BOOM!, Allow password with ":" """

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class """
