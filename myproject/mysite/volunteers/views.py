from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

@login_required
def volunteer_dashboard(request):
    if not request.user.is_volunteer:
        return redirect('login')
    return render(request, 'volunteers/dashboard.html', {
        'user': request.user
    })

@login_required
def partner_dashboard(request):
    if not request.user.is_partner:
        return redirect('login')
    return render(request, 'partners/dashboard.html', {
        'user': request.user
    })

class RedirectAfterLoginView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_volunteer:
            return redirect('volunteer_dashboard')
        elif request.user.is_partner:
            return redirect('partner_dashboard')
        elif request.user.is_superuser:
            return redirect('/admin/')
        return redirect('home')
