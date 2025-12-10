# birthday/models.py
from django.db import models


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', max_length=20, help_text='Необязательное поле', blank=True
    )
    birthday = models.DateField('Дата рождения')
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)