from django.test import TestCase, override_settings
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from profiles.models import Profile


User = get_user_model()


# overide WHITENOISE_AUTOREFRESH to avoid getting warnings about
# 'No directory at {}' for STATIC_ROOT directory
@override_settings(WHITENOISE_AUTOREFRESH=True)
class BaseTestCase(TestCase):
    """
    Custom TestCase class with fixtures.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Class level test data.
        """
        cls.user = User.objects.create_user(
            username='username'
        )
        cls.profile = Profile.objects.create(
            user=cls.user,
            favorite_city='favorite_city'
        )


class TestProfilesView(BaseTestCase):
    """
    Profiles views test class.
    """
    url_list = reverse_lazy('profiles:index')
    url_detail = reverse_lazy('profiles:profile', args=('username',))

    def test_list_view(self):
        """
        GET on url_list rendrers the page with status code 200,
        the expected context data and the right templates.
        """
        templates_expected = [
            'profiles/index.html',
            'base.html'
        ]
        response = self.client.get(self.url_list)
        templates_used = [template.name for template in response.templates]

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertQuerysetEqual(
            response.context.get('profiles_list', None),
            Profile.objects.all(),
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
            'profiles/profile.html',
            'base.html'
        ]
        response = self.client.get(self.url_detail)
        templates_used = [template.name for template in response.templates]

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            response.context.get('profile', None),
            self.profile
        )
        self.assertEqual(
            templates_used,
            templates_expected
        )


class TestProfilesModels(BaseTestCase):
    """
    Lettings models test class.
    """

    def test_create_profile(self):
        """
        The Profile object created is correctly registered in the
        database and its str method returns the expected value.
        """
        profile_count = Profile.objects.count()
        user = User.objects.create_user(
            username='test_user'
        )
        profile = Profile.objects.create(
            user=user,
            favorite_city='test_favorite_city'
        )
        self.assertEqual(
            Profile.objects.count(),
            profile_count + 1
        )
        self.assertEqual(
            Profile.objects.last(),
            profile
        )
        self.assertEqual(
            str(profile),
            f'{profile.user.username}'
        )
