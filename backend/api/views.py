from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request, *args, **kwargs):
    return HttpResponse("Helloworld")

