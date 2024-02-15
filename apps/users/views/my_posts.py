from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from yozing.models import Yozing
from yozing.serializers.yozing import YozingListSerializer, YozingMyPostDetailSerializer


class MyPostDetailView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(tags=['Users'], responses={200: YozingMyPostDetailSerializer(many=False)})
    def get(self, request, pk):
        instance = get_object_or_404(Yozing, id=pk)
        serializer = YozingMyPostDetailSerializer(instance=instance, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MyPostsView(ListAPIView):
    serializer_class = YozingListSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        return Yozing.objects.my_posts(user=self.request.user)

    @swagger_auto_schema(tags=['Users'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
