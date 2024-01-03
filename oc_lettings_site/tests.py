from django.test import TestCase, Client
from django.urls import reverse_lazy, path
from django.conf import settings
from django.test.utils import override_settings
from oc_lettings_site import views
from oc_lettings_site.urls import urlpatterns as all_urls


def view_trigger_error_500(request):
    """Fake view to trigger 500 error."""
    return 1 / 0


# Add test urls to test custom_404, custom_500 and
# view_trigger_error_500 view.
urlpatterns = all_urls + [
    path('test/404/', views.custom_404, name='test_404'),
    path('test/500/', views.custom_500, name='test_500'),
    path('test/trigger_500', view_trigger_error_500, name='test_trigegr_500')
]


class BaseTestCase(TestCase):
    """
    Custom TestCase class with fixtures.
    """
    @classmethod
    def setUpClass(cls):
        """
        Class level test data.
        """
        super().setUpClass()
        settings.TESTING = True


@override_settings(ROOT_URLCONF=__name__)
class TestOcLettingsSiteViews(BaseTestCase):
    """
    Oc_lettings_site views test class.
    """
    url = reverse_lazy('index')
    url_404 = reverse_lazy('test_404')
    url_500 = reverse_lazy('test_500')
    url_trigger_404 = 'unexisting_url/'
    url_trigger_500 = reverse_lazy('test_trigegr_500')

    def test_index(self):
        """
        GET on url rendrers the page with status code 200
        and the right templates.
        """
        templates_expected = [
            'index.html',
            'base.html'
        ]
        response = self.client.get(self.url)
        templates_used = [template.name for template in response.templates]
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            templates_used,
            templates_expected
        )

    def test_404(self):
        """
        GET on url_500 rendrers the page with status code 404
        and the right templates.
        """
        templates_expected = [
            '404.html',
            'base.html'
        ]
        response = self.client.get(self.url_404)
        templates_used = [template.name for template in response.templates]
        self.assertEqual(
            response.status_code,
            404
        )
        self.assertEqual(
            templates_used,
            templates_expected
        )

    def test_500(self):
        """
        GET on url_500 rendrers the page with status code 404
        and the right templates.
        """
        templates_expected = [
            '500.html',
            'base.html',
            None
        ]
        response = self.client.get(self.url_500)
        templates_used = [template.name for template in response.templates]
        self.assertEqual(
            response.status_code,
            500
        )
        self.assertEqual(
            templates_used,
            templates_expected
        )

    def test_trigger_404(self):
        """
        GET on unexisting url rendrers the page with status code 404
        and the right templates.
        """
        templates_expected = [
            '404.html',
            'base.html'
        ]
        response = self.client.get(self.url_trigger_404)
        templates_used = [template.name for template in response.templates]
        self.assertEqual(
            response.status_code,
            404
        )
        self.assertEqual(
            templates_used,
            templates_expected
        )

    def test_trigger_500(self):
        """
        GET url whose view contains an error rendrers the page with
        status code 500 and the right templates.
        """
        client = Client(raise_request_exception=False)
        templates_expected = [
            '500.html',
            'base.html',
            None
        ]
        response = client.get(self.url_trigger_500)
        templates_used = [template.name for template in response.templates]
        self.assertEqual(
            response.status_code,
            500
        )
        self.assertEqual(
            templates_used,
            templates_expected
        )


def test_dummy():
    assert 1
