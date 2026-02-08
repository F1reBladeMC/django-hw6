from django.shortcuts import render
from .models import MyInfo, CompanyInfo

# Create your views here.

def base_view(request):
    my_info = MyInfo.objects.first()
    context = {
        'my_info': my_info
    }
    return render(request, 'base.html', context)

def homepage_view(request):
    context = {
        'title': 'Добро пожаловать',
        'greeting': 'Добро пожаловать на наш сайт!'
    }
    return render(request, 'homepage.html', context)

def urmat_view(request):
    company_info = CompanyInfo.objects.first()
    context = {
        'company_info': company_info
    }
    return render(request, 'urmat.html', context)

def sierra_view(request):
    company_info = CompanyInfo.objects.first()
    context = {
        'company_info': company_info
    }
    return render(request, 'sierra.html', context)