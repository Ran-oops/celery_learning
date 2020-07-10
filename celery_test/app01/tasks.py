# -*- coding:utf8 -*-
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time

# 这里不再使用@app.task,而是用@shared_task，是指定可以在其他APP中也可以调用这个任务
@shared_task
def add(x,y):
    print('########## running add #####################')
    return x + y

@shared_task
def minus(x,y):
    # time.sleep(30)
    print('########## running minus #####################')
    return x - y