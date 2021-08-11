from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import home_view

class homeTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        #response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        #response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code,200)

    def test_homepage_template(self):
        #response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'pages/home.html')

    def test_homepage_contains_correct_html(self):
        #response = self.client.get('/')
        self.assertContains(self.response, 'About')

    def test_homepage_does_not_contain_incorrect_html(self):
        #response = self.client.get('/')
        self.assertNotContains(self.response, 'This code should not be on the page')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            home_view.__name__
        )
