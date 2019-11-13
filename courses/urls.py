from django.contrib import admin
from django.urls import path

from courses import views
from courses.views import *
app_name = 'courses'


urlpatterns = [
    path('courses/', CourseCreateView.as_view(), name='courses'),
    path('retrieve/<int:pk>/', views.CourseRetrieveView.as_view(), name='retrieve'),
]
