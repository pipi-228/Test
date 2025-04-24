from django.db import models
from django.contrib.auth.models import AbstractUser

"""User Наследуется от AbstractUser, что даёт стандартную систему авторизации Django.

Добавлены флаги: is_volunteer, is_partner, is_admin — чтобы различать типы пользователей.

"""
class User(AbstractUser):
    is_volunteer = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

"""Volunteer Связан один к одному с User. Один пользователь = один волонтёр.

Поля:

full_name, inn, phone, email, birth_date, achievements

category: категория волонтёра (по очкам или активности)

unique_code: уникальный код (возможно, как идентификатор или для бонусов)"""
class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=100)
    inn = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    birth_date = models.DateField()
    achievements = models.TextField()
    category = models.IntegerField(choices=[(1, '1-50'), (2, '51-100'), (3, '101-150')])
    unique_code = models.CharField(max_length=20, unique=True)

"""Partner Также связан один к одному с User.

Поля:

company_name, contact_person, phone, email"""
class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

"""Bonus Связан с Partner (многие бонусы могут принадлежать одному партнёру).

Поля:

name, description

category_available: для какой категории волонтёров бонус доступен

valid_from, valid_to: период действия

is_active: активен ли бонус"""
class Bonus(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category_available = models.IntegerField(choices=[(1, '1-50'), (2, '51-100'), (3, '101-150')])
    valid_from = models.DateField()
    valid_to = models.DateField()
    is_active = models.BooleanField(default=True)

class BonusHistory(models.Model): #Журнал, фиксирующий, кто (волонтёр) использовал какой бонус, у какого партнёра, и когда.
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(auto_now_add=True)
    code_used = models.CharField(max_length=20)
