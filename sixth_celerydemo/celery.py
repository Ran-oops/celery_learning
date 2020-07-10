from __future__ import absolute_import    
from celery import Celery     
app = Celery('sixth_celerydemo', include=["sixth_celerydemo.tasks"])    
app.config_from_object("sixth_celerydemo.celeryconfig")     
if __name__ == "__main__":        
	app.start()     
