# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

from .api.login import Login
from .api.logout import Logout


routes = [
    dict(resource=Login, urls=['/login'], endpoint='login'),
    dict(resource=Logout, urls=['/logout'], endpoint='logout'),
]