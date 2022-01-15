#! /usr/bin/env python

"""StackOverflow Remote Login
    This module provides login to stackoverflow.com
"""

import requests
from bs4 import BeautifulSoup
from typing import TypedDict, Optional


class Form(TypedDict):
    ssrc: str
    email: str
    password: str


class User(TypedDict):
    id: str
    nick: str


class Credentials(TypedDict):
    username: Optional[str]
    password: Optional[str]


class StackOverflow(object):
    # Form action
    ACTION: str = 'https://stackoverflow.com/users/login'

    # Edit your profile (to check if user is logged)
    check_login: str = 'https://stackoverflow.com/users/edit/'

    # Form data
    FORM: Form = {
        "ssrc": "login"
    }

    # Initialize user's data
    USER: User = {}

    # Initialize new session
    session = requests.session()

    def __init__(self, credentials: Credentials):
        self.FORM['email'] = credentials['username']
        self.FORM['password'] = credentials['password']

    def login(self) -> bool:
        """
        :return:
        """

        # Current Session
        session = self.session

        # Response from the site
        response = session.post(self.ACTION, data=self.FORM)

        soup = BeautifulSoup(response.text, 'html.parser')

        my_profile = soup.find(
            "a",
            {
                "class": "my-profile"
            }
        )

        # if logged
        if my_profile is not None:
            href = my_profile.attrs["href"]

            self.USER['id'] = href.split("/")[2]
            self.USER['nick'] = href.split("/")[3]

            self.check_login = self.check_login + self.USER['id']

            return response.status_code == 200

        return False

    def logged(self) -> bool:
        # Current session
        session = self.session

        # Try to edit profile and get "status code"
        response = session.get(self.check_login)

        print(response.status_code)

        return response.status_code == 200

    def close(self) -> bool:
        # Current session
        session = self.session

        # Close current session
        session.close()

        return True
