from __future__ import absolute_import    
from fourth_celerydemo.celery import app   
  
@app.task    
def add(x, y):        
	return x + y 
