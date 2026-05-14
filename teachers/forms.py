from django import forms

from users.models import Teacher_profile
from teachers.models import Complaints, TeachersComplaints


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = TeachersComplaints
        fields = ('teacher_name', 'complaint')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # complaints = Complaints.objects.all()
        #
        # self.dict_comp = {complaint.name_complaint: complaint.id for complaint in complaints}
        #
        # choices = [(complaint.name_complaint, complaint.name_complaint) for complaint in complaints]

        self.fields['complaint'] = forms.CharField(label="Complaint")

        self.fields['teacher_name'] = forms.CharField(label="Teacher Name")

    def clean_complaint(self):
        complaint_key = self.cleaned_data.get('complaint')
        try:
            return Complaints.objects.get(name_complaint=complaint_key)
        except Complaints.DoesNotExist:
            raise forms.ValidationError("Invalid complaint selected.")


    def clean_teacher_name(self):
        teacher_name_key = self.cleaned_data.get('teacher_name')
        try:
            return Teacher_profile.objects.get(username=teacher_name_key)
        except Teacher_profile.DoesNotExist:
            raise forms.ValidationError("Invalid teacher name selected.")
