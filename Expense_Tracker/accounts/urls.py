from django.urls import path
from . import views  # ✅ Import the whole views module

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup, name="signup"),  # ✅ Now views.signup is accessible
]
