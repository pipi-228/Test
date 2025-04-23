from django.contrib import admin
from django import forms
from .models import Volunteer

"""class VolunteerAdminForm(forms.ModelForm):
    manual_bonuses = forms.IntegerField(
        label='Бонусы (ручной ввод)',
        required=False,
        help_text='Введите количество бонусов для ручного начисления'
    )

    class Meta:
        model = Volunteer
        fields = '__all__' """

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    #form = VolunteerAdminForm
    list_display = ('rank', 'full_name', 'inn', 'birth_date', 'achievements_short')
    list_display_links = ('rank', 'full_name')
    list_filter = ('rank',)
    search_fields = ('full_name', 'inn', 'email')
    list_per_page = 200
    ordering = ('rank',)
    
    def achievements_short(self, obj):
        return obj.achievements[:50] + "..." if len(obj.achievements) > 50 else obj.achievements
    achievements_short.short_description = 'Достижения'
    
    """
    def manual_bonuses_display(self, obj):
        # Здесь можно добавить логику вычисления бонусов
        # Пока просто возвращаем поле для ручного ввода
        return obj.bonus_points  # Или другое поле, куда сохраняются бонусы
    manual_bonuses_display.short_description = 'Бонусы'
    
    def save_model(self, request, obj, form, change):
        # Сохраняем ручной ввод бонусов
        if 'manual_bonuses' in form.cleaned_data:
            obj.bonus_points = form.cleaned_data['manual_bonuses']
        super().save_model(request, obj, form, change)
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        # Добавляем поле для ручного ввода бонусов в форму редактирования
        return fieldsets + [
            ('Ручное начисление бонусов', {
                'fields': ['manual_bonuses'],
                'classes': ('collapse',)
            }),
        ]
    

from django.contrib import admin
from .models import Volunteer

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('rank', 'full_name', 'inn', 'birth_date', 'achievements_short', 'bonus_points')
    list_display_links = ('rank', 'full_name')
    list_filter = ('rank',)
    search_fields = ('full_name', 'inn', 'email')
    list_per_page = 200  # Увеличиваем количество записей на странице
    ordering = ('rank',)  # Сортировка по рангу по умолчанию

    def achievements_short(self, obj):
        return obj.achievements[:50] + "..." if len(obj.achievements) > 50 else obj.achievements
    achievements_short.short_description = 'Достижения'
    
    # Добавляем action для админки
    actions = ['reset_bonus_points']
    
    def reset_bonus_points(self, request, queryset):
        queryset.update(bonus_points=0)
    reset_bonus_points.short_description = "Обнулить бонусные баллы"
"""