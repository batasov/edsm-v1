from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from docs.models import Doc
import datetime

def change_image(post_object):
    ''' 
    функция удаления изображений при их замене на новые
    '''
    try:
        pre_object = post_object.__class__.objects.get(id=post_object.id)
        if pre_object.photo != post_object.photo:
            pre_object.photo.delete(save=False)
    except:
        pass


def delete_image(sender, **kwargs):
    '''
    функция удаления изображений при удалении объектов
    '''
    try:
        object_ = kwargs.get('instance')
        storage, path = object_.photo.storage, object_.photo.path
        storage.delete(path)
    except:
        pass

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, blank=True)
    patronymic = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='media', blank=True)
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    def save(self, *args, **kwargs):
        change_image(post_object=self)
        super(UserProfile, self).save(*args, **kwargs)

    post_save.connect(create_user_profile, sender=User)
    post_delete.connect(receiver=delete_image)

class Notif(models.Model):
    now = datetime.datetime.now()

    user = models.ForeignKey(User, related_name="notif", on_delete=models.CASCADE)
    doc = models.ForeignKey(Doc, related_name="notif", on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    is_signature_request = models.BooleanField(default=False)
    message = models.CharField(max_length=500, blank=True)
    date = models.DateField(default=now.strftime("%Y-%m-%d"))
    is_signature = models.BooleanField(default=False)

    
        
