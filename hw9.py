#!/usr/bin/env python3.6

import time
import traceback
from datetime import datetime


class ContextManager:
    def __init__(self, path):
        """ Method that initialize instance

        :type path: str
        :param path: file that will contain some errors
        """

        self.path = path


    def __enter__(self):
        self.start = time.time()


    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Method to exit from context manager

        :param exc_type: type of error
        :param exc_val: value of error
        :param exc_tb: traceback of error
        """

        if exc_type is not None:
            exec_time = self.start - time.time()
            with open(self.path, 'w') as file:
                traceback.print_exception(exc_type, exc_val, exc_tb, file=file)
                file.write('Date of error is {}\n'.format(datetime.now().date()))
                file.write('Time of execution is {}\n'.format(exec_time))


if __name__ == '__main__':
    with ContextManager('somefile.txt') as file:
        try:
            3 / 0
        except ZeroDivisionError:
            raise ZeroDivisionError
