from django.urls import path, include
from api.website.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("query", QueryApi, basename="WAQuery")
router.register("blog", BlogApi, basename="WABlog")

urlpatterns = [
    path('', include(router.urls), name="WApi"),
    path('translate/', TranslateApi.as_view(), name='WATranslateApi'),
]
