from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from yozing.models import Yozing
from yozing.permissions.is_owner import IsOwner
from yozing.serializers.yozing import YozingUpdateSerializer


class YozingUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(request_body=YozingUpdateSerializer)
    def put(self, request, pk):
        instance = get_object_or_404(Yozing, pk=pk)
        serializer = YozingUpdateSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=YozingUpdateSerializer)
    def patch(self, request, pk):
        instance = get_object_or_404(Yozing, pk=pk)
        serializer = YozingUpdateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
