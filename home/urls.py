from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.login,name='login'),              #for login page
    path('signin',views.signin,name='signIN'),
    path('sign_up',views.signuppage,name='signUP'), #for signup page
    path('signup',views.signup,name='signup'),
    path('reset_page',views.reset_page,name='reset_page'), #for reset page
    path('reset_pass',views.reset_pass,name='reset_pass'),
]