from django.db import models
# question_text is field of the model which is used as coloumn in database
# models tells the whereabouts of our data in a app.
class Question(models.Model):
    question_text = models. CharField(max_length=250 )
    published_date = models.DateTimeField('date published')

# since there can be more than one choice for question, we will use "foreign key" - creates many to one relationship 
# use of on_delete = models.cascade --> if the question is deleted, the choices will be deleted automatically
class options(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)