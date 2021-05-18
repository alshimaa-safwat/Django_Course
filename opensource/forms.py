from django import forms
from opensource.models import Student,Track

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname','lname','age','student_track')
class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('name',)