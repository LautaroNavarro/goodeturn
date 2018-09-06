from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def create_event(request):
	return render(request,'create_event.html')

def view_event(request):
	return render(request,'view_event.html')