from django.conf import settings
from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    num = models.CharField(max_length=1)
    price = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    picture = models.ImageField(upload_to='media', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.picture.name)
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Hot(models.Model):
    author = models.CharField(max_length=15)
    num = models.CharField(max_length=1)
    price = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    picture = models.ImageField(upload_to='media', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.picture.name)
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Guest(models.Model):
    author = models.CharField(max_length=15)
    num = models.CharField(max_length=1)
    price = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    picture = models.ImageField(upload_to='media', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.picture.name)
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title