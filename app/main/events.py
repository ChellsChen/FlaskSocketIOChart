#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-04 15:18:58
# @Author  : 陈小雪
# @Email   : shell_chen@yeah.net

from flask import session
from flask.ext.socketio import emit, join_room, leave_room
from .. import socketio



@socketio.on('joined', namespace='/chat')
def joined(message):
    """当一个client进来的时候，通知在这个room里的所有client"""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def sent(message):
    """当room里的client送来一条消息时，向在这个room的所有client都发出消息"""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ' : ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """当client离开room的时候，发离开通知给这个room的所有client"""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)




