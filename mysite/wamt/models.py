from django.db import models
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_location = models.CharField(max_length=200)  # may change in the future
    event_start_vote_time = models.DateTimeField("start vote time", default=datetime.now)
    event_end_vote_time = models.DateTimeField("end vote time", default=datetime.now)
    event_time = models.DateTimeField("event time", default=datetime.now)


class GroupEventManager(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    group_events = models.ManyToManyField(Event)
    @receiver(post_save, sender=Group)
    def create_group_event(sender, instance, created, **kwargs):
        if created:
            GroupEvent.objects.create(group=instance)

    @receiver(post_save, sender=Group)
    def save_group_event(sender, instance, **kwargs):
        instance.GroupEvent.save()


class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_simple_describe = models.CharField(max_length=200)
    movie_detailed_describe = models.TextField()
    movie_link = models.URLField()
    movie_published = models.DateTimeField("date published")

    def __str__(self):
        return self.movie_title
