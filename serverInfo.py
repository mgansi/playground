from flask import request
import os

class ServerInfo:
    def __init__(self, x):
        self.x = x

    @staticmethod
    def get_info():
        """ get information from computer for display"""
        info = {}
        info['os'] = os.uname()
        info['ip'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        return info

