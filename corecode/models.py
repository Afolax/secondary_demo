from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from staffs.models import Staff


# Create your models here.

#school management

class SiteConfig(models.Model):
    """Site Configurations"""

    key = models.SlugField()
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key


class AcademicSession(models.Model):
    """Academic Session"""

    name = models.CharField(max_length=200, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class AcademicTerm(models.Model):
    """Academic Term"""

    name = models.CharField(max_length=20, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class StudentClass(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Subject(models.Model):
    """Subject"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'{self.name}'


class AssignSubject(models.Model):
    teacher_name = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    class_name = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.teacher_name} for {self.class_name}'s subjects"

    def get_absolute_url(self): 
        return reverse("assigned-detail", kwargs={"pk": self.pk})



class SubjectItem(models.Model):
    subject_data = models.ForeignKey(AssignSubject, on_delete=models.SET_NULL, null=True)
    subject_name = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.subject_name}'

#frontpage

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    venu = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    time_from = models.TimeField(default=timezone.now)
    time_to = models.TimeField(default=timezone.now)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Club(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    chairman = models.CharField(max_length=200)
    founder = models.CharField(max_length=200)
    founder_date = models.DateField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to="club")
    
    def __str__(self):
        return f"{self.title}"
  
class Article(models.Model):
    TYPE = [("poem", "poem"), ("article", "article"), ("quote", "quote"), ("riddles", "riddles"), ("jokes", "jokes"), ("write-up", "write-up"), ("health-talk", "health-talk"), ("short-story", "short-story"), ("others", "other")]

    type = models.CharField(
        max_length=20, choices=TYPE, default="article"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images')
    date = models.DateTimeField(auto_now_add=True)
    host = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, blank=True, null=True)
    
class News(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    images = models.FileField()
    date = models.DateField()
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, blank=True, null=True)

class Staff_message(models.Model):
    message = models.TextField()
    host = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}"

class Student_message(models.Model):
    message = models.TextField()
    host = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}"

class Public_message(models.Model):
    message = models.TextField()
    host = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}"

#About Us

class Academic(models.Model):
    content = models.TextField()
    current = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to="images")

    def __str__(self):
        return f"{self.id}"

class Admission(models.Model):
    content = models.TextField()
    current = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to="images")

    def __str__(self):
        return f"{self.id}"

class School(models.Model):
    content = models.TextField()
    current = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to="images")

    def __str__(self):
        return f"{self.id}"

class Hostel(models.Model):
    content = models.TextField()
    current = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to="images")

    def __str__(self):
        return f"{self.id}"

class Staff_Front(models.Model):
    content = models.TextField()
    current = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to="images")

    def __str__(self):
        return f"{self.id}"

class Founder(models.Model):
    content = models.TextField()
    current = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to="images")

    def __str__(self):
        return f"{self.id}"

class Mission(models.Model):
    content = models.TextField()
    current = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to="images")

    def __str__(self):
        return f"{self.id}"

class Vision(models.Model):
    content = models.TextField()
    current = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to="images")

    def __str__(self):
        return f"{self.id}"


