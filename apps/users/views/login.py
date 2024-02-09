from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from bot.helpers.redis_db import redis_client
from users.serializers.login import LoginSerializer, JwtSerializer


class LoginView(APIView):

    @swagger_auto_schema(request_body=LoginSerializer, responses={200: JwtSerializer()})
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        if redis_client.exists(f"otp_{data['otp_code']}"):
            otp = redis_client.get(f"otp_{data['otp_code']}").decode("utf-8")
            print('ok')
        return Response(data=data, status=status.HTTP_200_OK)
