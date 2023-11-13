# -*- coding: utf-8 -*-
from scapy.layers.inet import IP, ICMP, sr1
from detcore.base import BasePing


class IcmpPing(BasePing):
    def __init__(self, ip, timeout=2):
        self.timout = timeout
        super().__init__(ip)

    def process(self):
        packet = IP(dst=self.ip) / ICMP()
        response = sr1(packet, timeout=self.timout, verbose=False)
        if response:
            return True
        return False
