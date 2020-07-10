# celery_learning
```

python3 -m venv python3.5  //创建一个名为python3.5的虚拟环境
. python3.5/bin/activate  //进入python3.5的虚拟环境


###########celery的常用命令###############
celery -A projname worker -l info     //启动worker
celery -A projname worker -Q web_tasks -l info   //启动worker到对应的queue
celery -A projname beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler  //启动django-celery-beat
celery multi start w1 w2 -A projname -l info   //启动两个worker进程
celery -A projname status    //查看workder进程状态
python3 manage.py migrate django_celery_beat   //为添加到installed_app的django-celery-beat迁移数据库


##########redis的常用命令#################
select 1
keys *
type key
smembers key   //如果是set类型
lrange key 0 1   //如果是list类型
llen key   //如果是list类型
get key  //如果是string类型
hget key  //如果是hash类型



```
