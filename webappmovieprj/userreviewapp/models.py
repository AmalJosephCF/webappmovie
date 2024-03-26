from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Reviews(models.Model):
    desc=models.TextField(blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    uname = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ('uname',)
        verbose_name = 'review'
        verbose_name_plural = 'review'

    def __str__(self):
        return '{}'.format(self.uname)