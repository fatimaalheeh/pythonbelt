from django.db import models
import re

class UserManager(models.Manager):
    def basic_Validator(request,postData):
        pass

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass
class Messages(models.Model):
    message = models.CharField(max_length=2550)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Users, related_name="messages", on_delete = models.CASCADE)
class Comments(models.Model):
    comment = models.CharField(max_length=2550)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Users, related_name="comments", on_delete = models.CASCADE)
    message_id = models.ForeignKey(Messages, related_name="comments", on_delete = models.CASCADE)


