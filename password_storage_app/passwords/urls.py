from django.urls import path
from . import views

urlpatterns = [
    path('passwords/', views.home_page, name='passwords'),

    # user account
    # path('register/', views.register_page, name="register-page"),
    # path('login/', views.login_page, name="login-page"),
    # path('logged_out/', views.logged_out_page, name="logged_out-page")
]
