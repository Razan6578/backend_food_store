from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Номер телефону неправильний"
)


class User(models.Model):
    phone_number = models.CharField(validators=[phone_validator], max_length=17)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email