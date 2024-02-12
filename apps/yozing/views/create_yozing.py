from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from yozing.serializers.yozing import YozingCreateSerializer


class YozingCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=YozingCreateSerializer)
    def post(self, request):
        serializer = YozingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=None, created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

