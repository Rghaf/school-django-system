from django.contrib import admin
from .models import class_room, lesson, homework, homework_answers

# Register your models here.
admin.site.register(class_room)
admin.site.register(lesson)
admin.site.register(homework)
admin.site.register(homework_answers)