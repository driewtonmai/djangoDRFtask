import json
from django.test import TestCase
from courses.models import *
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class CourseTest(TestCase):
    def setUp(self):
        self.courses_data = {
                                "name": "english zone",
                                "description": "upgrade ur english bro!",
                                "category": 1,
                                "contacts": [
                                    {
                                        "value": "0551134155"
                                    }
                                ],
                                "branches": [
                                    {
                                        "latitude": "145675567",
                                        "longitude": "345790754",
                                        "addres": "ул. Анала д. Карнавала"
                                    }
                                ]
                            }


    def test_course_create_view(self):
        response = self.client.get(reverse('courses:courses'), self.courses_data)
        self.assertEqual(response.status_code, 200)


    def test_course_retrieve_view(self):
        course = self.courses_data
        response = self.client.get(reverse('courses:retrieve', kwargs={"pk":1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course)

