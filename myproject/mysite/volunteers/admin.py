from django.contrib import admin
from .models import Volunteer

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'inn', 'rank', 'bonus_points', 'get_rank_group_display')
    list_filter = ('rank',)  # Фильтруем по реальному полю rank
    search_fields = ('full_name', 'inn', 'email')
    ordering = ('rank',)

    def get_rank_group_display(self, obj):
        return obj.rank_group
    get_rank_group_display.short_description = 'Группа'
