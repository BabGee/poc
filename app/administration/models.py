from django.db import models
from django.shortcuts import reverse
from iic.models import PageGroupPage


class Host(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gateway(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    hosts = models.ManyToManyField(Host)
    pagegrouppage = models.ForeignKey(PageGroupPage, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gateway-details', kwargs={
            'slug': self.slug})
