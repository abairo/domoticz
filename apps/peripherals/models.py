from django.db import models
from .managers import ActionLogManager

class PeripheralType(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):        
        return '{} - {}'.format(self.name, self.is_active)


class Peripheral(models.Model):
    pin = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    peripheral_type = models.ForeignKey(PeripheralType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.pin, self.name)


class ActionLog(models.Model):
    user_id = models.IntegerField()
    user_username = models.CharField(max_length=50)
    perfipheral_pin = models.IntegerField()
    perfipheral_name = models.CharField(max_length=50)
    perfipheral_type_id = models.IntegerField()
    perfipheral_type_name = models.CharField(max_length=50)
    perfipheral_created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()
    creation = ActionLogManager()

    def __str__(self):
        return '{} - {} - {}'.format(self.user_username, self.perfipheral_type_name, self.perfipheral_name)
