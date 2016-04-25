__author__ = "Vinod.Gupta@nutanix.com"

from unittest import TestCase
from commvault_app.app import app

class AppTest(TestCase):

    def __init__(self, *args, **kwargs):
        self.app = app.CommVaultApp()
        super(AppTest, self).__init__(*args, **kwargs)

    def setUp(self):
        pass

    def test_login(self):
        self.app.login('10.4.8.86', 'admin', 'nutanix/4u')
        self.assertNotEqual(self.app.auth_token, None)
