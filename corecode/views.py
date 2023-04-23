from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, View, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from account.models import User

from .forms import *

from .models import *



class IndexView(TemplateView):
    template_name = "index2.html"


class SiteConfigView(LoginRequiredMixin, View):
    """Site Config View"""

    form_class = SiteConfigForm
    template_name = "corecode/siteconfig.html"

    def get(self, request, *args, **kwargs):
        formset = self.form_class(queryset=SiteConfig.objects.all())
        context = {"formset": formset}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        formset = self.form_class(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, "Configurations successfully updated")
        context = {"formset": formset, "title": "Configuration"}
        return render(request, self.template_name, context)


class SessionListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = AcademicSession
    template_name = "corecode/session_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SessionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AcademicSession
    form_class = AcademicSessionForm
    template_name = "corecode/mgt_form.html"
    success_url = reverse_lazy("sessions")
    success_message = "New session successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new session"
        return context


class SessionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AcademicSession
    form_class = AcademicSessionForm
    success_url = reverse_lazy("sessions")
    success_message = "Session successfully updated."
    template_name = "corecode/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            terms = (
                AcademicSession.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not terms:
                messages.warning(self.request, "You must set a session to current.")
                return redirect("session-list")
        return super().form_valid(form)


class SessionDeleteView(LoginRequiredMixin, DeleteView):
    model = AcademicSession
    success_url = reverse_lazy("sessions")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The session {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete session as it is set to current")
            return redirect("sessions")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(SessionDeleteView, self).delete(request, *args, **kwargs)


class TermListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = AcademicTerm
    template_name = "corecode/term_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TermCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AcademicTerm
    form_class = AcademicTermForm
    template_name = "corecode/mgt_form.html"
    success_url = reverse_lazy("terms")
    success_message = "New term successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new term"
        return context



class TermUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AcademicTerm
    form_class = AcademicTermForm
    success_url = reverse_lazy("terms")
    success_message = "Term successfully updated."
    template_name = "corecode/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            terms = (
                AcademicTerm.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not terms:
                messages.warning(self.request, "You must set a term to current.")
                return redirect("term")
        return super().form_valid(form)


class TermDeleteView(LoginRequiredMixin, DeleteView):
    model = AcademicTerm
    success_url = reverse_lazy("terms")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The term {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete term as it is set to current")
            return redirect("terms")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(TermDeleteView, self).delete(request, *args, **kwargs)


class ClassListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = StudentClass
    template_name = "corecode/class_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ClassCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentClass
    form_class = StudentClassForm
    template_name = "corecode/norm_form.html"
    success_url = reverse_lazy("classes")
    success_message = "New class successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new class"
        return context


class ClassUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = StudentClass
    fields = ["name"]
    success_url = reverse_lazy("classes")
    success_message = "class successfully updated."
    template_name = "corecode/norm_form.html"


class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = StudentClass
    success_url = reverse_lazy("classes")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The class {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        print(obj.name)
        messages.success(self.request, self.success_message.format(obj.name))
        return super(ClassDeleteView, self).delete(request, *args, **kwargs)


class SubjectListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Subject
    template_name = "corecode/subject_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SubjectForm()
        return context
        
class SubjectDetailView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Subject
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(SubjectDetailView, self).get_context_data(**kwargs)
        context["items"] = Subject.objects.filter(subject_class=self.object)
        return context

class SubjectCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "corecode/norm_form.html"
    success_url = reverse_lazy("subjects")
    success_message = "New subject successfully added"

class SubjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Subject
    fields = ["name", "subject_class"]
    success_url = reverse_lazy("subjects")
    success_message = "Subject successfully updated."
    template_name = "corecode/mgt_form.html"

class CurrentSessionAndTermView(LoginRequiredMixin, View):
    """Current SEssion and Term"""

    form_class = CurrentSessionForm
    template_name = "corecode/current_session.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(
            initial={
                "current_session": AcademicSession.objects.get(current=True),
                "current_term": AcademicTerm.objects.get(current=True),
            }
        )
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            session = form.cleaned_data["current_session"]
            term = form.cleaned_data["current_term"]
            AcademicSession.objects.filter(name=session).update(current=True)
            AcademicSession.objects.exclude(name=session).update(current=False)
            AcademicTerm.objects.filter(name=term).update(current=True)
            AcademicTerm.objects.exclude(name=term).update(current=False)

        return render(request, self.template_name, {"form": form})


class AssignSubjectListView(LoginRequiredMixin, ListView):
    model = AssignSubject


class AssignSubjectCreateView(LoginRequiredMixin, CreateView):
    model = AssignSubject
    fields = "__all__" 
    success_url = "/management/assignsubject/list" 

    def get_context_data(self, **kwargs):
        context = super(AssignSubjectCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["items"] = SubjectItemFormset(
                self.request.POST, prefix="subjectitem_set"
            )
        else:
            context["items"] = SubjectItemFormset(prefix="subjectitem_set")   
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["items"] 
        self.object = form.save()
        if self.object.id != None:
            if form.is_valid() and formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)


class AssignSubjectDetailView(LoginRequiredMixin, DetailView):
    model = AssignSubject
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(AssignSubjectDetailView, self).get_context_data(**kwargs)
        context["items"] = SubjectItem.objects.filter(subject_data=self.object)
        return context 


class AssignSubjectUpdateView(LoginRequiredMixin, UpdateView):
    model = AssignSubject
    fields = ["teacher_name", "class_name"]

    def get_context_data(self, **kwargs):
        context = super(AssignSubjectUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["items"] = SubjectItemFormset(
                self.request.POST, instance=self.object
            )
        else:
            context["items"] = SubjectItemFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        itemsformset = context["items"]
        if form.is_valid() and itemsformset.is_valid():
            form.save()
            itemsformset.save(commit=False)
        return super().form_valid(form)


class AssignSubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = AssignSubject
    success_url = reverse_lazy("assigned-list")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The class {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        print(obj.name)
        messages.success(self.request, self.success_message.format(obj.name))
        return super(AssignSubjectDeleteView, self).delete(request, *args, **kwargs)


#Frontpage

class EventCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "corecode/norm_form.html"
    success_url = reverse_lazy("events")
    success_message = "Event Created successfully"

    def get_form(self):
        """add date picker in forms"""
        form = super(EventCreateView, self).get_form()
        form.fields["date"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["time_from"].widget = widgets.DateInput(attrs={"type": "time"})
        form.fields["time_to"].widget = widgets.DateInput(attrs={"type": "time"})
        return form


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new Event"
        return context

class EventListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Event
    template_name = "corecode/event_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Event
    fields = "__all__"
    success_url = reverse_lazy("events")
    success_message = "Event successfully updated."
    template_name = "corecode/norm_form.html"

    def get_form(self):
        """add date picker in forms"""
        form = super(EventUpdateView, self).get_form()
        form.fields["date"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["time_from"].widget = widgets.DateInput(attrs={"type": "time"})
        form.fields["time_to"].widget = widgets.DateInput(attrs={"type": "time"})
        return form

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy("events")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The event {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message.format(obj.name))
        return super(EventDeleteView, self).delete(request, *args, **kwargs)



class ClubCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Club
    form_class = ClubForm
    template_name = "corecode/norm_form.html"
    success_url = reverse_lazy("clubs")
    success_message = "Club added successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new Club"
        return context

class ClubListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Club
    template_name = "corecode/club_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ClubUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Club
    fields = "__all__"
    success_url = reverse_lazy("clubs")
    success_message = "Club successfully updated."
    template_name = "corecode/norm_form.html"

class ClubDeleteView(LoginRequiredMixin, DeleteView):
    model = Club
    success_url = reverse_lazy("clubs")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The club {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message.format(obj.name))
        return super(ClubDeleteView, self).delete(request, *args, **kwargs)


class StudentMessageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student_message
    form_class = StudentMessageForm
    template_name = "corecode/norm_form.html"
    success_url = reverse_lazy("student-messages")
    success_message = "Message Sent successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Message to Students"
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class StudentMessageListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Student_message
    context_object_name = "std_msg"
    template_name = "corecode/message_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StudentMessageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student_message
    fields = ["__all__"]
    excludes = ['host', 'date']
    success_url = reverse_lazy("student-messages")
    success_message = "Message updated."
    template_name = "corecode/norm_form.html"

class StudentMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Student_message
    success_url = reverse_lazy("student-messages")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The message {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message.format(obj.name))
        return super(StudentMessageDeleteView, self).delete(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "corecode/norm_form.html"
    success_url = reverse_lazy("articles")
    success_message = "Write-Up successfully Uploaded"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create a Write-Up"
        return context

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

class ArticleListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Article
    template_name = "corecode/message_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ArticleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Article
    fields = ["__all__"]
    excludes = ['host', 'date']
    success_url = reverse_lazy("articles")
    success_message = "Article updated."
    template_name = "corecode/norm_form.html"

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy("articles")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The message {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message.format(obj.name))
        return super(ArticleDeleteView, self).delete(request, *args, **kwargs)


class NewsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = "corecode/norm_form.html"
    success_url = reverse_lazy("newslist")
    success_message = "News created Successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add News"
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NewsListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = News
    template_name = "corecode/message_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class NewsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = News
    fields = ["__all__"]
    excludes = ['host', 'date']
    success_url = reverse_lazy("newslist")
    success_message = "News updated."
    template_name = "corecode/norm_form.html"

class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    success_url = reverse_lazy("newslist")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The message {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message.format(obj.name))
        return super(NewsDeleteView, self).delete(request, *args, **kwargs)


class StaffMessageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Staff_message
    form_class = StaffMessageForm
    template_name = "corecode/norm_form.html"
    success_url = reverse_lazy("staff-messages")
    success_message = "Message Sent successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Message to Staff"
        return context

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

class StaffMessageListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Staff_message
    context_object_name = "stf_msg"
    template_name = "corecode/message_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StaffMessageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Staff_message
    fields = ["__all__"]
    excludes = ['host', 'date']
    success_url = reverse_lazy("staff-messages")
    success_message = "message successfully updated."
    template_name = "corecode/norm_form.html"

class StaffMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff_message
    success_url = reverse_lazy("staff-messages")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The message {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message.format(obj.name))
        return super(StaffMessageDeleteView, self).delete(request, *args, **kwargs)



class PublicMessageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Public_message
    form_class = GeneralMessageForm
    template_name = "corecode/norm_form.html"
    success_url = reverse_lazy("public-messages")
    success_message = "Message Sent successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Message to Public"
        return context

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

class PublicMessageListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Public_message
    context_object_name = "pub_msg"
    template_name = "corecode/message_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PublicMessageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Public_message
    fields = ["__all__"]
    excludes = ['host', 'date']
    success_url = reverse_lazy("public-messages")
    success_message = "Message successfully updated."
    template_name = "corecode/norm_form.html"

class PublicMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Public_message
    success_url = reverse_lazy("public-messages")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The message {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message.format(obj.name))
        return super(PublicMessageDeleteView, self).delete(request, *args, **kwargs)



def all_messages(request):
    stu_msg = Student_message.objects.all()
    stf_msg = Staff_message.objects.all()
    pub_msg = Public_message.objects.all()
    
    context = {
        "stumessage":stu_msg,
        "stfmessage":stf_msg,
        "pubmessage":pub_msg,
    }
    return render(request, "corecode/message_list", context)

def users(request):
    users = User.objects.all()
    return render(request, "corecode/userlist.html", {"users":users})

def event(request, pk):
    event = Event.objects.get(id=pk)
    title = "Event"
    return render(request, "corecode/event.html", {"data": event, "title": title})

def club(request, pk):
    club = Club.objects.get(id=pk)
    title = "Club"
    return render(request, "corecode/club.html", {"club": club, "title": title})

def article(request, pk):
    article = Article.objects.get(id=pk)
    title = "Article"
    return render(request, "corecode/event.html", {"data": article, "title": title})

def news(request, pk):
    news = News.objects.get(id=pk)
    title = "News"
    return render(request, "corecode/detail.html", {"data": news, "title": title})

def student_message(request, pk):
    stu_msg = Student_message.objects.get(id=pk)
    title = "Student Message"
    return render(request, "account/message.html", {"data": stu_msg, "title": title})

def staff_message(request, pk):
    stf_msg = Staff_message.objects.get(id=pk)
    title = "Staff Message"
    return render(request, "account/message.html", {"data": stf_msg, "title": title})

def public_message(request, pk):
    pub_msg = Public_message.objects.get(id=pk)
    title = "Public Message"
    return render(request, "account/message.html", {"data": pub_msg, "title": title})

def academic(request, pk):
    academic = Academic.objects.get(id=pk)
    title = "Academic"
    return render(request, "corecode/detail.html", {"data":academic, "title": title})

def admission(request, pk):
    admission = Admission.objects.get(id=pk)
    title = "Admission"
    return render(request, "corecode/detail.html", {"data":admission, "title": title})

def school(request, pk):
    school = School.objects.get(id=pk)
    title = "School"
    return render(request, "corecode/detail.html", {"data":school, "title": title})

def hostel(request, pk):
    hostel = Hostel.objects.get(id=pk)
    title = "Hostel"
    return render(request, "corecode/detail.html", {"data":hostel, "title": title})

def staff(request, pk):
    staff = Staff_Front.objects.get(id=pk)
    title = "Staff"
    return render(request, "corecode/detail.html", {"data":staff, "title": title})

def founder(request, pk):
    founder = Founder.objects.get(id=pk)
    title = "Founder"
    return render(request, "corecode/detail.html", {"data":founder, "title": title})

def mission(request, pk):
    mission = Mission.objects.get(id=pk)
    title = "Mission"
    return render(request, "corecode/detail.html", {"data":mission, "title": title})

def vision(request, pk):
    vision = Vision.objects.get(id=pk)
    title = "Vision"
    return render(request, "corecode/detail.html", {"data":vision, "title": title})


# def userdelete(request, pk):
#     user = User.object.get(id=pk)
#     user.delete()
#     return redirect(users)

#About Us
#__Academic

class AcademicListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Academic
    template_name = "corecode/academic_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AcademicCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Academic
    form_class = AcademicForm
    template_name = "corecode/mgt_form.html"
    success_url = reverse_lazy("academics")
    success_message = "New academic write-up successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Academic write-up"
        return context

class AcademicUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Academic
    form_class = AcademicForm
    success_url = reverse_lazy("academics")
    success_message = "Academic write-up successfully updated."
    template_name = "corecode/mgt_form.html"

    def form_valid(self, form): 
        obj = self.object
        if obj.current == False:
            Academics = (
                Academic.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not Academics:
                messages.warning(self.request, "You must set a academic to current.")
                return redirect("academics")
        return super().form_valid(form)

class AcademicDeleteView(LoginRequiredMixin, DeleteView):
    model = Academic
    success_url = reverse_lazy("academics")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The academic write-up {} has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete this academic write-up as it is set to current")
            return redirect("academics")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(AcademicDeleteView, self).delete(request, *args, **kwargs)

#_Admission

class AdmissionListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Admission
    template_name = "corecode/admission_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdmissionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Admission
    form_class = AdmissionForm
    template_name = "corecode/mgt_form.html"
    success_url = reverse_lazy("admissions")
    success_message = "New admission requirement successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new admission requirement"
        return context

class AdmissionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Admission
    form_class = AdmissionForm
    success_url = reverse_lazy("admissions")
    success_message = "Admission requirement successfully updated."
    template_name = "corecode/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            admissions = (
                Admission.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not admissions:
                messages.warning(self.request, "You must set a admission to current.")
                return redirect("admissions")
        return super().form_valid(form)

class AdmissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Admission
    success_url = reverse_lazy("admissions")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The admission requirements {} has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete this admission requirement as it is set to current")
            return redirect("admissions")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(AdmissionDeleteView, self).delete(request, *args, **kwargs)

#_School

class SchoolListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = School
    template_name = "corecode/school_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SchoolCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = School
    form_class = SchoolForm
    template_name = "corecode/mgt_form.html"
    success_url = reverse_lazy("schools")
    success_message = "New school information successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new school history"
        return context

class SchoolUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = School
    form_class = SchoolForm
    success_url = reverse_lazy("schools")
    success_message = "school information successfully updated."
    template_name = "corecode/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            schools = (
                School.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not schools:
                messages.warning(self.request, "You must set a school to current.")
                return redirect("schools")
        return super().form_valid(form)

class SchoolDeleteView(LoginRequiredMixin, DeleteView):
    model = School
    success_url = reverse_lazy("schools")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The schools information {} has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete this school information as it is set to current")
            return redirect("schools")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(SchoolDeleteView, self).delete(request, *args, **kwargs)

#_Hostel

class HostelListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Hostel
    template_name = "corecode/hostel_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class HostelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Hostel
    form_class = HostelForm
    template_name = "corecode/mgt_form.html"
    success_url = reverse_lazy("hostels")
    success_message = "New hostel information successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new hostel information"
        return context

class HostelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Hostel
    form_class = HostelForm
    success_url = reverse_lazy("hostels")
    success_message = "hostels information successfully updated."
    template_name = "corecode/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            hostels = (
                Hostel.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not hostels:
                messages.warning(self.request, "You must set a hostel to current.")
                return redirect("hostels")
        return super().form_valid(form)

class HostelDeleteView(LoginRequiredMixin, DeleteView):
    model = Hostel
    success_url = reverse_lazy("hostels")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The hostel information {} has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete this hostel information as it is set to current")
            return redirect("hostels")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(HostelDeleteView, self).delete(request, *args, **kwargs)

#_Staff

class FrontStaffListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Staff_Front
    template_name = "corecode/frontstaff_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class FrontStaffCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Staff_Front
    form_class = StaffForm
    template_name = "corecode/mgt_form.html"
    success_url = reverse_lazy("f-staffs")
    success_message = "New staff qualities successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add staff qualities"
        return context

class FrontStaffUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Staff_Front
    form_class = StaffForm
    success_url = reverse_lazy("f-staffs")
    success_message = "staffs qualities successfully updated."
    template_name = "corecode/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            hostels = (
                Staff_Front.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not hostels:
                messages.warning(self.request, "You must set a staff to current.")
                return redirect("f-staffs")
        return super().form_valid(form)

class FrontStaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff_Front
    success_url = reverse_lazy("f-staffs")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The staff quality {} has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete this staff quality as it is set to current")
            return redirect("f-staffs")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(FrontStaffDeleteView, self).delete(request, *args, **kwargs)

#_Founder

class FounderListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Founder
    template_name = "corecode/founder_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class FounderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Founder
    form_class = FounderForm
    template_name = "corecode/mgt_form.html"
    success_url = reverse_lazy("founders")
    success_message = "New founder(s) history successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new founder history"
        return context

class FounderUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Founder
    form_class = FounderForm
    success_url = reverse_lazy("founders")
    success_message = "founders history successfully updated."
    template_name = "corecode/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            founders = (
                Founder.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not founders:
                messages.warning(self.request, "You must set a founders history to current.")
                return redirect("founders")
        return super().form_valid(form)

class FounderDeleteView(LoginRequiredMixin, DeleteView):
    model = Hostel
    success_url = reverse_lazy("founders")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The founders history {} has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete this founders history as it is set to current")
            return redirect("founders")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(FounderDeleteView, self).delete(request, *args, **kwargs)

#_Mission

class MissionListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Mission
    template_name = "corecode/mission_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MissionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Mission
    form_class = MissionForm
    template_name = "corecode/mgt_form.html"
    success_url = reverse_lazy("missions")
    success_message = "New missions successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new mission"
        return context

class MissionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Mission
    form_class = MissionForm
    success_url = reverse_lazy("missions")
    success_message = "mission successfully updated."
    template_name = "corecode/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            missions = (
                Mission.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not missions:
                messages.warning(self.request, "You must set a missions to current.")
                return redirect("missions")
        return super().form_valid(form)

class MissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Mission
    success_url = reverse_lazy("missions")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The missions {} has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete this missions as it is set to current")
            return redirect("missions")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(MissionDeleteView, self).delete(request, *args, **kwargs)

#_Vision

class VisionListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Vision
    template_name = "corecode/vision_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VisionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Vision
    form_class = VisionForm
    template_name = "corecode/mgt_form.html"
    success_url = reverse_lazy("visions")
    success_message = "New visions successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new vision"
        return context

class VisionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Vision
    form_class = VisionForm
    success_url = reverse_lazy("visions")
    success_message = "visions successfully updated."
    template_name = "corecode/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            visions = (
                Vision.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not visions:
                messages.warning(self.request, "You must set a visions history to current.")
                return redirect("visions")
        return super().form_valid(form)

class VisionDeleteView(LoginRequiredMixin, DeleteView):
    model = Vision
    success_url = reverse_lazy("visions")
    template_name = "corecode/core_confirm_delete.html"
    success_message = "The visions {} has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete this visions as it is set to current")
            return redirect("visions")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(VisionDeleteView, self).delete(request, *args, **kwargs)

