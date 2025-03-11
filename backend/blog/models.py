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
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = '4. Tags'

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    content = models.TextField()
    featured_image = models.ImageField(
        upload_to='posts/featured_images/%Y/%m/%d/')
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Each post can recieve likes from multiple users and each users can like multiple posts
    likes = models.ManyToManyField(User, related_name='post_likes')

    # Each post belong to one user one category
    category = models.ForeignKey(Category, 
                                 on_delete=models.SET_NULL,
                                 null=True)
    # Each post can have multiple tags and each tag can be used in multiple posts
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = '5. Posts'

    def __str__(self):
        return self.title
    
    def get_number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    # Each comment can recieve likes from multiple users and each users can like multiple comments
    likes = models.ManyToManyField(User, related_name='comment_likes')

    # Each comment belong to one user and one post
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = '6. Comments'

    def __str__(self):
        if len(self.content) > 50:
            comment = self.content[:50] + '...'
        else:
            comment = self.content
        return comment
    
    def get_number_of_likes(self):
        return self.likes.count()
