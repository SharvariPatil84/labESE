from django.contrib import admin
from django.urls import include, path
from home import views


urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="handleregister"),
    path('log', views.log, name="handlelog"),
    path('signup', views.handleSign, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('contact', views.contact, name="contact"),
    # path('/', include('blog.urls'))
]