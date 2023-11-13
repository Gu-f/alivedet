# -*- coding: utf-8 -*-
import re
import socket


class IpConvertBase(object):
    _SEGMENT_RANGE_1_PATTERN = re.compile("((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))-((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))")

    def __init__(self, ip_strs: list):
        if not isinstance(ip_strs, list):
            raise ValueError(f"ip_strs must be a list.")
        self._support_parsers = []
        self.ip_strs = ip_strs
        self.register_parser(self._segment_range_1)

    def register_parser(self, func):
        self._support_parsers.append(func)

    def parser(self):
        results = set()
        for ip_str in self.ip_strs:
            for parser_func in self._support_parsers:
                ips = parser_func(ip_str)
                if ips:
                    for ip in ips:
                        results.add(ip)
                    break
        return sorted(results, key=socket.inet_aton)

    def _segment_range_1(self, ip_str) -> list:
        """
        192.168.1.1-192.168.1.10
        :param ip_str:
        :return: [ip,ip]
        """
        results = []
        if re.match(self._SEGMENT_RANGE_1_PATTERN, ip_str):
            start_ip, end_ip = ip_str.split('-')
            ip_prefix = '.'.join(start_ip.split('.')[:3])
            for i in range(int(start_ip.split('.')[-1]), int(end_ip.split('.')[-1]) + 1, 1):
                results.append(f"{ip_prefix}.{i}")
        return results
