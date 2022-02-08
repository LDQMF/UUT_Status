#!/usr/bin/env python3

import os
import test_station
import tm
import logging

# tss = "log@192.168.0.130 log@192.168.0.83".split()
tss = "log@192.168.0.210 log@192.168.0.130".split()
hop = "cchiang@192.168.66.36"

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # if flask_env env is development will not sync
    if os.getenv('FLASK_ENV') == 'development':
        del os.environ['FLASK_ENV']

    prjs = tm.TestMonitor.getSupportedPrj()
    print(prjs)

    for ts in tss:
        t = test_station.TestStation(ts)
        t.sync(prjs, hop=hop)
        

