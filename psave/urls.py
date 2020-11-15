from rest_framework.routers import SimpleRouter

from psave.views import DataViewSet

router = SimpleRouter()
router.register(r'stats', DataViewSet, basename='data')
