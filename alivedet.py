# -*- coding: utf-8 -*-
import logging
import sys
from docopt import docopt
from threading import Event

from controller.dispatch import Dispatcher


def main():
    USAGES = """Host Alive Det:

        Usage:
          alivedet.py (--hosts=<hosts>)...
                  [--multi=<multi>]
                  [--log-level=<log-level>]
          alivedet.py --version

        Options:
          -h --help                           显示帮助信息
          --version                           显示版本
          --hosts=<hosts>                     要探测的hosts,可空格写多个
          --multi=<multi>                     并发数 [default: 10]
          --log-level=<log-level>             记录日志级别 [DEBUG|INFO|WARNING|ERROR|CRITICAL] [default: ERROR]
        """
    arguments = docopt(USAGES, options_first=True, version="Alivedet 1.0")

    hosts = arguments.get("--hosts")
    multi = int(arguments.get("--multi"))
    log_level = arguments.get("--log-level")

    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        print(f"Log Level not support {log_level}")
        sys.exit(1)

    if multi > 50000 or multi < 1:
        print(f"multi must be [1, 50000], current is {multi}")
        sys.exit(1)

    logging.getLogger("scapy.runtime").setLevel(log_level)
    dispatcher = Dispatcher(hosts)
    event_signal = Event()
    event_signal.set()
    try:
        dispatcher.start(event_signal, multi)
    except KeyboardInterrupt:
        event_signal.clear()
        print("已终止!")
        sys.exit(0)


if __name__ == '__main__':
    main()
