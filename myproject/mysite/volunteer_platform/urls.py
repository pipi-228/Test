from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from volunteers import views

urlpatterns = [
    # Главная страница (перенаправление на логин)
    path('', RedirectView.as_view(url='/login/'), name='home'),

    # Админка
    path('admin/', admin.site.urls),

    # Авторизация
    path('login/', auth_views.LoginView.as_view(template_name='volunteers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URL приложения volunteers
    path('', include('volunteers.urls')),
]
