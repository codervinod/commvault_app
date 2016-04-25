# This file contains all the logic to connect with commvault app
__author__ = "Vinod.Gupta@nutanix.com"

import base64
import json
import requests

from commvault_app.app import constants
from commvault_app.app import exceptions


class CommVaultApp(object):

    def __init__(self):
        self.server = None
        self.username = None
        self.password = None
        self.auth_token = None

    def get_auth_token(self):
        """

        :return:
        """
        return self.auth_token

    def _get_path(self, path_type, server=None):
        """

        :param path_type:
        :param server:
        :return:
        """
        server = server if server else self.server

        return constants.PROTO + server + ':' + \
            unicode(constants.BASE_PORT) +  \
            constants.COMMVAULT_PATHS[path_type]

    def login(self, server, username, password):
        """

        :param server:
        :param username:
        :param password:
        :return:
        """
        self.server = server
        self.username = username
        self.password = password

        login_body = constants.LOGIN_BODY
        login_body = login_body.replace('<<username>>', username)
        login_body = login_body.replace('<<password>>', base64.b64encode(
            password))
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/xml'}

        resp = requests.post(url=self._get_path(constants.LOGIN_PATH),
                             data=login_body, headers=headers)
        if resp.status_code == 200:
            try:
                r = json.loads(resp.text)
                self.auth_token = r['token']
                return self.auth_token
            except ValueError:
                pass
        raise exceptions.LoginFailure(username, password)

    def get_virtual_machines(self):
        pass


global_app = None


def get():
    global global_app
    if global_app is None:
        global_app = CommVaultApp()

    return global_app
