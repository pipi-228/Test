from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Volunteer, Partner, Bonus

class VolunteerSignUpForm(UserCreationForm):
    # Дополнительные поля для волонтера
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100)
    inn = forms.CharField(max_length=12)  # ИНН как уникальный идентификатор
    phone = forms.CharField(max_length=15)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Календарь для выбора даты
    achievements = forms.CharField(widget=forms.Textarea)  # Большое текстовое поле для достижений

    class Meta:
        model = User  # Основная модель пользователя
        fields = ['username', 'email', 'password1', 'password2']  # Стандартные поля UserCreationForm

    def save(self, commit=True):
        """
        Переопределенный метод сохранения:
        1. Создает пользователя через родительский класс
        2. Помечает его как волонтера
        3. Создает связанную запись Volunteer с дополнительными данными
        """
        user = super().save(commit=False)  # Создаем пользователя без сохранения в БД
        user.is_volunteer = True  # Устанавливаем флаг волонтера
        user.save()  # Сохраняем пользователя
        
        # Создаем профиль волонтера
        Volunteer.objects.create(
            user=user,  # Связь с пользователем
            full_name=self.cleaned_data['full_name'],
            inn=self.cleaned_data['inn'],
            phone=self.cleaned_data['phone'],
            email=self.cleaned_data['email'],
            birth_date=self.cleaned_data['birth_date'],
            achievements=self.cleaned_data['achievements'],
            category=1,  # Категория по умолчанию (можно изменить логику)
            unique_code=f"VOL-{user.id}-{self.cleaned_data['inn'][-4:]}"  # Генерация уникального кода
        )
        return user

class PartnerSignUpForm(UserCreationForm):
    # Дополнительные поля для партнера
    company_name = forms.CharField(max_length=100)  # Название компании
    contact_person = forms.CharField(max_length=100)  # Контактное лицо
    phone = forms.CharField(max_length=15)  # Телефон
    email = forms.EmailField()  # Email

    class Meta:
        model = User  # Основная модель пользователя
        fields = ['username', 'email', 'password1', 'password2']  # Стандартные поля

    def save(self, commit=True):
        """
        Метод сохранения для партнера:
        1. Создает пользователя
        2. Помечает его как партнера
        3. Создает связанную запись Partner
        """
        user = super().save(commit=False)
        user.is_partner = True  # Устанавливаем флаг партнера
        user.save()
        
        # Создаем профиль партнера
        Partner.objects.create(
            user=user,
            company_name=self.cleaned_data['company_name'],
            contact_person=self.cleaned_data['contact_person'],
            phone=self.cleaned_data['phone'],
            email=self.cleaned_data['email']
        )
        return user

class BonusForm(forms.ModelForm):
    """
    Форма для создания/редактирования бонусов, которые партнеры могут предлагать волонтерам.
    Наследуется от ModelForm для автоматического создания формы на основе модели Bonus.
    """
    class Meta:
        model = Bonus  # Модель, на основе которой создается форма
        fields = ['name', 'description', 'category_available', 'valid_from', 'valid_to']
        # Поля формы:
        # - name: название бонуса
        # - description: описание
        # - category_available: для каких категорий волонтеров доступен
        # - valid_from/valid_to: срок действия бонуса