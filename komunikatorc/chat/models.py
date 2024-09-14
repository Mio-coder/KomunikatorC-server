from django.db import models


class User(models.Model):
    username = models.TextField(unique=True, max_length=100)
    password = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')

    class Meta:
        unique_together = ('user', 'friend')


class Group(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=100)
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)
    users = models.ManyToManyField(User)


class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    reaction = models.TextField(max_length=100)

    class Meta:
        unique_together = ('user', 'message')
