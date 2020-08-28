from django.urls import path
from . import views
import _json
urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('checkusername', views.check_username_exist, name="checkusername"),
    path('checkemail', views.check_checkemail_exist, name="checkemail"),
    path('checkpassword', views.check_checkpassword_exist, name="checkpassword"),
    path('verify-user', views.verify_user, name="verify-user"),
    path('user-verified', views.user_verified, name="user-verified"),
    #passowrd verification
    path('forgetPass-link', views.forgetPass_link, name="forgetPass-link"),
    path('verify-forgetpassword', views.verify_forgetpassword, name="verify-forgetpassword"),
    path('verified-forgetpassword', views.verified_forgetpassword, name="verified-forgetpassword"),
    path('password-updated', views.password_updated, name="password-updated"),
]
