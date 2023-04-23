from django.urls import path

from .views import *


urlpatterns = [
    
    path("", frontpage, name="home" ),
    path("event/<int:pk>/", event, name="event" ),
    path("article/<int:pk>/", article, name="article" ),
    path("club/<int:pk>/", club, name="club" ),

    #About Us
    path("academic/<int:pk>/", academic, name="academic" ),
    path("admission/<int:pk>/", admission, name="admission" ),
    path("school/<int:pk>/", school, name="school" ),
    path("founder/<int:pk>/", founder, name="founder" ),
    path("hostel/<int:pk>/", hostel, name="hostel" ),
    path("staff/<int:pk>/detail", staff, name="home-staff" ),
    path("mission/<int:pk>/", mission, name="mission" ),
    path("vision/<int:pk>/", vision, name="vision" ),

]