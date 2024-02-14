from django.db import connection
from rest_framework.generics import ListAPIView

from yozing.models import Yozing
from yozing.serializers.yozing import YozingListSerializer


class YozingListView(ListAPIView):
    serializer_class = YozingListSerializer

    def get_queryset(self):
        search_params = self.request.query_params.get('search')
        return Yozing.objects.search(search=search_params)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

