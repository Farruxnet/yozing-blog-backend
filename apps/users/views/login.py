from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from bot.helpers.redis_db import redis_client, get_otp_from_redis
from users.models import Token, User
from users.serializers.login import LoginSerializer, JwtSerializer


class LoginView(APIView):

    @swagger_auto_schema(tags=["Users"], request_body=LoginSerializer, responses={200: JwtSerializer()})
    def post(self, request):
        """
        :param otp_code:
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        if redis_client.exists(f"otp_{data['otp_code']}"):
            otp = f"{data['otp_code']}"
            redis_data = get_otp_from_redis(otp=otp)
            if delete := Token.objects.filter(user__telegram_id=redis_data['user']):
                delete.delete()
            token = Token.objects.create(
                user=User.objects.get(telegram_id=redis_data['user'])
            )
            serializer = JwtSerializer(many=False, instance=token)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data={'status': "UNAUTHORIZED"}, status=status.HTTP_401_UNAUTHORIZED)
