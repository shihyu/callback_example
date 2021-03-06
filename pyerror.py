# -*- coding: utf-8 -*-

class PyError(Exception):

    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return repr(self._msg)
