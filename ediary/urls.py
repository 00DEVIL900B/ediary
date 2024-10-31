"""
URL configuration for ediary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.signin, name="login"),
    path('help/', views.help, name="help"),
    path('signup/', views.signup, name="signup"),
    path('handleSignup', views.handleSignup, name="handleSignup"),
    path('handleLogin', views.handleLogin, name="handleLogin"),
    path('changePassword/', views.changePass, name="changePassword"),
    path('404/', views.error, name='error'),
    path('logout/', views.signout, name='logout'),
    path('diary/', include('diary.urls'), name="udiary"),
    # password reset link on email
    path("reset-password/", auth_views.PasswordResetView.as_view(template_name="pass/reset_password.html"), name="pass_reset"),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name="pass/mail_sent.html"), name="password_reset_done"),
    # check token and set new password
    path("reset-password/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="pass/new_password.html"), name="password_reset_confirm"),
    path("reset-password-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="pass/pass_changed.html"), name="password_reset_complete"),
]
