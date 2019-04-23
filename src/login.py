#! /usr/bin/env python
# -*- conding: utf8 -*-

"""StackOverflow Remote Login
    This module provides login to stackoverflow.com
"""

import re
import requests


class StackOverflow(object):
    """
        :param email:
        :param password:
    """

    # Form action
    ACTION = 'https://stackoverflow.com/users/login?\
    ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f'

    # Edit your profile (to check if user is logged)
    check_login = 'https://stackoverflow.com/users/edit/'

    # Form data
    FORM = {
        "fkey": "96a951839d53e991ecd53c4fd6b9c729",
        "submit-button": "Log in",
        "ssrc": "head"
    }

    # Initialize user's data
    USER = {}

    # Regex
    REGEX_USER_ID = re.compile(r'<a href="/users/([0-9]{1,})/(\w+)" .*?>')
    REGEX_USERNAME = re.compile(r'<a href="/users/([0-9]{1,})/(\w+)" .*?>')

    # Initialize new session
    session = requests.session()

    def __init__(self, email, password):
        """
        :param email:
        :param password:
        """

        # LOGIN: Email
        self.FORM['email'] = email

        # LOGIN: Password
        self.FORM['password'] = password

    def login(self):
        """
        :return:
        """

        # Current Session
        session = self.session

        # Response from the site
        response = session.post(self.ACTION, data=self.FORM)

        # if logged
        if bool(self.REGEX_USER_ID.search(response.text)):
            self.USER['id'] = self.REGEX_USER_ID.search(
                response.text).groups()[0]
            self.USER['nick'] = self.REGEX_USERNAME.search(
                response.text).groups()[1]
            self.check_login = self.check_login + self.USER['id']

            return response

        return False

    def logged(self):
        """
        :return:
        """

        # Current session
        session = self.session

        # Try to edit profile and get "status code"
        status = session.get(self.check_login).status_code

        # If 200 / OK
        if status == 200:
            return True

        return False

    def close(self):
        """
            :return True:
        """

        # Current session
        session = self.session

        # Close current session
        session.close()

        return True
