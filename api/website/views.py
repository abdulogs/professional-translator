from app.models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from api.helpers import pagination
from googletrans import Translator


class BlogApi(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.filter(is_active=True).select_related()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["id", "name", "description",
                        "category__name", "is_active"]
    ordering = ['-id']
    pagination_class = pagination


class QueryApi(viewsets.ModelViewSet):
    queryset = Query.objects.all().select_related()
    serializer_class = QuerySerializer


class TranslateApi(APIView):
    def post(self, request, format=None):
        translator = Translator()
        translateto = request.data.get('translateto')
        translatefrom = request.data.get('translatefrom')
        text = request.data.get('text')
        translation = translator.translate(text, dest=translatefrom)
        return Response({'text': translation.text})
