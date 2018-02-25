from rest_framework import routers
from .views import ActionViewSet, ActionLogViewSet, PeripheralViewSet


router = routers.SimpleRouter()
router.register(r'action', ActionViewSet, base_name='action')
router.register(r'action-log', ActionLogViewSet, base_name='action-log')
router.register(r'peripheral', PeripheralViewSet, base_name='peripheral')

urlpatterns = router.urls
