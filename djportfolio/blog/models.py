from django.db import models
from django.conf import settings
from django.conf.urls.static import static

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField()
    img = models.ImageField(upload_to='uploads/',blank=True, null=True)
    author = models.CharField(max_length=255, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-created',) #change for creation date

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.id}/'

    def get_image(self):
        if self.img:
            return self.img.url
        return ''
