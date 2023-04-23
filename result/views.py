from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View

from students.models import Student
from staffs.models import Staff
from corecode.models import StudentClass, AcademicSession, AcademicTerm, SubjectItem


from .forms import CreateResults, EditResults
from .models import Result


@login_required
def create_result(request, pk):
    cl = StudentClass.objects.get(id=pk)
    user = request.user
    staff = Staff.objects.get(user=user)
    values = SubjectItem.objects.filter(subject_data__teacher_name=staff, subject_data__class_name=cl)
    students = Student.objects.filter(current_class=cl)
    if request.method == "POST":

        # after visiting the second page
        if "finish" in request.POST:
            form = CreateResults(request.POST, options=values)
            if form.is_valid():
                subjects = form.cleaned_data["subjects"]
                session = form.cleaned_data["session"]
                term = form.cleaned_data["term"]
                students = request.POST["students"]
                results = []
                for student in students.split(","):
                    stu = Student.objects.get(pk=student)
                    if stu.current_class:
                        for subject in subjects:
                            check = Result.objects.filter(
                                session=session,
                                term=term,
                                current_class=stu.current_class,
                                subject=subject,
                                student=stu,
                            ).first()
                            if not check:
                                results.append(
                                    Result(
                                        session=session,
                                        term=term,
                                        current_class=stu.current_class,
                                        subject=subject,
                                        student=stu,
                                    )
                                )

                Result.objects.bulk_create(results)
                return redirect("edit-results")

        # after choosing students
        id_list = request.POST.getlist("students")
        if id_list:
            form = CreateResults(options=values,
                initial={
                    "session": request.current_session,
                    "term": request.current_term,
                    # "subjects": SubjectItem.objects.filter(subject_data__teacher_name=staff,
                    # subject_data__class_name=cl)
                }
            )
            studentlist = ",".join(id_list)
            return render(
                request,
                "result/create_result_page2.html",
                {"students": studentlist, "form": form, "count": len(id_list)},
            )
        else:
            messages.warning(request, "You didnt select any student.")
    return render(request, "result/create_result.html", {"students": students})


@login_required
def edit_results(request):
    form = EditResults()
    if request.method == "POST":
        form = EditResults(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Results successfully updated")
        return redirect("edit-results")
    else:
        results = Result.objects.filter(
            session=request.current_session, term=request.current_term
        )
        form = EditResults(queryset=results)
    return render(request, "result/edit_results.html", {"formset": form})


def student_results(request, pk):
    cl = StudentClass.objects.get(id=pk)
    results = Result.objects.filter(
        session=request.current_session, term=request.current_term, current_class=cl,
    )
    bulk = {}

    for result in results:
        first_CA = 0
        second_CA = 0
        exam_total = 0
        subjects = []
        for subject in results:
            if subject.student == result.student:
                subjects.append(subject)
                first_CA += subject.first_CA
                second_CA += subject.second_CA
                exam_total += subject.exam_score

        bulk[result.student.id] = {
            "student": result.student,
            "subjects": subjects,
            "first_CA": first_CA,
            "second_CA": second_CA,
            "exam_total": exam_total,
            "total_total": first_CA + second_CA + exam_total,
        }

    context = {"results": bulk}
    return render(request, "result/all_results.html", context)



# class ResultListView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         results = Result.objects.filter(current_class=self.request.GET.get()
#             session=request.current_session, term=request.current_term
#         )
#         bulk = {}

#         for result in results:
#             test_total = 0
#             exam_total = 0
#             subjects = []
#             for subject in results:
#                 if subject.student == result.student:
#                     subjects.append(subject)
#                     test_total += subject.test_score
#                     exam_total += subject.exam_score

#             bulk[result.student.id] = {
#                 "student": result.student,
#                 "subjects": subjects,
#                 "test_total": test_total,
#                 "exam_total": exam_total,
#                 "total_total": test_total + exam_total,
#             }

#         context = {"results": bulk}
#         return render(request, "result/all_results.html", context)
