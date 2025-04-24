from django.shortcuts import render, redirect
from django.contrib import messages
import csv
from io import TextIOWrapper
from datetime import datetime
from .models import Volunteer

def import_volunteers(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = TextIOWrapper(
            request.FILES['csv_file'].file,
            encoding='utf-8-sig'
        )
        reader = csv.DictReader(csv_file)
        total_imported = 0
        
        for i, row in enumerate(reader):
            try:
                if i < 50:
                    category = 'A'
                elif i < 100:
                    category = 'B'
                else:
                    category = 'C'
                
                birth_date = datetime.strptime(
                    row['Дата рождения'], 
                    '%d.%m.%Y'
                ).date()
                
                Volunteer.objects.create(
                    full_name=row['ФИО'],
                    inn=row['ИНН'],
                    phone=row['Номер телефона'],
                    email=row['Электронная почта'],
                    birth_date=birth_date,
                    achievements=row['Достижения'],
                    category=category
                )
                total_imported += 1
            
            except Exception as e:
                messages.error(
                    request,
                    f'Ошибка в строке {i+1}: {str(e)}'
                )
        
        messages.success(
            request,
            f'Успешно импортировано {total_imported} волонтеров'
        )
        return redirect('admin:volunteers_volunteer_changelist')
    
    return render(request, 'admin/import_volunteers.html')