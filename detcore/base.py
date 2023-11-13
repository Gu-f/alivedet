# -*- coding: utf-8 -*-
class BasePing(object):
    def __init__(self, ip):
        self.ip = ip

    def ping(self) -> bool:
        return self.process()

    def process(self) -> bool:
        raise NotImplementedError
