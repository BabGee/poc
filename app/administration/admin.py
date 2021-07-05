from django.contrib import admin
from .models import Gateway, Host


class GatewayAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Gateway, GatewayAdmin)
admin.site.register(Host)
