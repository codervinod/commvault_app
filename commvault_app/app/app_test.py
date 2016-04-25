__author__ = "Vinod.Gupta@nutanix.com"

import requests_mock

from unittest import TestCase
from commvault_app.app import app
from commvault_app.app import constants

class AppTest(TestCase):

    def __init__(self, *args, **kwargs):
        self.server = 'dummyserver.com'
        self.app = app.CommVaultApp(self.server)
        super(AppTest, self).__init__(*args, **kwargs)

    def setUp(self):
        pass

    def test_login(self):
        with requests_mock.mock() as m:
            login_url = self.app.getPath(constants.LOGIN_PATH)
            m.post(login_url, text='{"token":"test"}')
            self.app.login('admin', 'nutanix/4u')
            self.assertNotEqual(self.app.auth_token, None)
            self.assertEquals(self.app.auth_token, 'test')
