from django.shortcuts import render
from rest_framework import generics, viewsets

from mango.models import Request, Portfolio
from mango.serializers import RequestSerializer, PortfolioSerializer


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
    portfolios = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfolios, many=True)
    return render(request, "portfolio.html", {"portfolio": serializer.data})

def portfolio_detail(request, id):
    portfolio = Portfolio.objects.get(id=id)

    serializer = PortfolioSerializer(portfolio)
    return render(
        request,
        "portfolio-detail.html",
        {"portfolio": serializer.data},
    )

class RequestView(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
