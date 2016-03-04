#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-04 15:18:58
# @Author  : 陈小雪
# @Email   : shell_chen@yeah.net

from flask import Flask
from flask.ext.socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'addafdsfrfnrjgjrbvba'

    from .main import main_bp
    app.register_blueprint(main_bp)

    socketio.init_app(app)
    return app

