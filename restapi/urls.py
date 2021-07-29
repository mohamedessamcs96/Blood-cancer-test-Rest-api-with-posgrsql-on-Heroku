from django.urls import path

from .views import userList
from . import views
urlpatterns = [
    
    path('users/',userList.as_view()),
    path('',views.home),
]