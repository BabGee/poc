from django.shortcuts import render
from administration.models import Gateway


def iic_editor_home(request):
    context = {
        'gateways': Gateway.objects.all()
    }
    return render(request, 'admin/app_index.html', context)


def gateway_details(request, slug):
    gateway = Gateway.objects.get(slug=slug)
    context = {
        'gateway': gateway,
        'gatewayhosts': gateway.hosts.all()
    }
    return render(request, 'admin/gateway_details.html', context)
