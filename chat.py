#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-04 15:18:58
# @Author  : 陈小雪
# @Email   : shell_chen@yeah.net


from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port = 8888)
