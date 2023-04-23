from django.urls import path
from .views import *

urlpatterns = [
    path("student/registration/", student_register, name="student-register"),
    path("student/login/", student_login, name="student-login"),
    path("student/profile/", student_profile, name="student-profile"),
    path("staff/registration", staff_register, name="staff-register"),
    path("staff/login/", staff_login, name="staff-login"),
    path("staff/profile/", staff_profile, name="profile"),

    path("student/result/", view_result, name="student-result"),
    path("student/payment/detail/", paymentdetail, name="payment-detail"),

    path("staff/message/<str:pk>", staff_message, name="stf-msg"),
    path("student/message/<str:pk>", student_message, name="stu-msg"),


    path("under_construction/", under_construct, name="under_construction"),
 

]