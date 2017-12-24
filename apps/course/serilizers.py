from rest_framework import serializers

from .models import CourseTemplate

class CourseTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseTemplate
        fields = ('id', 'name',)
