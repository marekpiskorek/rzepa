from rest_framework.routers import DefaultRouter

from movies.views import MovieViewSet

router = DefaultRouter()
router.register(r"movies", MovieViewSet, base_name="movie")
urlpatterns = router.urls
