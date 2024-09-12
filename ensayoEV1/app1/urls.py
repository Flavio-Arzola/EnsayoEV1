from django.urls import path
from . import views

urlpatterns = [
    path('display1/', views.display, name='display1'),
    path("display2/", views.display2, name="display2"),
]