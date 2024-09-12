from django.db import models


class User(models.Model):
    username = models.TextField(unique=True)
    password = models.CharField(max_length=128)
    avatar = models.TextField(null=True, blank=True)


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')

    class Meta:
        unique_together = ('user', 'friend')


class Group(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    icon = models.TextField(null=True, blank=True)
    users = models.ManyToManyField(User)


class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    reaction = models.TextField()

    class Meta:
        unique_together = ('user', 'message')
