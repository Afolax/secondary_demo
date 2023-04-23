from ast import Sub
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SiteConfig)
admin.site.register(AcademicSession)
admin.site.register(AcademicTerm)
admin.site.register(StudentClass)
admin.site.register(Subject)
admin.site.register(AssignSubject)
admin.site.register(SubjectItem)

admin.site.register(Academic)
admin.site.register(Admission)
admin.site.register(School)
admin.site.register(Hostel)
admin.site.register(Staff_Front)
admin.site.register(Founder)
admin.site.register(Mission)
admin.site.register(Vision)
admin.site.register(Staff_message)
admin.site.register(Student_message)
admin.site.register(Public_message)


