from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from parser_classes_api.views import AppleViewSet, AppleJsonOnlyViewSet

app_name = 'parser_classes_api'

router = DefaultRouter()
router.register(r'multi-parser', AppleViewSet)
router.register(r'json-only', AppleJsonOnlyViewSet)


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api', include(router.urls)),
]
