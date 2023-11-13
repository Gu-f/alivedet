# -*- coding: utf-8 -*-
from multiprocessing import Queue
from _queue import Empty


class Dispatcher(object):
    def __init__(self, inputs: Queue, outputs: Queue):
        self.inputs = inputs
        self.outputs = outputs

    def get_data(self):
        data = None
        try:
            data = self.inputs.get(timeout=1)
        except Empty:
            print("当前队列为空")
        return data

    def start(self):
        pass

    def loop_detect(self):
        pass

    def loop_record(self):
        pass
