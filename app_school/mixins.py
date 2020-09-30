from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import homework

class ClassroomFiledMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='teacher').exists():
            self.fields = ['title', 'chairs', 'level']
        else:
            raise Http404('Not allowed!!')  
        return super().dispatch(request, *args, **kwargs)

class LessonFieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='teacher').exists():
            self.fields = ['title', 'class_room', 'start_time', 'end_time']
        else:
            raise Http404('Not allowed!')
        return super().dispatch(request, *args, **kwargs)

class LessonValidMixin():
    def form_valid(self, form):
        if self.request.user.groups.filter(name='teacher').exists():
            self.obj = form.save(commit = False)
            self.obj.teacher = self.request.user
        return super().form_valid(form)
    
class HomeworkFieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='teacher').exists():
            self.fields = ['title', 'question', 'question_file', 'lesson']
        else:
            raise Http404('Not allowed!')
        return super().dispatch(request, *args, **kwargs)

class HomeworkValidMixin():
    def form_valid(self, form):
        if self.request.user.groups.filter(name='teacher').exists():
            self.obj = form.save(commit = False)
            self.obj.teacher = self.request.user
        else:
            raise Http404('Not allowed!')
        return super().form_valid(form)

class AnswerFieldMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['answer']
        return super().dispatch(request, *args, **kwargs)
    

class AnswerValidMixin():
    def form_valid(self, form):
        question = get_object_or_404(homework, pk=self.kwargs['pk'])
        self.obj = form.save(commit = False)
        self.obj.student = self.request.user
        self.obj.question = question
        return super().form_valid(form)
    




    
    