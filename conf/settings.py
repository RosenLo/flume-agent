#!/usr/bin/env python
# encoding: utf-8

"""
Author: Rosen
Mail: rosenluov@gmail.com
File: settings.py
Created Time: 12/28/16 11:53
"""

import logging
from socket import gethostname
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))
FLUME_FILE = BASE_DIR + '/flume.yaml'
STATSD_FILE = BASE_DIR + '/statsd.yaml'
PID_FILE = '/var/run/flume-agent/flume-agent.pid'
HOSTNAME = gethostname()

STDOUT = '/data/log/flume-agent/flume-agent.log'
STDERR = '/data/log/flume-agent/flume-agent.err'
LOG_FILE = BASE_DIR + '/log_conf'

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }

COUNTER = [
    u'Count',
    u'Timer',
]

EXCEPT = [
    u'Type',
    u'StartTime',
    u'StopTime',
]
