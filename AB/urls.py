from django.urls import path
from .views import *

urlpatterns = [
    path("", bb, name="bb"),
    path("1", cc, name="cc"),
    path("2", dd, name="dd"),
    path("3/<str:pk>", ss.as_view(), name="ss"),
    path("4/<str:pk>", yy.as_view(), name="yy"),
]
