from django_filters import rest_framework


class FilterBackend(rest_framework.DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if(request.query_params.get('status') == 'notPublish'):
            queryset = queryset.exclude(status='Publish')
            return queryset

        return super().filter_queryset(request, queryset, view) 