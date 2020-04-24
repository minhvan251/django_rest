from .views import UserCreateView, CreateTokenView, my_view, UserUpdateView
from django.urls import path

app_name = 'user'


urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('', my_view, name='test'),
]
