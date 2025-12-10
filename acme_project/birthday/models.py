from django.db import models
from django.urls import reverse

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', max_length=20, help_text='Необязательное поле', blank=True
    )
    birthday = models.DateField('Дата рождения')
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)

    def get_absolute_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.pk}) 