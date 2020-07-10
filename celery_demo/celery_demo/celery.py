#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:sy
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 设置django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_demo.settings')  
app = Celery('celery_demo')
#  使用CELERY_ 作为前缀，在settings中写配置
app.config_from_object('django.conf:settings', namespace='CELERY') 
# 发现任务文件每个app下的task.py
app.autodiscover_tasks()  