from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from yozing.models import Yozing
from yozing.serializers.yozing import YozingDetailSerializer


class YozingDetailView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(responses={200: YozingDetailSerializer(many=False)})
    def get(self, request, pk):
        instance = get_object_or_404(Yozing, id=pk)
        serializer = YozingDetailSerializer(instance=instance, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
