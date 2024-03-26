from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('movieapp:movies_by_category',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)

class Movie(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    cast = models.TextField()
    trailer = models.TextField()
    rel_date = models.DateField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='movie',blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_url(self):
        return reverse('movieapp:movDetail',args=[self.category.slug,self.slug])
    class Meta:
        ordering = ('name',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return '{}'.format(self.name)