from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_volunteer = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

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

class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

class Bonus(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category_available = models.IntegerField(choices=[(1, '1-50'), (2, '51-100'), (3, '101-150')])
    valid_from = models.DateField()
    valid_to = models.DateField()
    is_active = models.BooleanField(default=True)

class BonusHistory(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(auto_now_add=True)
    code_used = models.CharField(max_length=20)
