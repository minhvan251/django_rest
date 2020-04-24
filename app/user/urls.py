from .views import UserCreateView
from django.urls import path

app_name = 'user'


urlpatterns = [
    path('', UserCreateView.as_view(), name='create')
]
