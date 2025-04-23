from django.contrib import admin
from django.urls import path
from volunteers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.leaderboard, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
    path('import/', views.import_data, name='import'),
]
