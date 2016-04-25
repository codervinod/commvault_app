__author__ = "Vinod.Gupta@nutanix.com"


class LoginFailure(Exception):

    def __init__(self, server, username, password):
        self.username = username
        self.password = password
