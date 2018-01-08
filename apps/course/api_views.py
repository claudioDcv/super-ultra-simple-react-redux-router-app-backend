from rest_framework import viewsets
from django.db.models import Q

from .models import CourseTemplate, Course, Carrer
from .serilizers import CourseTemplateSerializer, CarrerSerializer, CourseSerializer
from apps.base.paginators import StandardResultsSetPagination
from apps.base.views import OptionalPaginationMixin

from rest_framework import filters
from rest_framework_filters.backends import DjangoFilterBackend


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.order_by('-id').all()
    serializer_class = CourseSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (
        filters.OrderingFilter,
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    filter_fields = {
        'id': ('exact', 'icontains'),
        'carrer__name': ('exact', 'icontains'),
        'course_template__name': ('exact', 'icontains'),
    }
    search_fields = '__all__'


class CarrerViewSet(OptionalPaginationMixin, viewsets.ModelViewSet):
    queryset = Carrer.objects.order_by('-id').all()
    serializer_class = CarrerSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        qs = super(CarrerViewSet, self).get_queryset()
        q = self.request.GET.get('q', False)
        if 'q' in self.request.GET:
            if len(q) > 3:
                return qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
            else:
                return qs[0:100]
        return qs


class CourseTemplateViewSet(OptionalPaginationMixin, viewsets.ModelViewSet):
    queryset = CourseTemplate.objects.order_by('-id').all()
    serializer_class = CourseTemplateSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        qs = super(CourseTemplateViewSet, self).get_queryset()
        q = self.request.GET.get('q', False)
        if 'q' in self.request.GET:
            if len(q) > 3:
                return qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
            else:
                return qs[0:100]
        return qs
