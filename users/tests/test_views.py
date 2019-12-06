from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from users.models import Users
from users.tests.mocks.mock_files import load_file


class TestUsersHomePage(TestCase):
    def setUp(self):
        standard_user = User.objects.create_user(
            username="test",
            email="test@example.com",
            password="test_password"
        )
        Users.objects.create(
            user=standard_user,
            photo=load_file()
        )

    def test_user_index_page(self):
        response = self.client.get(reverse("index:index"))
        self.assertTrue(response.context["users_list"])
