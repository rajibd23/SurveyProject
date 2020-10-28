import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    seq = models.IntegerField(default=1)
    class Meta:
        ordering = ('seq',)
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

class SurveyResponse(models.Model):
    name = models.CharField(max_length=200)
    emailid = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default='Enter City')
    #save the choice_id in these fields as per response
    question1 = models.CharField(max_length=10, default='0')
    question2 = models.CharField(max_length=10, default='0')
    question3 = models.CharField(max_length=250, default='Please enter')
    question4 = models.CharField(max_length=250, default='Self')
    question5 = models.CharField(max_length=250, default='Medicine Procurement')
    question6 = models.CharField(max_length=10, default='0')
    question7 = models.CharField(max_length=250, default='Weekly')
    question8 = models.CharField(max_length=10, default='0')
    question9 = models.CharField(max_length=10, default='0')
    question10 = models.CharField(max_length=10, default='0')
    question11 = models.CharField(max_length=250, default='Health monitoring')
    question12 = models.CharField(max_length=250, default='Rs. 7000 to Rs. 10000')
    comments = models.CharField(max_length=250, default='Enter Comment')
    res_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
