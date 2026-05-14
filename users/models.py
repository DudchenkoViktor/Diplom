from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser
from teachers.models import Specializations

class Locations(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'location'
        ordering = ['name', ]

    def __str__(self):
        return self.name

class Mode_teaching(models.Model):
    name_mode = models.CharField(max_length=20, verbose_name='mode_teaching')

    class Meta:
        db_table = 'mode_of_teaching'

    def __str__(self):
        return self.name_mode


class Teacher_profile(AbstractUser):

    username = models.CharField(unique=True, max_length=50, verbose_name='identifier')
    age = models.CharField(null=True, blank=True)
    experience = models.CharField(null=True, blank=True)
    phone = models.CharField(verbose_name='phone number', blank=True, null=True)
    slug = AutoSlugField(populate_from='get_full_name', unique=True, always_update=True, blank=True, null=True)

    info_about_teacher = models.TextField(null=True, blank=True)
    work_experience = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    other_specialities = models.TextField(null=True, blank=True)

    locations = models.ForeignKey(to=Locations, blank=True, null=True, on_delete=models.PROTECT)
    main_specialty = models.ForeignKey(to=Specializations, blank=True, null=True, on_delete=models.PROTECT)
    mode_teaching = models.ForeignKey(to=Mode_teaching, blank=True, null=True, on_delete=models.PROTECT)

    image = models.ImageField(upload_to='users_image', blank=True, null=True)

    class Meta:
        db_table = 'info_teacher'
        ordering = ('id',)

    def get_full_name(self):
        return f"{self.last_name}-{self.first_name}-{self.username}"

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
