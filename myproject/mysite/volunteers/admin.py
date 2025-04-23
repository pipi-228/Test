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
