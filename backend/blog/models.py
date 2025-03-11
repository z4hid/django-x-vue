from django.db import models
from django.contrib.auth.models import AbstractUser


class Site(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo/')

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = '1. Site'

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='user/avatars/%Y/%m/%d',
        default='user/avatars/default.jpg',
        blank=True, null=True)
    
    bio = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=100, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = '2. Users'

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = '3. Categories'

    def __str__(self):
        return self.name
    

