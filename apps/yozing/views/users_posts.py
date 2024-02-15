from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer

from yozing.models import Yozing
from yozing.serializers.yozing import YozingListSerializer


class UsersPostsView(ListAPIView):
    serializer_class = YozingListSerializer
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return Yozing.objects.users_posts(user_id=user_id)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('user_id', openapi.IN_QUERY, description="Filter by user id", type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
