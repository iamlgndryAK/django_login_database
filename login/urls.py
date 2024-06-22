from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
]
