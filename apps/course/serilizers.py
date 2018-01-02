from rest_framework import serializers

from .models import CourseTemplate, Course, Carrer


class CarrerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrer
        fields = ('id', 'name', 'code')


class CourseTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseTemplate
        fields = ('id', 'name', 'code')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    carrer = CarrerSerializer(read_only=True)
    course_template = CourseTemplateSerializer(read_only=True)
    class Meta:
        model = Course
        fields = ('id', 'get_dynamic_natural_key', 'carrer', 'course_template')
