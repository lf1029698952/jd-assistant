# -*- coding:utf-8 -*-
import time
import json
import requests
from datetime import datetime
from log import logger


class Timer(object):

    def __init__(self, buy_time, sleep_interval=0.01):

        # '2018-09-28 22:45:50.000'
        self.buy_time = datetime.strptime(buy_time, "%Y-%m-%d %H:%M:%S.%f")
        self.sleep_interval = sleep_interval

    def start(self):
        logger.info('正在等待到达设定时间:%s' % self.buy_time)
        now_time = datetime.now
        while True:
            if now_time() >= self.buy_time:
                logger.info('时间到达，开始执行……')
                break
            else:
                time.sleep(self.sleep_interval)

    def getJDSystemTime(self):
        #获取京东服务器时间，需要计算延迟时差，大概30ms
        url = 'https://a.jd.com//ajax/queryServerData.html'
        session = requests.session()

        # get server time
        result = session.get(url).text
        print(result)
        servertime = json.load(result)
        jdServertime = servertime["serverTime"]
        print(jdServertime)
        localtime = jdServertime - 30

        return localtime
