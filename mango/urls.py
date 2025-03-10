from django.urls import path
from rest_framework.routers import SimpleRouter

from mango.views import (
    index, about, service, contact,
    # contact02, contact03, contact04, contact05,
    portfolio, portfolio_detail, RequestView
)

router = SimpleRouter()
router.register("request", RequestView)
urlpatterns = router.get_urls()
urlpatterns += [
    path("", index, name="index"),
    path("about", about, name="about"),
    path("service", service, name="service"),
    path("contact", contact, name="contact"),
    # path("contact02", contact02, name="contact02"),
    # path("contact03", contact03, name="contact03"),
    # path("contact04", contact04, name="contact04"),
    # path("contact05", contact05, name="contact05"),
    path("portfolio", portfolio, name="portfolio"),
    path("portfolio/<int:id>", portfolio_detail, name="portfolio_detail"),
]