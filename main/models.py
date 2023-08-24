from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=100)
    describtion = models.CharField(max_length=200)
    cost = models.PositiveIntegerField()
    date = models.DateField(default=datetime.date.today())


class UserAccount(models.Model): 
    user = models.ForeignKey(User, on_delete = models.CASCADE, unique=True)
    data = models.ManyToManyField(Expense)
    limit_per_day = models.IntegerField(null = True)
    limit_per_month = models.IntegerField(null = True)
    


