from django.contrib.auth.models import User
from django.test import override_settings, TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from psave.models import Host
import datetime


class DataEndpointTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="test_user", is_superuser=True)
        cls.host = Host.objects.create(hostname="test_host", api_user=cls.user)
        cls.token = Token.objects.create(user=cls.user)
        cls.client = APIClient()

    def setUp(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

    def test_data_creation_correct_data(self):
        data = {"cpu": 0.000, "memory": {}, "processes": [{"p1": "value1"}, {"p2": "value2"}], "disk": {}, "date": datetime.datetime.now()}
        res = self.client.post("/api/stats/", data, format="json")
        assert res.status_code == HTTP_201_CREATED
        assert res.body == data

    def test_data_creation_bad_data(self):
        data = {"bad_data": 12345}
        res = self.client.post("/api/stats/", data, format="json")

        assert res.status_code == HTTP_400_BAD_REQUEST