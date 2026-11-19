from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AuthenticationTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='student',
            password='strong-password',
        )

    def test_login_page_is_available(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)

    def test_valid_login_redirects_to_dashboard(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'student', 'password': 'strong-password'},
        )

        self.assertRedirects(response, reverse('dashboard'))

    def test_logout_returns_to_login_page(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('logout'))

        self.assertRedirects(response, reverse('login'))
