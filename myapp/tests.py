from django.test import Client, TestCase
from django.urls import reverse

from .models import TelevisionShow
from .views import ShowListView

class ShowListViewTestCase(TestCase):
    def setUp(self):
      self.show1 = TelevisionShow.objects.create(
          title='Test Show 1',
          release_date='2022-01-01'
      )
      self.show2 = TelevisionShow.objects.create(
          title='Test Show 2',
          release_date='2023-01-01'
      )

    def test_show_list_view(self):
      client = Client()
      response = client.get(reverse('show_list'))

      self.assertEqual(response.status_code, 200)

      self.assertTemplateUsed(response, 'show_list.html')

      self.assertIn('shows', response.context)
      shows = response.context['shows']

      self.assertSequenceEqual(
          [show.title for show in shows],
          ['Test Show 2', 'Test Show 1']
      )

      self.assertContains(response, self.show1.title)
      self.assertContains(response, self.show2.title)
