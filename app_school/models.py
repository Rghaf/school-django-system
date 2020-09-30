from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.
class class_room(models.Model):
    title = models.CharField(max_length=120, null=True)
    chairs = models.IntegerField(null=True, blank=True)
    level = models.CharField(max_length=2, null=True)

    def __str__(self):
        return "%s" % (self.title)

class lesson(models.Model):
    title = models.CharField(max_length=200, null=True)
    class_room = models.ForeignKey(class_room ,null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    start_time = models.TimeField(null=True, blank=True) 
    end_time = models.TimeField(null=True, blank=True)
    students = models.ManyToManyField(User, blank=True, related_name='childrens')

    def __str__(self):
        return "%s" % (self.title)

class homework(models.Model):
    title = models.CharField(max_length=250, null=True)
    teacher = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='teachers')
    question = models.TextField(max_length=1000, null=True, blank=True)
    question_file = models.FileField(upload_to='questions', null=True, blank=True)
    lesson = models.ForeignKey(lesson, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return reverse('app-school:homework', kwargs={'pk': self.pk})

class homework_answers(models.Model):
    question = models.ForeignKey(homework, null=True, on_delete=models.CASCADE)
    answer = models.FileField(upload_to='answers', null=True)
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s-%s" % (self.question, self.student)

    def get_absolute_url(self):
        return reverse('app-school:answer', kwargs={'pk': self.pk})