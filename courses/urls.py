from django.contrib import admin
from django.urls import path

from courses import views
from courses.views import *
app_name = 'courses'


urlpatterns = [
    path('create/', CourseCreateView.as_view()),
    path('retrieve/<int:pk>/', views.CourseRetrieveView.as_view()),
]
