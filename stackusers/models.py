from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    User = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.CharField(max_length = 1000)
    Phone = models.IntegerField()
    Image = models.ImageField(default = 'default.jpg', upload_to = "profile_pic")


    def __str__(self):
        return f'{self.User.username} - Profile'
