from django import forms
from django.forms import modelformset_factory

from corecode.models import (
    AcademicSession, AcademicTerm, SubjectItem
    )
from .models import Result


class CreateResults(forms.Form):

    session = forms.ModelChoiceField(queryset=AcademicSession.objects.all())
    term = forms.ModelChoiceField(queryset=AcademicTerm.objects.all())
    subjects = forms.ModelMultipleChoiceField(
        queryset=SubjectItem.objects.all(),
        widget= forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, options, **kwargs): 
        self.options = options
        super(CreateResults, self).__init__(*args, **kwargs)
        self.fields['subjects'].queryset = options
            
            
    # def __init__(self, testList, *args, **kwargs): 
    #     self.testList = testList
    #     super(CreateResults, self).__init__(*args, **kwargs)
    #     self.fields['subjects'].choices = self.testList


EditResults = modelformset_factory(
    Result, fields=("first_CA", "second_CA", "exam_score"), extra=0, can_delete=True
)

