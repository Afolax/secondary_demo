from django import forms
from django.forms import ModelForm, modelformset_factory, inlineformset_factory

from .models import *

SiteConfigForm = modelformset_factory(
    SiteConfig,
    fields=(
        "key",
        "value",
    ),
    extra=0,
)

 
class AcademicSessionForm(ModelForm):
    prefix = "Academic Session"

    class Meta:
        model = AcademicSession
        fields = ["name", "current"]


class AcademicTermForm(ModelForm):
    prefix = "Academic Term"

    class Meta:
        model = AcademicTerm
        fields = ["name", "current"]


class SubjectForm(ModelForm):
    prefix = "Subject"

    class Meta:
        model = Subject
        fields = ["name"]


class StudentClassForm(ModelForm): 
    prefix = "Class"

    class Meta:
        model = StudentClass
        fields = ["name"]


class CurrentSessionForm(forms.Form):
    current_session = forms.ModelChoiceField(
        queryset=AcademicSession.objects.all(),
        help_text='Click <a href="/session/create/?next=current-session/">here</a> to add new session',
    )
    current_term = forms.ModelChoiceField(
        queryset=AcademicTerm.objects.all(),
        help_text='Click <a href="/term/create/?next=current-session/">here</a> to add new term',
    )


SubjectItemFormset = inlineformset_factory(
    AssignSubject, SubjectItem, fields=["subject_name"], extra=1, can_delete=True
)

Subjects = modelformset_factory(AssignSubject, exclude=(), extra=4)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = "__all__"

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["type", "title", "content", "image"]

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "date", "images"]

class StudentMessageForm(forms.ModelForm):
    class Meta:
        model = Student_message
        fields = ["message"]

class StaffMessageForm(forms.ModelForm):
    class Meta:
        model = Staff_message
        fields = ["message"]
       
class GeneralMessageForm(forms.ModelForm):
    class Meta:
        model = Public_message
        fields = ["message"]



#About Us

class AcademicForm(forms.ModelForm):
    class Meta:
        model = Academic
        fields = "__all__"

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = "__all__"

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"

class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = "__all__"

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff_Front
        fields = "__all__"

class FounderForm(forms.ModelForm):
    class Meta:
        model = Founder
        fields = "__all__"

class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = "__all__"

class VisionForm(forms.ModelForm):
    class Meta:
        model = Vision
        fields = "__all__"

   