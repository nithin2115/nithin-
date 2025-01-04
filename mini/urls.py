from django.urls import path
from mini import views
urlpatterns=[
    path('',views.home,name="homepage"),
    path('login',views.loginview,name="loginpage"),
    path('register',views.register,name="registerpage"),
    path('profile',views.profile,name="profilepage"),
    path('single',views.single,name="singlepage"),
    path('create',views.create,name="createpage"),
    path('display/<int:rid>',views.displaypage,name='displaypage'),
    path('logout',views.logoutview,name="logoutpage"),
]