__author__ = "Vinod.Gupta@nutanix.com"

import requests_mock

from unittest import TestCase
from commvault_app.app import app
from commvault_app.app import constants
from commvault_app.app import exceptions


class AppTest(TestCase):

    def __init__(self, *args, **kwargs):
        self.server = 'dummyserver.com'
        self.app = app.CommVaultApp()
        super(AppTest, self).__init__(*args, **kwargs)

    def test_getPath(self):
        login_path = self.app._get_path(constants.LOGIN_PATH, self.server)
        self.assertEquals(
            login_path,
            u'http://dummyserver.com:81/SearchSvc/CVWebService.svc/Login')

    def test_login(self):
        with requests_mock.mock() as m:
            login_url = self.app._get_path(constants.LOGIN_PATH, self.server)
            m.post(login_url, text='{"token":"test"}')
            self.app.login(self.server, 'admin', 'nutanix/4u')
            self.assertNotEqual(self.app.auth_token, None)
            self.assertEquals(self.app.auth_token, 'test')

    def test_login_fails(self):
        with requests_mock.mock() as m:
            login_url = self.app._get_path(constants.LOGIN_PATH, self.server)
            m.post(login_url, text='Failed')
            with self.assertRaises(exceptions.LoginFailure):
                self.app.login(self.server, 'admin', 'nutanix/4u')
