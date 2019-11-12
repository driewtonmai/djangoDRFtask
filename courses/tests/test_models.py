from django.test import TestCase
from courses.models import *


class CategoryTest(TestCase):

    def create_category(self, name=1, impath="image.jpeg"):
        return Category.objects.create(name=name, impath=impath)

    def test_category_creation(self):
        category = self.create_category()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), category.impath
                         )


class BranchTest(TestCase):

    def create_branch(self, latitude="400234234", longitude="399123444", address="Пр. Чуй 162"):
        category = Category.objects.create(name=1, impath="image.jpeg")
        course = Course.objects.create(name="Четкий плов", description="Тут делают четкий плов", category=category)
        return Branch.objects.create(latitude=latitude, longitude=longitude, addres=address, course=course)

    def test_branch_creation(self):
        branch = self.create_branch()
        self.assertTrue(isinstance(branch, Branch))
        self.assertEqual(branch.__str__(), branch.addres)


class ContactTest(TestCase):

    def create_contact(self, type=1, value="+996558332233"):
        category = Category.objects.create(name=1, impath="image.jpeg")
        course = Course.objects.create(name="Четкий плов", description="Тут делают четкий плов", category=category)
        return Contact.objects.create(type=1, value=value, course=course)

    def test_contact_creation(self):
        contact = self.create_contact()
        self.assertTrue(isinstance(contact, Contact))
        self.assertEqual(contact.__str__(), contact.value)

class CourseTest(TestCase):

    def create_course(self, name="Четкий плов", description="Тут делают четкий плов"):
        category = Category.objects.create(name=1, impath="image.jpeg")
        return Course.objects.create(name=name, description=description, category=category)

    def test_course_creation(self):
        course = self.create_course()
        self.assertTrue(isinstance(course, Course))
        self.assertEqual(course.__str__(), course.name)
