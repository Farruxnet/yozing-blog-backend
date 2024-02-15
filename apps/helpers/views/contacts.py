from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from helpers.models import Contacts
from helpers.serializers.contacts import ContactSerializer


class ContactsView(APIView):
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(responses={200: ContactSerializer(many=False)})
    def get(self, request):
        serializer = ContactSerializer(many=False, instance=Contacts.objects.all())
        return Response(data=serializer.data, status=status.HTTP_200_OK)
