# coding=utf-8
from __future__ import absolute_import    
from sixth_celerydemo.celery import app
from celery.utils.log import get_task_logger  
from celery.signals import after_task_publish  
  
@app.task    
def add(x, y):        
	return x + y 

# 在执行任务 add 之后, 打印一些信息. 
@after_task_publish
def task_send_handler(sender=None, body=None, **kwargs):    
	print 'after_task_publish: task_id: {body[id]}; sender: {sender}'.format(body=body, sender=sender)

logger = get_task_logger(__name__)


@app.task(bind=True)                                                                             
def div(self, x, y):                                                                             
    logger.info(('Executing task id {0.id}, args: {0.args!r} '                                   
                 'kwargs: {0.kwargs!r}').format(self.request))                                   
    try:                                                                                         
        result = x / y                                                                           
    except ZeroDivisionError as e:                                                               
        raise self.retry(exc=e, countdown=5, max_retries=3)                                      
    return result  