from django.urls import path

from .views import *

urlpatterns = [
    path("create/<str:pk>/", create_result, name="create-result"),
    path("edit-results/", edit_results, name="edit-results"),
    path("view/<str:pk>/", student_results, name="student_result"), 

]
