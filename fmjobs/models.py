from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    link1title = models.TextField(null=True, blank=True)
    link1 = models.TextField(null=True, blank=True)
    link2title = models.TextField(null=True, blank=True)
    link2 = models.TextField(null=True, blank=True)
    link3title = models.TextField(null=True, blank=True)
    link3 = models.TextField(null=True, blank=True)
    link4title = models.TextField(null=True, blank=True)
    link4 = models.TextField(null=True, blank=True)
    link5title = models.TextField(null=True, blank=True)
    link5 = models.TextField(null=True, blank=True)
    monthlyincome = models.IntegerField(null=True, blank=True)
    profitperiod = models.TextField(null=True, blank=True)
    advantage = models.TextField(null=True, blank=True)
    weakness = models.TextField(null=True, blank=True)
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    
class Plan(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    planer = models.CharField(max_length=6)
    classification = models.CharField(max_length=10)
    category = models.CharField(max_length=30)
    target_value = models.IntegerField()
    unit = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)
    modification_date = models.DateTimeField(blank=True, null=True)
    
    
    #inspection_code = models.CharField(max_length=10, unique=True)
    