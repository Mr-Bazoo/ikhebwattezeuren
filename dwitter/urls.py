from django.urls import path
from .views import dashboard, profile_list, profile, like_post
from . import views

app_name = "dwitter"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('like/', like_post, name='like-post'),
]
