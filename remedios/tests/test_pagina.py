import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('index'))
    return resp
