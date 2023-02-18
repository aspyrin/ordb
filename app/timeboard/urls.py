from django.urls import path
from timeboard import views


app_name = 'timeboard'
urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    path('', views.IndexView.as_view(), name='index'),
]

