from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers.user_detail import UserDetailSerializer


class UserMeDetailView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(tags=['Users'], responses={200: UserDetailSerializer(many=False)})
    def get(self, request):
        serializer = UserDetailSerializer(instance=request.user, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(tags=['Users'], responses={200: UserDetailSerializer(many=False)})
    def get(self, request, pk):
        instance = get_object_or_404(User, pk=pk)
        serializer = UserDetailSerializer(instance=instance, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
