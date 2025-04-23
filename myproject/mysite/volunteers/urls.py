from django.urls import path
from . import views

urlpatterns = [
    path('volunteer/dashboard/', views.volunteer_dashboard, name='volunteer_dashboard'),
    path('partner/dashboard/', views.partner_dashboard, name='partner_dashboard'),
    path('accounts/profile/', views.RedirectAfterLoginView.as_view(), name='login_redirect'),
    # ... остальные URL ...
]
