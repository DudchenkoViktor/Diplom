from django.db import models

class Specializations(models.Model):
    name_spec = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = 'specialization'
        ordering = ['id',]

    def __str__(self):
        return self.name_spec


class Complaints(models.Model):
    name_complaint = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = 'complaint'

    def __str__(self):
        return self.name_complaint

class TeachersComplaints(models.Model):
    complaint = models.ForeignKey(Complaints, on_delete=models.CASCADE)
    teacher_name = models.ForeignKey('users.Teacher_profile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

