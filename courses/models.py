from django.db import models

CATEGORY = [
    (1, 'Language courses'),
    (2, 'culinarnye courses'),
    (3, 'vojdenie courses'),
    (4, 'programming courses')
]

CONTACT = [
    (1, 'phone'),
    (2, 'email'),
    (3, 'facebook')
]

class Category(models.Model):
    name = models.IntegerField(choices=CATEGORY)
    impath = models.CharField(verbose_name='Imapath', max_length=20)


class Branch(models.Model):
    latitude = models.CharField(verbose_name='Latitude', max_length=64)
    longitude = models.CharField(verbose_name='Longitude', max_length=64)
    adress = models.CharField(verbose_name='Adress', max_length=128)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Branch', related_name='branches')


class Contact(models.Model):
    type = models.IntegerField(choices=CONTACT, verbose_name='Variants', null=True, blank=True)
    value = models.CharField(max_length=64)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Contacts', related_name='contacts')


class Course(models.Model):
    name = models.CharField(verbose_name='Name', max_length=128)
    description = models.TextField(verbose_name='Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
