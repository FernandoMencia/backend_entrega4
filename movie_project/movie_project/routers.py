from rest_framework.routers import DefaultRouter
from movies.viewsets import DirectorViewSet, MovieViewSet

router = DefaultRouter()
router.register('directors', DirectorViewSet, basename='director')
router.register('movies', MovieViewSet, basename= 'movie')

urlpatterns = router.urls