# from celery import Celery

# app = Celery('tasks', broker='amqp://guest@localhost//')

# @app.task
# def add(x, y):
    # return x + y
    
import time
from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/1')

@celery.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')


@celery.task
def get_list():
    lists = ['hello', 1, 'change', 'modify']
    
    print('this is lists', lists)
    return lists