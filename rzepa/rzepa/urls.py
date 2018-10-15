from rest_framework.routers import DefaultRouter

from comments.views import CommentViewSet
from movies.views import MovieViewSet

router = DefaultRouter()
router.register(r"movies", MovieViewSet, base_name="movie")
router.register(r"comments", CommentViewSet, base_name="comment")
urlpatterns = router.urls
