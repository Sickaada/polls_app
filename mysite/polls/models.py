from django.db import models
from django.utils import timezone
import datetime
# question_text is field of the model which is used as column in database
# models tells the whereabouts of our data in a app.
class Question(models.Model):
    question_text = models. CharField(max_length=250 )
    published_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
# time handling in python
        return now -datetime.timedelta(days=1) <= self.published_date <= now

# since there can be more than one choice for question, we will use "foreign key" - creates many to one relationship 
# use of on_delete = models.cascade --> if the question is deleted, the choices will be deleted automatically
class options(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    option_text1 = models.CharField(max_length=250,default = '')
    votes_count = models.IntegerField(default = 0)
    def __str__(self):
        return self.option_text1
