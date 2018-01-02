from django.shortcuts import render


class OptionalPaginationMixin():
    '''
    Mixin class to implement optional pagination to DRF
    Use example: url/?skip_pagination
    '''
    def paginate_queryset(self, queryset):
        if self.request.GET and 'select' in self.request.GET:
            return None
        else:
            return super().paginate_queryset(queryset)
