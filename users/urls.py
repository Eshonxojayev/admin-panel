from django.urls import path
from .views import UserLoginView, UserRegisterView, UserListView, UserDetailView, UserSettingsView, LogOutView

# app_name = "users"
urlpatterns = [
    # auth
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("users/", UserListView.as_view(), name="users"),
    path("users/<int:id>/", UserDetailView.as_view(), name="users-detail"),
    path("settings/<int:id>/", UserSettingsView.as_view(), name="settings"),
]