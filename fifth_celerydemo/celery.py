from __future__ import absolute_import    
from celery import Celery     
app = Celery('fifth_celerydemo', include=["fifth_celerydemo.tasks"])    
app.config_from_object("fifth_celerydemo.celeryconfig")     
if __name__ == "__main__":        
	app.start()     
