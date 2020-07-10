from __future__ import absolute_import    
from celery import Celery     
app = Celery('second_celerydemo', include=["second_celerydemo.tasks"])    
app.config_from_object("second_celerydemo.celeryconfig")     
if __name__ == "__main__":        
	app.start()     
