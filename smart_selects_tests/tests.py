import json
from django.test import TestCase
from django.core.urlresolvers import reverse
from .forms import LocationForm
from .models import Continent, Country


class SimpleTest(TestCase):
    def setUp(self):
        self.asia = Continent.objects.create(continent='Asia')
        Country.objects.create(continent=self.asia, country='Russia')
        Country.objects.create(continent=self.asia, country='Japan')
        self.europe = Continent.objects.create(continent='Europe')
        Country.objects.create(continent=self.europe, country='Italy')
        Country.objects.create(continent=self.europe, country='Spain')

    def test_render(self):
        form = LocationForm()
        rendered = form.as_p()
        self.assertIn('Asia', rendered)
        self.assertIn('Europe', rendered)

    def test_view(self):
        chain_url = reverse('chained_filter', kwargs={
            'app': 'smart_selects_tests',
            'model': 'Country',
            'field': 'continent',
            'value': self.asia.pk})
        response = self.client.get(chain_url)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(['Japan', 'Russia'], [x['display'] for x in data])
