import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from volunteers.models import User, Volunteer
from django.db.utils import IntegrityError
import uuid

class Command(BaseCommand):
    help = 'Импорт волонтёров из CSV файла'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Путь к CSV файлу')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        total_imported = 0
        date_errors = 0
        code_conflicts = 0

        with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)

            for i, row in enumerate(reader, 1):
                if not row['ФИО'] or not row['ИНН']:
                    continue

                # Проверка и преобразование даты
                try:
                    birth_date = datetime.strptime(row['Дата рождения'], '%d.%m.%Y').date()
                except ValueError:
                    date_errors += 1
                    self.stdout.write(self.style.ERROR(
                        f'Ошибка даты: {row["ФИО"]} - {row["Дата рождения"]}'))
                    continue

                # Определение категории
                category = 1 if i <= 50 else (2 if i <= 100 else 3)

                # Генерация уникального кода с добавлением UUID
                base_code = f"VOL-{row['ИНН'][-6:]}"
                unique_code = f"{base_code}-{uuid.uuid4().hex[:4]}"

                try:
                    # Создание пользователя
                    username = f"volunteer_{row['ИНН']}_{i}"
                    user = User.objects.create_user(
                        username=username,
                        password=str(uuid.uuid4()),  # Генерация случайного пароля
                        is_volunteer=True
                    )

                    # Создание волонтера
                    Volunteer.objects.create(
                        user=user,
                        full_name=row['ФИО'],
                        inn=row['ИНН'],
                        phone=row['Номер телефона'],
                        email=row['Электронная почта'],
                        birth_date=birth_date,
                        achievements=row['Достижения'],
                        category=category,
                        unique_code=unique_code
                    )

                    total_imported += 1

                except IntegrityError as e:
                    code_conflicts += 1
                    self.stdout.write(self.style.ERROR(
                        f'Конфликт данных: {row["ФИО"]} - {str(e)}'))
                    continue

        # Итоговый отчет
        self.stdout.write(self.style.SUCCESS(
            f'Импорт завершен. Успешно: {total_imported}, '
            f'Ошибок даты: {date_errors}, '
            f'Конфликтов уникальности: {code_conflicts}'))

        # Предупреждение о static files (можно игнорировать во время разработки)
        self.stdout.write(self.style.WARNING(
            'Предупреждение о static files не влияет на работу импорта'))
