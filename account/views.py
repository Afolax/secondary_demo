from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import StudentRegistrationForm, StudentLogin, StaffRegistrationForm, StaffLogin, SessionForm
from students.models import Student
from staffs.models import Staff
from result.models import Result
from finance.models import Invoice, InvoiceItem, Receipt
from corecode.models import Student_message, Staff_message
from corecode.forms import ArticleForm
from .decorators import student_required, staff_required
from django.db.models import Q

#Create your view:

def under_construct(request):
    return render(request, "account/under_construct.html")

#Student Use

def student_register(request):
    form = StudentRegistrationForm()
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            _id = form.cleaned_data.get('_id')
            student = Student.objects.filter(surname=lastname, firstname=firstname, registration_number=_id)
            if student.exists():
                form.save()
                messages.success(request, "Your account has been successfully created, procede to login")
                return redirect("student-login")

        else:
            messages.error(request, "Please fill all the required spaces")

    return render(request, "account/student-register.html", {"form":form})

def student_login(request):
    form = StudentLogin(request.POST)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None and user.is_student:
            login(request, user)
            surname = request.user.last_name
            name =request.user.first_name
            messages.info(request, f"You are now logged in as {surname} {name}.")
            return redirect("student-profile")
        else:
            messages.error(request,"Invalid username or password.")
    form = StudentLogin()
    context = {
        'form' : form
    }
    return render(request, 'account/student-login.html', context)

@login_required
@student_required
def student_profile(request):
    user = request.user
    student = Student.objects.get(user=user)
    return render (request, 'account/profile.html', {'student':student})

@login_required
@student_required
def view_result(request):
    formset = SessionForm()
    if request.method == 'POST':
        formset = SessionForm(request.POST)
        if 'finish' in request.POST:
            session = request.POST.get("session")
            term = request.POST.get("term")
            student = request.user
            stu = student.id
            results = Result.objects.filter(student=stu, term=term, session=session)
            context = {
                'results':results,
            }
        return render(request, 'account/result.html', context)

    formset = SessionForm()
    context ={
        'formset': formset,
    }
    return render(request, 'account/result1.html', context)


@login_required
@student_required
def paymentdetail(request):
    formset = SessionForm()
    if request.method == 'POST':
        formset = SessionForm(request.POST)
        if 'finish' in request.POST:
            session = request.POST.get("session")
            term = request.POST.get("term")
            student = Student.objects.get(user=request.user)
            invoice = Invoice.objects.filter(student=student, term=term, session=session)
            if not invoice:
                return render(request, 'account/404.html')
            else:
                receipts = Receipt.objects.get(invoice=invoice)
                items = InvoiceItem.objects.filter(invoice=invoice)
                context = {
                    "invoice": invoice,
                    "student": student,
                    "receipts":receipts,
                    "items": items,
                }
            return render(request, "account/invoice-detail.html", context)  

    formset = SessionForm()
    context ={
        'formset': formset,
    }
    return render(request, 'account/invoice2.html', context)

@login_required
@student_required
def student_message(request, pk):
    msg = Student_message.objects.get(id=pk)
    title = "Student Message"
    return render(request, "account/message.html", {"data": msg, "title": title})

# def article_create(request):
#     form = ArticleForm()
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             request.

def staff_register(request):
    form = StaffRegistrationForm()
    if request.method == "POST":
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            # _id = form.cleaned_data.get('_id')
            staff = Staff.objects.filter(surname=lastname, firstname=firstname)
            if staff.exists():
                form.save()
                messages.success(request, "Your account has been successfully created, procede to login")
                return redirect("staff-login")

        else:
            messages.error(request, "Please fill all the required spaces")

    return render(request, "account/staff-register.html", {"form":form})

def staff_login(request):
    form = StaffLogin(request.POST)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            surname = request.user.last_name
            name =request.user.first_name
            messages.info(request, f"You are now logged in as {surname} {name}.")
            return redirect("profile")
        else:
            messages.error(request,"Invalid staff_id or password.")
    form = StudentLogin()
    context = {
        'form' : form
    }
    return render(request, 'account/staff-login.html', context)

@login_required
@staff_required
def staff_profile(request):
    user = request.user
    staff = Staff.objects.get(user=user)
    return render (request, 'account/staff_profile.html', {'staff':staff})


@login_required
@staff_required
def staff_message(request, pk):
    msg = Staff_message.objects.get(id=pk)
    title = "Student Message"
    return render(request, "account/message.html", {"data": msg, "title": title})
