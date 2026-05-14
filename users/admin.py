from django.contrib import admin

from users.models import Mode_teaching, Teacher_profile, Locations

@admin.register(Teacher_profile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name',  'email', 'phone', 'age')
    search_fields = ('username', 'first_name', 'last_name',  'email', 'phone')
    list_filter = ('first_name', 'last_name', 'age', 'experience', 'locations')
    fields = [
        'username',
        ('first_name', 'last_name'),
        'locations',
        'main_specialty',
        'mode_teaching',
        ('email', 'phone'),
        'password',
        ('age', 'experience'),
        'info_about_teacher',
        'work_experience',
        'education',
        'other_specialities',
    ]

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Mode_teaching)
class Mode_teachingAdmin(admin.ModelAdmin):
    list_display = ('name_mode',)

