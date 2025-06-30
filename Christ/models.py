from django.db import models

# Create your models here

class Sermon(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField(blank=True)
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Devotional(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField()  # ← Add this line
    image = models.ImageField(upload_to='devotionals/')
    tag = models.CharField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title




    
