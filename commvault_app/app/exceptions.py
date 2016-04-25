__author__ = "Vinod.Gupta@nutanix.com"


class LoginFailure(Exception):

    def __init__(self, username, password):
        self.username = username
        self.password = password
