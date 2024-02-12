from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from yozing.models import Yozing
from yozing.serializers.yozing import YozingUpdateSerializer


class YozingUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, pk, request):
        instance = get_object_or_404(Yozing, pk=pk)
        serializer = YozingUpdateSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, pk, request):
        instance = get_object_or_404(Yozing, pk=pk)
        serializer = YozingUpdateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
