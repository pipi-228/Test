from django.contrib import admin
from .models import User, Volunteer, Partner, Bonus, BonusHistory

@admin.register(User) #декоратор, который регистрирует модель User с кастомной настройкой UserAdmin.
class UserAdmin(admin.ModelAdmin): #класс, наследующий от admin.ModelAdmin, в котором ты настраиваешь поведение модели User в админке.
    list_display = ['username', 'email', 'is_volunteer', 'is_partner'] #указывает, какие поля будут отображаться в списке объектов в админке (в виде колонок таблицы).

#регистрируются без кастомного админ-класса, т.е. будут отображаться в админке с настройками по умолчанию.
admin.site.register(Volunteer)
admin.site.register(Partner)
admin.site.register(Bonus)
admin.site.register(BonusHistory)
