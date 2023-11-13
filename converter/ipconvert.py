# -*- coding: utf-8 -*-
from converter.base import IpConvertBase


class IpConvert(IpConvertBase):
    def __init__(self, ip_strs):
        super().__init__(ip_strs)
