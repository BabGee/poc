from django.contrib import admin
from django.urls import path
from administration.models import Gateway
from .models import PageGroup, PageGroupPage
from django.shortcuts import render
from django.db import models


# my dummy model
class IICEditor(models.Model):
    class Meta:
        verbose_name_plural = 'IIC Editor'
        app_label = 'iic'


def iic_editor_view(request):
    context = {
        'gateways': Gateway.objects.all()
    }
    return render(request, 'admin/app_index.html', context)


class IICEditorAdmin(admin.ModelAdmin):
    model = IICEditor

    def get_urls(self):
        view_name = f'{self.model._meta.app_label}_{self.model._meta.model_name}_changelist'
        return [
            path('iiceditor/', iic_editor_view, name=view_name),
        ]


admin.site.register(IICEditor, IICEditorAdmin)
admin.site.register(PageGroup)
admin.site.register(PageGroupPage)
