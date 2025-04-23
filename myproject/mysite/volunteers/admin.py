from django.contrib import admin
from .models import User, Volunteer, Partner, Bonus, BonusHistory

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_volunteer', 'is_partner']

admin.site.register(Volunteer)
admin.site.register(Partner)
admin.site.register(Bonus)
admin.site.register(BonusHistory)
