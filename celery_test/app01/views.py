from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from app01 import tasks

# Create your views here.

def index(request,*args,**kwargs):
    res=tasks.add.delay(1,3)
    #任务逻辑
    return JsonResponse({'status':res.status,'task_id':res.task_id})
    
def test(request):
    print('helloooooooooooo')
    #任务逻辑
    return JsonResponse({'status':'successful','task_id':"OK!"})