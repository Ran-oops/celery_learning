from __future__ import absolute_import    
from celery import Celery     
app = Celery('fourth_celerydemo', include=["fourth_celerydemo.tasks"])    
app.config_from_object("fourth_celerydemo.celeryconfig")     
if __name__ == "__main__":        
	app.start()     
