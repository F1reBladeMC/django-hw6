from django.db import models

# Create your models here.

class MyInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    photo = models.ImageField(upload_to='photos/', verbose_name="Фото")
    profession = models.CharField(max_length=100, verbose_name="Профессия")
    age = models.IntegerField(verbose_name="Возраст")
    
    class Meta:
        verbose_name = "Моя информация"
        verbose_name_plural = "Моя информация"


class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название компании")
    about = models.TextField(verbose_name="О компании")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=300, verbose_name="Адрес")
    working_hours = models.CharField(max_length=100, verbose_name="Часы работы")
    
    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компаниях"