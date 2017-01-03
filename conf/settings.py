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
PID_FILE = '/var/run/flume-monitor-agent/flume-monitor-agent.pid'
HOSTNAME = gethostname()

STDOUT = '/data/log/flume-monitor-agent/flume-agent.log'
STDERR = '/data/log/flume-monitor-agent/flume-agent.err'

IF_DATA = {
    u'True': 1,
    u'False': 0
}


COUNTER = [
    u'Count',
]

EXCEPT = [
    u'Type',
    u'StartTime',
    u'StopTime',
    u'SendTimer',
]
