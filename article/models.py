
#coding:utf-8
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    block=models.ForeignKey(Block,verbose_name=u"所属板块")
    owner=models.ForeignKey(User,verbose_name=u"作者")
    title=models.CharField(u"标题",max_length=300)
    content=models.CharField(u"内容",max_length=30000)
    status=models.IntegerField(u"状态",choices=((0,u"普通"),(-1,u"删除"),(10,u"精华")),default=0)
    create_timestamp=models.DateTimeField(auto_now_add=True)
    last_update_timestamp=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name=u"文章"
        verbose_name_plural=u"文章"

    
