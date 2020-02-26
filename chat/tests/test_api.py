import pytest
from django.urls import reverse
from model_bakery import baker

from chat.models import Message


@pytest.fixture
def message(db):
    return baker.make(
        Message,
        email='admin@gmail.com',
        text='New day'
    )


class TestChecksUrlMessageDetail:
    url_get_detail = 'message_detail'

    @pytest.fixture
    def url(self, message):
        return reverse(self.url_get_detail, kwargs={'pk': message.pk})

    @pytest.mark.django_db
    def test_checks_api_url_for_message_detail(self, client, url):
        response = client.get(url)
        assert response.status_code == 200
