from django.test import TestCase
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

    def test_create_address(self):
        """
        The Address object created is correctly registered in the
        database and its str method returns the expected value.
        """
        address_count = Address.objects.count()
        address = Address.objects.create(
            number=9606,
            street='Harvard Street',
            city='Aliquippa',
            state='PA',
            zip_code=15001,
            country_iso_code='USA'
        )
        self.assertEqual(
            Address.objects.count(),
            address_count + 1
        )
        self.assertEqual(
            Address.objects.last(),
            address
        )
        self.assertEqual(
            str(address),
            f'{address.number} {address.street}'
        )

    def test_create_letting(self):
        """
        The Letting object created is correctly registered in the
        database and its str method returns the expected value.
        """
        letting_count = Letting.objects.count()
        address = Address.objects.create(
            number=9606,
            street='Harvard Street',
            city='Aliquippa',
            state='PA',
            zip_code=15001,
            country_iso_code='USA'
        )
        letting = Letting.objects.create(
            title='The Mushroom Dome Retreat & LAND of Paradise Suite',
            address=address
        )
        self.assertEqual(
            Letting.objects.count(),
            letting_count + 1
        )
        self.assertEqual(
            Letting.objects.last(),
            letting
        )
        self.assertEqual(
            str(letting),
            letting.title
        )
