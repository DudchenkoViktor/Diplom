import re

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError

from users.models import Teacher_profile, Locations, Mode_teaching
from teachers.models import Specializations
from users.utils import numeric_validator, fullname_validator

class TeacherRegisterForm(UserCreationForm):
    first_name = forms.CharField(validators=[fullname_validator])
    last_name = forms.CharField(validators=[fullname_validator])
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    locations = forms.CharField()
    main_specialty = forms.CharField()

    class Meta:
        model = Teacher_profile
        fields = ('first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2',
                  'locations',
                  'main_specialty')

    def clean_locations(self):
        location_key = self.cleaned_data.get('locations')
        try:
            return Locations.objects.get(name=location_key)
        except Locations.DoesNotExist:
            raise forms.ValidationError("Invalid complaint selected.")

    def clean_main_specialty(self):
        specialization_key = self.cleaned_data.get('main_specialty')
        try:
            return Specializations.objects.get(name_spec=specialization_key)
        except Specializations.DoesNotExist:
            raise forms.ValidationError("Invalid complaint selected.")


class ProfileUpdateForm(UserChangeForm):

    first_name = forms.CharField(validators=[fullname_validator])
    last_name = forms.CharField(validators=[fullname_validator])
    username = forms.CharField(required=False)
    phone = forms.CharField(required=False, empty_value=None)
    email = forms.EmailField(required=False, empty_value=None)
    age = forms.CharField(required=False, validators=[numeric_validator], empty_value=None)
    experience = forms.CharField(required=False, validators=[numeric_validator], empty_value=None)
    info_about_teacher = forms.CharField(required=False)
    work_experience = forms.CharField(required=False)
    other_specialities = forms.CharField(required=False)
    education = forms.CharField(required=False)

    locations = forms.CharField()
    main_specialty = forms.ModelChoiceField(queryset=Specializations.objects.all(), required=False)
    mode_teaching = forms.CharField(required=False, empty_value=None)

    image = forms.ImageField(required=False)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone:
            return None

        if not phone.isdigit():
            raise forms.ValidationError("The phone number must contain only digits")

        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(phone):
            raise forms.ValidationError("The phone number must be 10 digits long")

        return phone


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:  # if email is empty, return None
            return None
        if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email):
            raise ValidationError("The email must include @gmail.com and be in English.")
        return email

    def clean_locations(self):
        location_key = self.cleaned_data.get('locations')
        try:
            return Locations.objects.get(name=location_key)
        except Locations.DoesNotExist:
            raise forms.ValidationError("Invalid complaint selected.")

    def clean_mode_teaching(self):
        mode_key = self.cleaned_data.get('mode_teaching')
        try:
            if not mode_key:
                return None
            return Mode_teaching.objects.get(name_mode=mode_key)
        except Mode_teaching.DoesNotExist:
            raise forms.ValidationError("Invalid complaint selected.")


    class Meta:
        model = Teacher_profile
        fields = ('first_name',
                  'last_name',
                  'username',
                  'age',
                  'experience',
                  'info_about_teacher',
                  'work_experience',
                  'other_specialities',
                  'education',
                  'locations',
                  'main_specialty',
                  'mode_teaching',
                  'phone',
                  'email',
                  'image'
                  )


