from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from yozing.models import Yozing
from yozing.permissions.is_owner import IsOwner


class YozingDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def delete(self, request, pk):
        instance = get_object_or_404(Yozing, id=pk)
        instance.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
