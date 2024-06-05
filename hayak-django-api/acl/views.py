from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Role, Permission

def roles(request):
    roles = Role.objects.all().values()
    template = loader.get_template('roles/index.html')
    context = {
        'roles': roles,
    }
    return HttpResponse(template.render(context, request))

def permissions(request):
    permissions = Permission.objects.all().values()
    template = loader.get_template('permissions/index.html')
    context = {
        'permissions': permissions,
    }
    return HttpResponse(template.render(context, request))
