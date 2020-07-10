from __future__ import absolute_import    
from celery import Celery     
app = Celery('third_celerydemo', include=["third_celerydemo.tasks"])    
app.config_from_object("third_celerydemo.celeryconfig")     
if __name__ == "__main__":        
	app.start()     
