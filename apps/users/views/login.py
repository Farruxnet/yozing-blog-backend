from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from bot.helpers.redis_db import redis_client
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
        otp_code = redis_client.keys(pattern=f"otp_{data['otp_code']}_*")

        if otp_code:
            otp_code = otp_code[0].decode("utf-8")
            otp = otp_code.split('_')
            if delete := Token.objects.filter(user__telegram_id=otp[2]):
                delete.delete()
            token = Token.objects.create(
                user=User.objects.get(telegram_id=otp[2])
            )
            redis_client.delete(f'{otp_code}')
            serializer = JwtSerializer(many=False, instance=token)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data={'status': "UNAUTHORIZED", "message": _("Something is wrong")}, status=status.HTTP_401_UNAUTHORIZED)
