from django.db import models

from corecode.models import (
    AcademicSession,
    AcademicTerm,
    StudentClass,
    SubjectItem,
) 
from students.models import Student

from .utils import score_grade


# Create your models here.
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
    current_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectItem, on_delete=models.CASCADE)
    first_CA = models.IntegerField(default=0)
    second_CA = models.IntegerField(default=0)
    exam_score = models.IntegerField(default=0)

    class Meta:
        ordering = ["subject"]

    def __str__(self):
        return f"{self.student} {self.session} {self.term} {self.subject}"

    def total_score(self):
        return self.first_CA + self.second_CA + self.exam_score
        

    def grade(self):
        return score_grade(self.total_score())
