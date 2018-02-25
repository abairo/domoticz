from rest_framework import serializers
from .models import PeripheralType, Peripheral, ActionLog


class PeripheralTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeripheralType
        fields = ('__all__')


class PeripheralSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Peripheral
        fields = ('__all__')
        

class ActionLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActionLog
        fields = ('__all__')


class ActionSerializer(serializers.Serializer):
    action = serializers.PrimaryKeyRelatedField(queryset=Peripheral.objects.all())
