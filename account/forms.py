from .models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from corecode.models import AcademicSession, AcademicTerm
from students.models import Student

class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name =forms.CharField(max_length=50)
    other_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'other_name', '_id', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Surname'}),
            'other_name': forms.TextInput(attrs={'placeholder': 'Other name'}),
            '_id': forms.TextInput(attrs={'placeholder': 'Student id'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user
        
# class ParentRegistrationForm(UserCreationForm):
#     fullname = forms.CharField(max_length=50)

#     class Meta:
#         model = User
#         fields = ['fullname', 'username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_parent = True
#         if commit:
#             user.save()
#         return user

class StaffRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name =forms.CharField(max_length=50)
    other_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'other_name', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Surname'}),
            #'_id': forms.TextInput(attrs={'placeholder': 'Staff id'}),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user

class StudentLogin(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control"
            }
        )
    )

class StaffLogin(forms.Form):
    staff_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control"
            }
        )
    )

# class ParentLogin(forms.Form):
#     email = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class': "form-control"
#             }
#         )
#     )

#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': "form-control"
#             }
#         )
#     )

class SessionForm(forms.Form):
    session = forms.ModelChoiceField(queryset=AcademicSession.objects.all())
    term = forms.ModelChoiceField(queryset=AcademicTerm.objects.all())
    
