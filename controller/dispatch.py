# -*- coding: utf-8 -*-
import sys
import threading
import time
from queue import Queue
from threading import Event, Thread
from _queue import Empty

from converter.ipconvert import IpConvert
from detcore.icmp_ping import IcmpPing


class Dispatcher(object):
    LOCK = threading.Lock()
    COUNTER = 0

    def __init__(self, ip_strs: list):
        self.inputs = Queue(10000)
        self.outputs = Queue(10000)
        self.ip_strs = ip_strs
        self.thread_list = []

    @classmethod
    def get_data(cls, data_queue):
        data = None
        try:
            data = data_queue.get(timeout=1)
        except Empty:
            pass
            # print("当前队列为空")
        return data

    def start(self, event_signal: Event, multi: int):
        # 启动探测线程
        print("启动探测线程")
        for i in range(multi):
            detect_thread = Thread(target=self.loop_detect,
                                   args=(self.inputs, self.outputs, event_signal))
            detect_thread.start()
            self.thread_list.append(detect_thread)
        # 启动记录线程
        print("启动记录线程")
        record_thread = Thread(target=self.loop_record, args=(self.outputs, event_signal))
        record_thread.start()
        self.thread_list.append(record_thread)
        # 开始IP解析
        print("开始解析IP...")
        convert_obj = IpConvert(self.ip_strs)
        convert_obj.parser(ips_queue=self.inputs)
        print("解析IP完成.")

        wait_for = 2
        while event_signal.is_set():
            time.sleep(3)
            print(f"剩余待处理-{self.inputs.qsize()}, 剩余已处理-{self.outputs.qsize()}, 剩余正在处理-{self.COUNTER}")
            if self.inputs.qsize() == 0 and self.outputs.qsize() == 0 and self.COUNTER == 0:
                if wait_for != 0:
                    wait_for -= 1
                else:
                    event_signal.clear()
                    print("扫描完成。")

    @classmethod
    def loop_detect(cls, inputs: Queue, outputs: Queue, event_signal: Event):
        while event_signal.is_set():
            ip = cls.get_data(inputs)
            if ip:
                cls.LOCK.acquire()
                cls.COUNTER += 1
                cls.LOCK.release()
                status = IcmpPing(ip).ping()
                cls.LOCK.acquire()
                cls.COUNTER -= 1
                cls.LOCK.release()
                outputs.put((ip, status))
                print(f"{ip}  {status}")
            # print("探测线程正在运行")

    @classmethod
    def loop_record(cls, outputs: Queue, event_signal: Event):
        with open(f'result-{int(time.time())}.txt', 'w') as fp:
            while event_signal.is_set():
                data = cls.get_data(outputs)
                if data:
                    fp.write(f"{data[0]}  {data[1]}\n")
                # print("写入线程正在运行")
