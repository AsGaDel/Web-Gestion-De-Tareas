from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)



class Thread(models.Model):
    users = models.ManyToManyField('auth.User', related_name='threads')
    messages = models.ManyToManyField(Message, related_name='threads')
'''
    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return f'Thread {self.pk}'

    def get_last_message(self):
        return self.messages.last()
'''