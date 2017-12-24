from rest_framework import viewsets

from .models import CourseTemplate
from .serilizers import CourseTemplateSerializer

class CourseTemplateViewSet(viewsets.ModelViewSet):
    queryset = CourseTemplate.objects.all()
    serializer_class = CourseTemplateSerializer
