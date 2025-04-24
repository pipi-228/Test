from django.contrib.auth.decorators import login_required
from .models import Vol
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def leaderboard(request):
    volunteers = Vol.objects.all().order_by('rank')
    context={
        'volunteers':volunteers,
        'top_50': volunteers.filter(rank__lte=50),
        'top_100': volunteers.filter(rank__range=(51,100)),
        'top_150': volunteers.filter(rank__range=(101,150))
            }
    return render(request, '_leaderboard.html')
