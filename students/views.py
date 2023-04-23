from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from corecode.models import StudentClass, AcademicSession, AcademicTerm
from finance.models import Invoice

from .models import Student

def all_student(request):
    session = request.current_session
    term = request.current_term
    students = Student.objects.all()
    page = 'students'
    return render(request, "students/student_list.html", {"students": students, "page":page, 'session':session, 'term':term})


def studentclass(request, pk):
    session = request.current_session
    term = request.current_term
    classname = StudentClass.objects.get(id=pk)
    students = Student.objects.filter(current_class=classname)
    page = 'Student'
    context = {
    'students':students,
    'page':page,
    'current_class':classname,
    'session':session,
    'term':term,
    }
    return render(request, "students/student_list.html", context)


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context["payments"] = Invoice.objects.filter(student=self.object)
        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    fields = ["current_status", "registration_number", "surname", "firstname", "other_name", "gender", "date_of_birth", 
    "current_class", "date_of_admission",
    "parent_mobile_number", "address", "others", "passport"
    ]    
    success_message = "New student successfully added."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentCreateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_admission"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        # form.fields['passport'].widget = widgets.FileInput()
        return form


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("student-list")

