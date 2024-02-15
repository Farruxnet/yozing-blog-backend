from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer

from helpers.models import Tags
from helpers.serializers.tags import TagSerializer


class TagsListView(ListAPIView):
    serializer_class = TagSerializer
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        search_params = self.request.query_params.get('search')
        return Tags.objects.search(search=search_params)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, description="Search by tag name", type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
