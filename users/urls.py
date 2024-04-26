from django.urls import path
from .views import LoginUserView, CreateUserView, LogoutUserView


urlpatterns = [
    path('events/login/', LoginUserView.as_view(), name='login_view'),
    path('events/register/', CreateUserView.as_view(), name='register_view'),
    path('events/logout/', LogoutUserView.as_view(), name='logout_view'),
]
