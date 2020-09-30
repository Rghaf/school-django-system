from django.urls import path, include
from app_school import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('add-class/', views.CreateClassroom.as_view(), name='add-class'),
    path('add-lesson/', views.CreateLesson.as_view(), name='add-lesson'),
    path('add-homework/', views.CreateHomework.as_view(), name='add-homework'),
    path('homeworks/', views.view_homeworks, name='homeworks'),
    path('homework/<int:pk>/', views.home_work, name='homework'),
    path('add-answer/<int:pk>/', views.CreateAnswer.as_view(), name='add-answer'),
    path('answer/<int:pk>/', views.answer, name='answer'),
]
