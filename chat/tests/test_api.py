import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_api_for_list_message(client):
    response = client.get(reverse('message_list'))
    assert response.status_code == 200


