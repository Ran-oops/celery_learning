# coding=utf-8

BROKER_URL = 'redis://localhost:6379/1'    
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'    
CELERY_TASK_SERIALIZER = 'json'    
CELERY_RESULT_SERIALIZER = 'json'    
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24   # 任务过期时间    
CELERY_ACCEPT_CONTENT = ["json"]
