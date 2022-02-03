from cProfile import label
from time import timezone
from django.db import models
import datetime
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')
    def __str__(self):
        return u"%s%s" % (self.question_text, self.pub_date)
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    advice = models.CharField(max_length=200, default='adv')
    votes = models.IntegerField(default=0)
    def __str__(self):
        return u'%s, %s, %s' % (self.choice_text, self.advice, self.votes)


    


