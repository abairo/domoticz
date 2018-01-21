from django.db import models


class AbstractPeripheral(models.Model):
    name = models.CharField(max_length=30)
    pin = models.IntegerField()
    value = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return '{} - {}'.format(self.name, self.value)


class Gate(AbstractPeripheral):
    pass

class Lamp(AbstractPeripheral):
    pass
