#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-04 15:18:58
# @Author  : 陈小雪
# @Email   : shell_chen@yeah.net

from flask import Blueprint

main_bp = Blueprint('main', __name__)

import routes, events
