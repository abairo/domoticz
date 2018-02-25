from django.shortcuts import render
from rest_framework import viewsets, response, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import ActionLog, Peripheral
from .serializers import ActionLogSerializer, PeripheralSerializer, ActionSerializer

class ActionLogViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = ActionLogSerializer
    queryset = ActionLog.objects.all()


class PeripheralViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PeripheralSerializer
    queryset = Peripheral.objects.all()


class ActionViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer_data = ActionSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        ActionLog.creation.perform_create(request.user, serializer_data.validated_data['action'])
        
        return response.Response(data={}, status=status.HTTP_200_OK)
