from django.db import models
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='profiles', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    @receiver(models.signals.post_save, sender='auth.User')
    def ensure_profile_exists(sender, instance, **kwargs):
        if kwargs.get('created', False):
            Profile.objects.get_or_create(user=instance)
        