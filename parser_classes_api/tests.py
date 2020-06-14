import json
from urllib.parse import urlencode

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from http import HTTPStatus


@pytest.mark.django_db
class TestAppleViewSet:
    def test_formをPOSTする(self):
        client = APIClient()
        data = {'name': 'シナノゴールド'}
        actual = client.post(reverse('parser_classes_api:apple-list'),
                             content_type='application/x-www-form-urlencoded',
                             data=urlencode(data))

        assert actual.status_code == HTTPStatus.CREATED

    def test_JSONをPOSTする_content_typeを指定(self):
        client = APIClient()
        data = {'name': 'シナノゴールド'}

        actual = client.post(reverse('parser_classes_api:apple-list'),
                             content_type='application/json',
                             data=json.dumps(data))

        assert actual.status_code == HTTPStatus.CREATED

    def test_JSONをPOSTする_formatを指定(self):
        client = APIClient()
        data = {'name': 'シナノゴールド'}

        actual = client.post(reverse('parser_classes_api:apple-list'),
                             format='json',
                             data=data)

        assert actual.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
class TestAppleJsonOnlyViewSet:
    def test_formをPOSTする(self):
        client = APIClient()
        data = {'name': 'シナノゴールド'}
        actual = client.post(reverse('parser_classes_api:applejsononly-list'),
                             content_type='application/x-www-form-urlencoded',
                             data=urlencode(data))

        assert actual.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE

    def test_JSONをPOSTする_content_typeを指定(self):
        client = APIClient()
        data = {'name': 'シナノゴールド'}

        actual = client.post(reverse('parser_classes_api:applejsononly-list'),
                             content_type='application/json',
                             data=json.dumps(data))

        assert actual.status_code == HTTPStatus.CREATED

    def test_JSONをPOSTする_formatを指定(self):
        client = APIClient()
        data = {'name': 'シナノゴールド'}

        actual = client.post(reverse('parser_classes_api:applejsononly-list'),
                             format='json',
                             data=data)

        assert actual.status_code == HTTPStatus.CREATED
