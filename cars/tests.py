from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Car

User = get_user_model()


class CarURLTests(TestCase):
    def setUp(self):
        # საჭირო მონაცემები ტესტებისთვის
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.car = Car.objects.create(
            owner=self.user,
            brand='Toyota',
            model='Camry',
            year=2020,
            price=25000,
            status='sale',
            description='ტესტ მანქანა'
        )

    def test_car_list_status_code(self):
        """მანქანების სია იტვირთება 200-ით"""
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)

    def test_car_list_uses_correct_template(self):
        """car_list სწორ template-ს იყენებს"""
        response = self.client.get(reverse('car_list'))
        self.assertTemplateUsed(response, 'cars/car_list.html')

    def test_car_detail_status_code(self):
        """კონკრეტული მანქანის გვერდი იტვირთება 200-ით"""
        response = self.client.get(reverse('car_detail', args=[self.car.pk]))
        self.assertEqual(response.status_code, 200)

    def test_car_detail_404_for_invalid_pk(self):
        """არარსებული მანქანის pk-ზე 404 უნდა დაბრუნდეს"""
        response = self.client.get(reverse('car_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_car_create_redirects_if_not_logged_in(self):
        """car_create — არაავტორიზებული user უნდა გადამისამართდეს login-ზე"""
        response = self.client.get(reverse('car_create'))
        self.assertEqual(response.status_code, 302)  # redirect

    def test_car_create_status_code_when_logged_in(self):
        """car_create — ავტორიზებული user-ისთვის 200 უნდა იყოს"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('car_create'))
        self.assertEqual(response.status_code, 200)

    def test_car_create_form_submission(self):
        """car_create — ფორმის წარმატებული გაგზავნა ქმნის ახალ Car-ს"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('car_create'), {
            'brand': 'BMW',
            'model': 'X5',
            'year': 2022,
            'price': 45000,
            'status': 'rent',
            'description': 'ახალი განცხადება',
        })
        self.assertEqual(Car.objects.count(), 2)  # setUp-ში 1, ახლა +1
        self.assertEqual(response.status_code, 302)  # redirect car_detail-ზე

    def test_car_str_representation(self):
        """__str__ მეთოდი სწორად აბრუნებს ტექსტს"""
        self.assertEqual(str(self.car), "Toyota Camry (2020)")
