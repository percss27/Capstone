from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginPage, name="login"),
    path('homepage/',views.HomePage, name="homepage"),
    path('signup/',views.SignUp, name="signup"),
]
