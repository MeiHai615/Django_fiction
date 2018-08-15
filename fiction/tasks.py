# -*- coding: utf-8 -*-
__author__ = 'MeiHai'
__date__ = '2018/7/23 11:59'
from celery import Celery, platforms
from time import sleep
platforms.C_FORCE_ROOT = True
# app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')
app = Celery('tasks', broker='redis://localhost:6379/10')
@app.task
def add(x, y):
    # sleep(5)
    return x + y

if __name__ == '__main__':
    result = add.delay(30,30)
    print(result)


