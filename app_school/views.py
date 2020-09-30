from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from app_school.mixins import ClassroomFiledMixin, LessonFieldMixin, LessonValidMixin, HomeworkFieldMixin, HomeworkValidMixin,  AnswerFieldMixin, AnswerValidMixin


from app_school.models import class_room, homework, lesson, homework_answers

# Create your views here.
def home(request):
    return HttpResponse("HOME PAGE")

def success(request):
    return HttpResponse("Done!!")

class CreateClassroom(LoginRequiredMixin, ClassroomFiledMixin ,CreateView):
    model = class_room
    template_name = 'add/add-class.html'
    success_url = reverse_lazy('app-school:success')

class CreateLesson(LoginRequiredMixin, LessonFieldMixin, LessonValidMixin, CreateView):
    model = lesson
    template_name = 'add/add-lesson.html'
    success_url = reverse_lazy('app-school:success')

class CreateHomework(LoginRequiredMixin, HomeworkFieldMixin, HomeworkValidMixin, CreateView):
    model = homework
    template_name = 'add/add-homework.html'
    success_url = reverse_lazy('app-school:success')

class CreateAnswer(LoginRequiredMixin, AnswerFieldMixin, AnswerValidMixin, CreateView):
    model = homework_answers
    template_name = 'add/add-answer.html'
    success_url = reverse_lazy('app-school:success')

def view_homeworks(request):
    ctx = {}
    if request.user.groups.filter(name='student').exists():
        my_works = homework.objects.filter(lesson__students=request.user)
        ctx['works'] = my_works
        ctx['role'] = 'student'
    elif request.user.groups.filter(name='teacher').exists():
        my_questions = homework.objects.filter(teacher=request.user)
        my_works = homework_answers.objects.filter(question__teacher=request.user)
        ctx['works'] = my_works 
        ctx['role'] = 'teacher'
    return render(request, 'homeworks.html', ctx)

def home_work(request, pk):
    ctx = {}
    work = get_object_or_404(homework, pk=pk)
    ctx['work'] = work
    return render(request, 'homework.html', ctx) 

def answer(request, pk):
    ctx = {}
    ctx['obj'] = get_object_or_404(homework_answers, pk=pk)
    return render(request, 'answer.html', ctx)