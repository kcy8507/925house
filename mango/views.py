from django.shortcuts import render
from rest_framework import generics, viewsets

from mango.models import Request
from mango.serializers import RequestSerializer


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

class RequestView(
    generics.ListAPIView,
    generics.RetrieveAPIView,
    generics.CreateAPIView,
    generics.UpdateAPIView,
    viewsets.GenericViewSet,
):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
