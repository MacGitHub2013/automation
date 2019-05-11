from django.db import models

# Create your models here.


class CodeBank(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    code = models.TextField(max_length=1000)
    link = models.URLField(max_length=200, null=True, blank=True)
    tags = models.TextField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
