from django.shortcuts import render, redirect
#from django.core.paginator import Paginator, EmptyPage
from corecode.models import *

# Create your views here.

def frontpage(request):
    events = Event.objects.order_by('-id')[:4]
    clubs = Club.objects.order_by('-id')[:4]
    articles = Article.objects.order_by('-id')[:6]
    news = News.objects.order_by('-id')[:6]
    g_msg = Public_message.objects.order_by('-id')[:4]
    academic = Academic.objects.filter(current=True)
    admission = Admission.objects.filter(current=True)
    school = School.objects.filter(current=True)
    staff = Staff_Front.objects.filter(current=True)
    hostel = Hostel.objects.filter(current=True)
    founder = Founder.objects.filter(current=True)
    mission = Mission.objects.filter(current=True)
    vision = Vision.objects.filter(current=True)


    context = {
        "events":events,
        "clubs" : clubs,
        "articles": articles,
        "newslist": news,
        "notifications": g_msg,
        "academic": academic,
        "admission": admission,
        "school": school,
        "hostel": hostel,
        "staff": staff,
        "founder": founder,
        "mission": mission,
        "vision": vision,
    }
    return render(request, "index2.html", context)

def event(request, pk):
    event = Event.objects.get(id=pk)
    vision = Vision.objects.filter(current=True)
    mission = Mission.objects.filter(current=True)
    return render(request, "front/event.html", {"event":event, "vis":vision, "mis":mission})

def club(request, pk):
    club = Club.objects.get(id=pk)
    vision = Vision.objects.filter(current=True)
    mission = Mission.objects.filter(current=True)
    return render(request, "front/club.html", {"club":club, "vis":vision, "mis":mission})

def article(request, pk):
    article = Article.objects.get(id=pk)
    vision = Vision.objects.filter(current=True)
    mission = Mission.objects.filter(current=True)
    return render(request, "front/article.html", {"article":article, "vis":vision, "mis":mission})


# About Us

def academic(request, pk):
    obj = Academic.objects.get(id=pk)
    title = "About Our Academic System"
    return render(request, "front/detail.html", {"obj":obj, "tilte":title})

def admission(request, pk):
    obj = Admission.objects.get(id=pk)
    title = "About Our Admission Process"
    return render(request, "front/detail.html", {"obj":obj, "tilte":title})
    
def school(request, pk):
    obj = School.objects.get(id=pk)
    title = "About Our School and Environment"
    return render(request, "front/detail.html", {"obj":obj, "tilte":title})

def hostel(request, pk):
    obj = Hostel.objects.get(id=pk)
    title = "About Our Hostel and Accomodation"
    return render(request, "front/detail.html", {"obj":obj, "tilte":title})

def founder(request, pk):
    obj = Founder.objects.get(id=pk)
    title = "About The Founder"
    return render(request, "front/detail.html", {"obj":obj, "tilte":title})

def staff(request, pk):
    obj = Staff_Front.objects.get(id=pk)
    title = "About Our Staff and qualifications"
    return render(request, "front/detail.html", {"obj":obj, "tilte":title})

def mission(request, pk):
    obj = Mission.objects.get(id=pk)
    title = "Our Mission"
    return render(request, "front/detail.html", {"obj":obj, "title":title})

def vision(request, pk):
    obj = Vision.objects.get(id=pk)
    title = "Our Vision"
    return render(request, "front/detail.html", {"obj":obj, "title":title})
