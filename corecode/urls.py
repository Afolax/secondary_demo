from django.urls import path

from .views import *


urlpatterns = [
    #path("", IndexView.as_view(), name="home"),
    path("site-config", SiteConfigView.as_view(), name="configs"),
    path(
        "current-session/", CurrentSessionAndTermView.as_view(), name="current-session"
    ),
    path("session/list/", SessionListView.as_view(), name="sessions"),
    path("session/create/", SessionCreateView.as_view(), name="session-create"),
    path(
        "session/<int:pk>/update/",
        SessionUpdateView.as_view(),
        name="session-update",
    ),
    path(
        "session/<int:pk>/delete/", 
        SessionDeleteView.as_view(),
        name="session-delete",
    ),
    path("term/list/", TermListView.as_view(), name="terms"),
    path("term/create/", TermCreateView.as_view(), name="term-create"),
    path("term/<int:pk>/update/", TermUpdateView.as_view(), name="term-update"),
    path("term/<int:pk>/delete/", TermDeleteView.as_view(), name="term-delete"),
    path("class/list/", ClassListView.as_view(), name="classes"),
    path("class/create/", ClassCreateView.as_view(), name="class-create"),
    path("class/<int:pk>/update/", ClassUpdateView.as_view(), name="class-update"),
    path("class/<int:pk>/delete/", ClassDeleteView.as_view(), name="class-delete"),
    path("subject/list/", SubjectListView.as_view(), name="subjects"),
    path("subject/create/", SubjectCreateView.as_view(), name="subject-create"),
    path(
        "subject/<int:pk>/update/",
        SubjectUpdateView.as_view(),
        name="subject-update",
    ),
    
    path("assignsubject/list/", AssignSubjectListView.as_view(), name="assigned-list"),
    path("assignsubject/create/", AssignSubjectCreateView.as_view(), name="assigned-create"),
    path("assignsubject/<int:pk>/detail/", AssignSubjectDetailView.as_view(), name="assigned-detail"),
    path("assignsubject/<int:pk>/update/", AssignSubjectUpdateView.as_view(), name="assigned-update"),
    path("assignsubject/<int:pk>/delete/", AssignSubjectDeleteView.as_view(), name="assigned-delete"),

    path("event/list/", EventListView.as_view(), name="events"),
    path("event/create/", EventCreateView.as_view(), name="event-create"),
    path("event/<int:pk>/update/", EventUpdateView.as_view(), name="event-update"),
    path("event/<int:pk>/delete/", EventDeleteView.as_view(), name="event-delete"),

    path("club/list/", ClubListView.as_view(), name="clubs"),
    path("club/create/", ClubCreateView.as_view(), name="club-create"),
    path("club/<int:pk>/update/", ClubUpdateView.as_view(), name="club-update"),
    path("club/<int:pk>/delete/", ClubDeleteView.as_view(), name="club-delete"),

    path("article/list/", ArticleListView.as_view(), name="articles"),
    path("article/create/", ArticleCreateView.as_view(), name="article-create"),
    path("article/<int:pk>/update/", ArticleUpdateView.as_view(), name="article-update"),
    path("article/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article-delete"),

    path("news/list/", NewsListView.as_view(), name="newslist"),
    path("news/create/", NewsCreateView.as_view(), name="news-create"),
    path("news/<int:pk>/update/", NewsUpdateView.as_view(), name="news-update"),
    path("news/<int:pk>/delete/", NewsDeleteView.as_view(), name="news-delete"),

    path("messages/list/", all_messages, name="messages"),

    path("student/message/list/", StudentMessageListView.as_view(), name="student-messages"),
    path("student/message/create/", StudentMessageCreateView.as_view(), name="stu-msg-create"),
    path("student/message/<int:pk>/update/", StudentMessageUpdateView.as_view(), name="stu-msg-update"),
    path("student/message/<int:pk>/delete/", StudentMessageDeleteView.as_view(), name="stu-msg-delete"),

    path("staff/message/list/", StaffMessageListView.as_view(), name="staff-messages"),
    path("staff/message/create/", StaffMessageCreateView.as_view(), name="stf-msg-create"),
    path("staff/message/<int:pk>/update/", StaffMessageUpdateView.as_view(), name="stf-msg-update"),
    path("staff/message/<int:pk>/delete/", StaffMessageDeleteView.as_view(), name="stf-msg-delete"),

    path("public/message/list/", PublicMessageListView.as_view(), name="public-messages"),
    path("public/message/create/", PublicMessageCreateView.as_view(), name="pub-msg-create"),
    path("public/message/<int:pk>/update/", PublicMessageUpdateView.as_view(), name="pub-msg-update"),
    path("public/message/<int:pk>/delete/", PublicMessageDeleteView.as_view(), name="pub-msg-delete"),

#About US

    path("about/academic/list/", AcademicListView.as_view(), name="academics"),
    path("about/academic/create/", AcademicCreateView.as_view(), name="academic-create"),
    path("about/academic/<int:pk>/update/", AcademicUpdateView.as_view(), name="academic-update"),
    path("about/academic/<int:pk>/delete/", AcademicDeleteView.as_view(), name="academic-delete"),

    path("about/admission/list/", AdmissionListView.as_view(), name="admissions"),
    path("about/admission/create/", AdmissionCreateView.as_view(), name="admission-create"),
    path("about/admission/<int:pk>/update/", AdmissionUpdateView.as_view(), name="admission-update"),
    path("about/admission/<int:pk>/delete/", AdmissionDeleteView.as_view(), name="admission-delete"),

    path("about/school/list/", SchoolListView.as_view(), name="schools"),
    path("about/school/create/", SchoolCreateView.as_view(), name="school-create"),
    path("about/school/<int:pk>/update/", SchoolUpdateView.as_view(), name="school-update"),
    path("about/school/<int:pk>/delete/", SchoolDeleteView.as_view(), name="school-delete"),

    path("about/hostel/list/", HostelListView.as_view(), name="hostels"),
    path("about/hostel/create/", HostelCreateView.as_view(), name="hostel-create"),
    path("about/hostel/<int:pk>/update/", HostelUpdateView.as_view(), name="hostel-update"),
    path("about/hostel/<int:pk>/delete/", HostelDeleteView.as_view(), name="hostel-delete"),

    path("about/staff/list/", FrontStaffListView.as_view(), name="f-staffs"),
    path("about/staff/create/", FrontStaffCreateView.as_view(), name="f-staff-create"),
    path("about/staff/<int:pk>/update/", FrontStaffUpdateView.as_view(), name="f-staff-update"),
    path("about/staff/<int:pk>/delete/", FrontStaffDeleteView.as_view(), name="f-staff-delete"),

    path("about/founder/list/", FounderListView.as_view(), name="founders"),
    path("about/founder/create/", FounderCreateView.as_view(), name="founder-create"),
    path("about/founder/<int:pk>/update/", FounderUpdateView.as_view(), name="founder-update"),
    path("about/founder/<int:pk>/delete/", FounderDeleteView.as_view(), name="founder-delete"),

    path("about/mission/list/", MissionListView.as_view(), name="missions"),
    path("about/mission/create/", MissionCreateView.as_view(), name="mission-create"),
    path("about/mission/<int:pk>/update/", MissionUpdateView.as_view(), name="mission-update"),
    path("about/mission/<int:pk>/delete/", MissionDeleteView.as_view(), name="mission-delete"),

    path("about/vision/list/", VisionListView.as_view(), name="visions"),
    path("about/vision/create/", VisionCreateView.as_view(), name="vision-create"),
    path("about/vision/<int:pk>/update/", VisionUpdateView.as_view(), name="vision-update"),
    path("about/vision/<int:pk>/delete/", VisionDeleteView.as_view(), name="vision-delete"),


# Detail Views url

    path("event/<int:pk>/detail/", event, name="event-detail"),
    path("news/<int:pk>/detail/", news, name="news-detail"),
    path("article/<int:pk>/detail/", article, name="article-detail"),
    path("club/<int:pk>/detail/", club, name="club-detail"),
    path("student/message/<int:pk>/detail/", student_message, name="stu-msg-detail"),
    path("staff/message/<int:pk>/detail/", staff_message, name="stf-msg-detail"),
    path("public/message/<int:pk>/detail/", public_message, name="pub-msg-detail"),


    path("academic/<int:pk>/detail/", academic, name="academic-detail"),
    path("admission/<int:pk>/detail/", admission, name="admission-detail"),
    path("school/<int:pk>/detail/", school, name="school-detail"),
    path("hostel/<int:pk>/detail/", hostel, name="hostel-detail"),
    path("staff/<int:pk>/detail/", staff, name="staff-detail"),
    path("founder/<int:pk>/detail/", founder, name="founder-detail"),
    path("mission/<int:pk>/detail/", mission, name="mission-detail"),
    path("vision/<int:pk>/detail/", vision, name="vision-detail"),




#others
    path("users/list/", users, name="users"),

]
