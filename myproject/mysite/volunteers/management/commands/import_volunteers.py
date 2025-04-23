import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from volunteers.models import Volunteer

def fix_invalid_date(date_str):
    """Исправляет некорректные даты (31.06 -> 30.06)"""
    try:
        return datetime.strptime(date_str, '%d.%m.%Y').date()
    except ValueError:
        day, month, year = map(int, date_str.split('.'))

        # Исправляем день, если он превышает количество дней в месяце
        if month == 2:
            max_day = 28 if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) else 29
        elif month in [4, 6, 9, 11]:
            max_day = 30
        else:
            max_day = 31

        fixed_day = min(day, max_day)
        fixed_date = f"{fixed_day:02d}.{month:02d}.{year}"
        return datetime.strptime(fixed_date, '%d.%m.%Y').date()

class Command(BaseCommand):
    help = 'Import volunteers from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        success_count = 0
        error_count = 0

        try:
            with open(options['csv_file'], mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for i, row in enumerate(reader, 1):
                    try:
                        # Обработка и исправление даты
                        original_date = row['Дата рождения'].strip()
                        birth_date = fix_invalid_date(original_date)

                        # Логирование исправленных дат
                        if original_date != birth_date.strftime('%d.%m.%Y'):
                            self.stdout.write(self.style.WARNING(
                                f"Строка {i}: Исправлена дата {original_date} -> {birth_date.strftime('%d.%m.%Y')}"
                            ))

                        Volunteer.objects.update_or_create(
                            inn=row['ИНН'],
                            defaults={
                                'full_name': row['ФИО'].strip(),
                                'phone': row['Номер телефона'].replace(' ', ''),
                                'email': row['Электронная почта'].strip(),
                                'birth_date': birth_date,
                                'achievements': row['Достижения'].strip(),
                                'rank': i
                            }
                        )
                        success_count += 1
                    except Exception as e:
                        error_count += 1
                        self.stdout.write(self.style.ERROR(
                            f"Строка {i}: Ошибка '{str(e)}'. Данные: {row}"
                        ))
                        continue

            self.stdout.write(self.style.SUCCESS(
                f"Импорт завершен. Успешно: {success_count}, с ошибками: {error_count}"
            ))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при открытии файла: {str(e)}'))
