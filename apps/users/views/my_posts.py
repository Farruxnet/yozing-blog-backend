from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from yozing.models import Yozing
from yozing.serializers.yozing import YozingListSerializer


class MyPostsView(ListAPIView):
    serializer_class = YozingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Yozing.objects.my_posts(user=self.request.user)

    @swagger_auto_schema(tags=['Users'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
