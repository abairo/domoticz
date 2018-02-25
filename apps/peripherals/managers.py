from django.db import models


class ActionLogManager(models.Manager):
    
    def perform_create(self, user, action_data):        
        from .models import ActionLog
        
        action_log = ActionLog(
            user_id=user.id,
            user_username = user.username,
            perfipheral_pin = action_data.pin,
            perfipheral_name = action_data.name,
            perfipheral_type_id = action_data.peripheral_type.id,
            perfipheral_type_name = action_data.peripheral_type.name,
            perfipheral_created_at = action_data.created_at            
        ).save()

        return action_log