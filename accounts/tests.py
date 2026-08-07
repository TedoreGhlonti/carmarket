from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountsURLTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_signup_page_status_code(self):
        """Signup გვერდი იტვირთება 200-ით"""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_status_code(self):
        """Login გვერდი იტვირთება 200-ით"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_correct_credentials(self):
        """სწორი მონაცემებით login წარმატებით ხდება"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123',
        })
        self.assertEqual(response.status_code, 302)  # redirect შესვლის შემდეგ

    def test_login_with_wrong_password(self):
        """არასწორი პაროლით login არ ხერხდება (200 ბრუნდება, ფორმა შეცდომით)"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)  # ისევ login გვერდზე რჩება

    def test_logout_redirects(self):
        """Logout წარმატებით ხდება და გადამისამართებს"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
