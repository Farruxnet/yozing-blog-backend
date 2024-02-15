from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from helpers.models import Rules
from helpers.serializers.rules import RuleSerializer


class RulesView(APIView):
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(responses={200: RuleSerializer(many=False)})
    def get(self, request):
        serializers = RuleSerializer(many=False, instance=Rules.objects.last())
        return Response(data=serializers.data, status=status.HTTP_200_OK)
