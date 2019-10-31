from django.contrib import admin

# Register your models here.
from courses.models import Category, Course, Branch, Contact

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Contact)
