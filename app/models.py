from django.db import models
from phone_field import PhoneField
from django.db.models.deletion import CASCADE


class Group(models.Model):
    photo = models.ImageField(upload_to='images')
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'

class Course(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to = 'images')

    def __str__(self) -> str:
        return f'{self.title}'
    
    @property
    def short_desc(self):
        if len(self.description) >= 50:
            return self.description[0:40] + '...'
        else:
            return self.description


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = PhoneField(max_length=12)
    email = models.EmailField()
    group_course = models.CharField(max_length=50)
    message = models.TextField(max_length=3000)
