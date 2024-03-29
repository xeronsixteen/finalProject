from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accounts.views import RegisterView, UserDetailView, ChangeProfileView, ChangePasswordView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('<int:pk>/', UserDetailView.as_view(), name='profile'),
    # path('users/', UsersView.as_view(), name='UsersView'),
    # path('change/', ChangeProfileView.as_view(), name='change_profile'),
    # path('change/password/', ChangePasswordView.as_view(), name='change_password'),


]
