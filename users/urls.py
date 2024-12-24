from django.urls import path
from .views import LoginUserView, CreateUserView, LogoutUserView, UpdateUserView


urlpatterns = [
    path('events/login/', LoginUserView.as_view(), name='login_user_view'),
    path('events/register/', CreateUserView.as_view(), name='register_user_view'),
    path('events/logout/', LogoutUserView.as_view(), name='logout_user_view'),
    path('events/profile/', UpdateUserView.as_view(), name='update_user_view'),
]
