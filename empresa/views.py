from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def nova_empresa(request):
    return render(request, 'nova_empresa.html')