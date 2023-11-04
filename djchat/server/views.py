from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Server
from .serializers import ServerSerializer


class ServerListViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        category = self.request.query_params.get('category', None)

        if category is not None:
             self.queryset.filter(category=category)

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
