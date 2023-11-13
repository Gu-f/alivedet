# -*- coding: utf-8 -*-
from detcore.icmp_ping import IcmpPing
from converter.ipconvert import IpConvert

from multiprocessing import Queue


def main():
    # 数据队列
    input_ips_queue = Queue(10000)
    output_status_queue = Queue(10000)
    aa = IpConvert(["192.168.1.1-192.168.1.10"])
    print(aa.parser())

    # print(IcmpPing("192.168.1.1").ping())


if __name__ == '__main__':
    main()
