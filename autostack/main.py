'''
Authors: Elijah Sawyers, Benjamin Sanders
Emails: elijahsawyers@gmail.com, ben.sanders97@gmail.com
Date: 03/17/2019
Overview: This opens the named pipe '/tmp/monitorPipe' and listens for data
passed to the pipe. If the data is detected to be a python error, it queries
Stack Overflow for the error and displays posts with accepted answers.
'''

from __future__ import print_function
from builtins import input
import os

from autostack.pipe import (
    create_pipe
)

PIPE_PATH = '/tmp/monitorPipe'


def main():
    '''
    Opens the fifo '/tmp/monitorPipe' and starts listening for python
    errors inputed to the pipe.
    '''

    try:
        create_pipe(PIPE_PATH)
    except:
        pass

    pipe = open(PIPE_PATH, 'r')

    listen_for_errors(pipe)
