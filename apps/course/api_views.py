from rest_framework import viewsets

from .models import CourseTemplate
from .serilizers import CourseTemplateSerializer
from apps.base.paginators import StandardResultsSetPagination


class CourseTemplateViewSet(viewsets.ModelViewSet):
    queryset = CourseTemplate.objects.order_by('-id').all()
    serializer_class = CourseTemplateSerializer
    pagination_class = StandardResultsSetPagination
