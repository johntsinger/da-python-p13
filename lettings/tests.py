from django.test import TestCase, Client
from django.urls import reverse_lazy
from lettings.models import Address, Letting


class BaseTestCase(TestCase):
    """
    Custom TestCase class with fixtures.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Class level test data.
        """
        cls.address = Address.objects.create(
            number=588,
            street='Argyle Avenue',
            city='East Meadow',
            state='NY',
            zip_code=11554,
            country_iso_code='USA'
        )
        cls.letting = Letting.objects.create(
            title='Underground Hygge',
            address=cls.address
        )


class TestLettingsView(BaseTestCase):
    """
    Lettings views test class.
    """
    url_list = reverse_lazy('lettings:index')
    url_detail = reverse_lazy('lettings:letting', args=(1,))

    def test_list_view(self):
        """
        GET on url_list rendrers the page with status code 200,
        the expected context data and the right templates.
        """
        templates_expected = [
            'lettings/index.html',
            'base.html'
        ]
        response = self.client.get(self.url_list)
        templates_used = [template.name for template in response.templates]

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertQuerysetEqual(
            response.context.get('lettings_list', None),
            Letting.objects.all(),
            transform=lambda x: x
        )
        self.assertEqual(
            templates_used,
            templates_expected
        )

    def test_detail_view(self):
        """
        GET on url_detail rendrers the page with status code 200,
        the expected context data and the right templates.
        """
        templates_expected = [
            'lettings/letting.html',
            'base.html'
        ]
        response = self.client.get(self.url_detail)
        templates_used = [template.name for template in response.templates]

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            response.context.get('title', None),
            self.letting.title
        )
        self.assertEqual(
            response.context.get('address', None),
            self.letting.address
        )
        self.assertEqual(
            templates_used,
            templates_expected
        )


class TestLettingsModels(BaseTestCase):
    """
    Lettings models test class.
    """

    def test_address_str(self):
        """
        Calling str method on Address return its number and street.
        """
        self.assertEqual(
            str(self.address),
            f'{self.address.number} {self.address.street}'
        )

    def test_letting_str(self):
        """
        Calling str method on Letting return its title.
        """
        self.assertEqual(
            str(self.letting),
            self.letting.title
        )
