from rest_framework import serializers
from courses.models import Course, Contact, Branch


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('value',)


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'adress',)


class CourseDetailSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(many=True)
    branches = BranchesSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'category', 'contacts', 'branches',)

    def create(self, validated_data):
        contacts = validated_data.pop('contacts')
        branches = validated_data.pop('branches')

        course = Course.objects.create(**validated_data)

        for contact in contacts:
            Contact.objects.create(course=course, **contact)

        for branch in branches:
            Branch.objects.create(course=course, **branch)

        return course

