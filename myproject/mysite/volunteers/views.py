from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Volunteer

def leaderboard(request):
    volunteers = Volunteer.objects.all().order_by('rank')
    context = {
        'volunteers': volunteers,
        'top_50': volunteers.filter(rank__lte=50),
        'top_100': volunteers.filter(rank__range=(51, 100)),
        'top_150': volunteers.filter(rank__range=(101, 150))
    }
    return render(request, 'volunteers/leaderboard.html', context)

@login_required
def profile(request):
    volunteer = request.user.volunteer
    return render(request, 'volunteers/profile.html', {'volunteer': volunteer})

def import_data(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        # Обработка загрузки файла
        pass
    return render(request, 'volunteers/import.html')
