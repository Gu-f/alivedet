# -*- coding: utf-8 -*-

class SegmentType(object):
    Segment = "segment"  # 192.168.1.0/24
    SegmentRange1 = "segment_range1"  # 192.168.1.1-192.168.1.10
    SegmentRange2 = "segment_range2"  # 192.168.1.1-10
    IpListComma = "ip_list_comma"  # 192.168.1.1,192.168.1.2
    IpLIstSpace = "ip_list_space"  # 192.168.1.1 192.168.1.3


class DetType(object):
    ICMP_PING = "1"
    ARP_PING = "2"
    TCP_ACK_PING = "3"
    TCP_SYN_PING = "4"
    UDP_PING = "5"
