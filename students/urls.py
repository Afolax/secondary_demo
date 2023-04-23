from django.urls import path

from .views import *


urlpatterns = [
    #path("list/", StudentListView.as_view(), name="student-list"),
    path("all/", all_student, name="all-students"),
    path("all/<str:pk>/", studentclass, name="student-list"),
    path("<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("create/", StudentCreateView.as_view(), name="student-create"),
    path("<int:pk>/update/", StudentUpdateView.as_view(), name="student-update"),
    path("delete/<int:pk>/", StudentDeleteView.as_view(), name="student-delete"),
    
]
