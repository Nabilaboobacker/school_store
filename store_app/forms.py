from django import forms
from . models import Course, Department
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import User_profile
from django.forms.widgets import DateInput

# registration form
class registration_form(UserCreationForm):
    class Meta:
        model=User
        fields=('username', 'password1', 'password2')


# user_details form
class user_profile_form(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ('name', 'email', 'date_of_birth', 'age', 'department', 'course','gender', 'phone', 'address', 'purpose', 'materials_provide')


        widgets = {
        'materials_provide': forms.CheckboxSelectMultiple,
        'date_of_birth': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()
            
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('course')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set





