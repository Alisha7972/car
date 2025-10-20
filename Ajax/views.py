from django.http import HttpResponse
from django.shortcuts import render

def Ajax(request):
    return render(request, 'Ajax/Ajax.html')

# Create your views here.
