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

    def getPath(self, path_type):
        """

        :param path_type:
        :return:
        """
        return constants.PROTO + self.server + ':' + \
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

        resp = requests.post(url=self.getPath(constants.LOGIN_PATH),
                             data=login_body, headers=headers)
        if resp.status_code == 200:
            r = json.loads(resp.text)
            self.auth_token = r['token']
            return

        raise exceptions.LoginFailure(server, username, password)
