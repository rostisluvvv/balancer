from rest_framework import viewsets
from rest_framework.response import Response

from user.models import BalancerUser
from user.serializers import BalancerUserSerializer


class UserViewSet(viewsets.ViewSet):
    queryset = BalancerUser.objects.all()
    serializer_class = BalancerUserSerializer()

    def create(self, request):
        """Это HTTP метод POST"""
        serializer = BalancerUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(data=serializer.errors, status=400)
