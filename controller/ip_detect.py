# -*- coding: utf-8 -*-
from const import DetType
from detcore.icmp_ping import IcmpPing


def check_host_status(ip, det_type):
    if det_type == DetType.ICMP_PING:
        return IcmpPing(ip).ping()
