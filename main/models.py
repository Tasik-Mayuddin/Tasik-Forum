from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField

# Create your models here.
class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="thread", null=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    edited_at = models.DateTimeField(auto_now=True, null=True)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000000000000)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    edit_status = BooleanField(default=False)
    edited_at = models.DateTimeField(auto_now=True, null=True)
    reply = models.CharField(max_length=200, default=False)
    
    def __str__(self):
        return self.content

class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='images')

    def __str__(self):
        return f'{self.user.username} Profile'


