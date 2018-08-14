from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
   instance.profile.save()

class Profile(models.Model):
    name = models.CharField(max_length=250)
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.CharField(max_length=300)
    user = models.OneToOneField(User)
    email = models.EmailField(null = True)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Affidavit(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    user = models.ForeignKey(User)
    doc = models.ForeignKey(Profile)

    def __str__(self):
        return self.title

    def save_document(self):
        self.save()

    def delete_document(self):
        self.delete()

class DemandLetter(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    user = models.ForeignKey(User)
    doc = models.ForeignKey(Profile)

    def __str__(self):
        return self.title

    def save_demandletter(self):
        self.save()

    def delete_demandletter(self):
        self.delete()

class LawFirms(models.Model):
    name =  models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    email = models.EmailField(null = True)
    address = models.CharField(max_length=250)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def save_document(self):
        self.save()

    def delete_document(self):
        self.delete()
