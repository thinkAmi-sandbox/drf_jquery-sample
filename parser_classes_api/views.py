from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from parser_classes_api.models import Apple, AppleJsonOnly
from parser_classes_api.serializers import AppleSerializer, AppleJsonOnlySerializer


class AppleViewSet(viewsets.ModelViewSet):
    queryset = Apple.objects.all()
    serializer_class = AppleSerializer


class AppleJsonOnlyViewSet(viewsets.ModelViewSet):
    queryset = AppleJsonOnly.objects.all()
    serializer_class = AppleJsonOnlySerializer
    parser_classes = (JSONParser, )
