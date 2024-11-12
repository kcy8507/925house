from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets, filters
from rest_framework.decorators import action
from django.db.models import F, Value, Q
from django.core.paginator import Paginator


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

# def contact02(request):
#     return render(request, "contact02.html")

# def contact03(request):
#     return render(request, "contact03.html")

# def contact04(request):
#     return render(request, "contact04.html")

# def contact05(request):
#     return render(request, "contact05.html")

def portfolio(request):
    return render(request, "portfolio.html")
