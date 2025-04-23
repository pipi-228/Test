import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from volunteers.models import Volunteer

class Command(BaseCommand):
    help = 'Импорт волонтёров из CSV файла'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Путь к CSV файлу')

    def handle(self, *args, **options):
        with open(options['file_path'], mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Volunteer.objects.update_or_create(
                    inn=row['ИНН'],
                    defaults={
                        'full_name': row['ФИО'],
                        'phone': row['Номер телефона'],
                        'email': row['Электронная почта'],
                        'birth_date': datetime.strptime(row['Дата рождения'], '%d.%m.%Y').date(),
                        'achievements': row['Достижения'],
                        'rank': int(row.get('Место в рейтинге', 1))
                    }
                )
        self.stdout.write(self.style.SUCCESS(f'Успешно импортировано {Volunteer.objects.count()} волонтёров'))
