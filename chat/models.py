from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# class Contact(models.Model):
#     user = models.ForeignKey(
#         User, related_name='friends', on_delete=models.CASCADE)
#     friends = models.ManyToManyField('self', blank=True)

#     def __str__(self):
#         return self.user.username


class Message(models.Model):
    author = models.ForeignKey(
        User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]


# class Chat(models.Model):
#     participants = models.ManyToManyField(
#         Contact, related_name='chats', blank=True)
#     messages = models.ManyToManyField(Message, blank=True)

#     def __str__(self):
#         return "{}".format(self.pk)
