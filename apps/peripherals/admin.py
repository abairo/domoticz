from django.contrib import admin
from .models import PeripheralType, Peripheral, ActionLog

admin.site.register(PeripheralType)
admin.site.register(Peripheral)
admin.site.register(ActionLog)
