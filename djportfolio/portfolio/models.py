from django.db import models
import datetime
import json

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField()
    slug = models.SlugField()
    webpage = models.CharField(max_length=255, blank=True, null=True )
    img = models.ImageField(upload_to='uploads/',blank=True, null=True)
    year = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    stack = models.CharField(max_length=2000, blank=True, null=True)

    def set_stack(self, x):
        self.stack = json.dumps(x)

    def get_stack(self):
        return json.loads(self.stack)

    def get_stack_line(self):
        obj = json.loads(self.stack)
        result = ""
        if(type(obj) is list):
            result = ' '.join(obj)
        return result

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}/'

    def get_image(self):
        if self.img:
            return  self.img.url
        return ''

    class Meta:
        ordering = ('-year',) #change for creation date
