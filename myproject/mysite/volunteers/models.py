from django.db import models
from django.core.validators import MinValueValidator

class Volunteer(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    inn = models.BigIntegerField("ИНН", unique=True)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email")
    birth_date = models.DateField("Дата рождения")
    achievements = models.TextField("Достижения")
    rank = models.IntegerField(
        "Место в рейтинге",
        validators=[MinValueValidator(1)],
        default=1
    )
    bonus_points = models.IntegerField("Бонусные баллы", default=0)

    @property
    def rank_group(self):
        if self.rank <= 50:
            return "Топ 1-50"
        elif self.rank <= 100:
            return "Топ 51-100"
        elif self.rank <= 150:
            return "Топ 101-150"
        return "Участник"

    def __str__(self):
        return f"{self.full_name} (ИНН: {self.inn})"

    class Meta:
        verbose_name = "Волонтёр"
        verbose_name_plural = "Волонтёры"
        ordering = ['rank']
