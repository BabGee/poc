from django.db import models


class PageGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PageGroupPage(models.Model):
    name = models.CharField(max_length=100)
    item_level = models.IntegerField()
    page_group = models.ForeignKey(PageGroup, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
