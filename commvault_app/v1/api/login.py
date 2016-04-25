# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
from .. import schemas

from commvault_app.app import app as commvault_app

class Login(Resource):

    def post(self):
        server = g.json['server']
        username = g.json['user']
        password = g.json['password']
        token = commvault_app.get().login(server, username, password)
        return {'token': token}, 200, None
