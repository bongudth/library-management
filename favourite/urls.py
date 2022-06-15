from django.urls import path

from . import views

app_name = 'favourite'

urlpatterns = [
    path('', views.book_favourite, name='book_favourite'),
]