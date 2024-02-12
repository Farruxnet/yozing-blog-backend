from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from helpers.models import About
from helpers.serializers.about import AboutSerializer


class AboutView(APIView):
    @swagger_auto_schema(responses={200: AboutSerializer()})
    def get(self, request):
        serializer = AboutSerializer(many=False, instance=About.objects.last())
        return Response(data=serializer.data, status=status.HTTP_200_OK)
