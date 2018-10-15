from rest_framework.routers import DefaultRouter

from django.conf.urls import url

from comments.views import CommentViewSet
from movies.views import MovieViewSet, TopMoviesView

urlpatterns = [url(r'top', TopMoviesView.as_view())]
router = DefaultRouter()
router.register(r"movies", MovieViewSet, base_name="movie")
router.register(r"comments", CommentViewSet, base_name="comment")
urlpatterns += router.urls
