from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200,verbose_name="学习主题",default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    text = models.CharField(max_length=200,verbose_name="学习条目",default="")
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)

    def __str__(self):
        return self.text