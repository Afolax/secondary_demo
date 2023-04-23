from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from students.models import Student
from staffs.models import Staff

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.filter(surname=instance.last_name, firstname=instance.first_name).update(user=instance)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_student(sender, instance, **kwargs):
#     instance.student.save()

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_parent_profile(sender, instance, created, **kwargs):
#     if created:
#         Parent.objects.create(user=instance)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_parent(sender, instance, **kwargs):
#     instance.parent.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_staff_profile(sender, instance, created, **kwargs):
    if created:
        stu = Staff.objects.filter(firstname=instance.first_name, surname=instance.last_name).update(user=instance)
        