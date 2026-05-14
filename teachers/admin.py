from django.contrib import admin

from teachers.models import Specializations, Complaints, TeachersComplaints

# admin.site.register(Specializations)

@admin.register(Specializations)
class SpecializationsAdmin(admin.ModelAdmin):
    list_display = ('name_spec',)

@admin.register(Complaints)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('name_complaint',)

@admin.register(TeachersComplaints)
class TeachersComplaintsAdmin(admin.ModelAdmin):
    list_display = ('complaint', 'teacher_name', 'created_at')
