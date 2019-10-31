from rest_framework import generics

from courses.models import Course
from courses.serializers import CourseDetailSerializer


class CourseCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class CourseRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer