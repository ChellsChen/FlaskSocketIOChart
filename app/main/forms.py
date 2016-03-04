#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-04 15:18:58
# @Author  : 陈小雪
# @Email   : shell_chen@yeah.net

from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('name', validators=[Required()])
    room = StringField('room', validators=[Required()])
    submit = SubmitField('enter')
