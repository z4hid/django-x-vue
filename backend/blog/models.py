from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo/')

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = '1. Site'

    def __str__(self):
        return self.name
    
