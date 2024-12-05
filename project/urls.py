from django.urls import path
from contact.views import views

urlpatterns = [
    path('', views.index,),
]
