from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Tag
from recipe.serializers import TagSerializer


TAGS_URL = reverse('recipe:tag-list')


def create_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


class PublicTagApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(TAGS_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagApitTest(TestCase):

    def setUp(self):
        self.user = create_user(
            email='test@test.com',
            password='test123',
            name='test name'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_tages(self):
        Tag.objects.create(user=self.user, name='Vegan')
        Tag.objects.create(user=self.user, name='Dessert')

        res = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by('name')
        serializers = TagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializers.data)

    def test_limit_tag_user(self):
        user2 = create_user(
            email='test2@test.com',
            password='test1234',
            name='test2 name'
        )
        tag = Tag.objects.create(user=self.user, name='Vegan')
        Tag.objects.create(user=user2, name='Dessert')

        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)

    def test_create_tag_succesful(self):
        tag = {'name': 'vegan'}
        self.client.post(TAGS_URL, tag)

        exists = Tag.objects.filter(
            user=self.user,
            name=tag['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_tag_invalid_name(self):
        tag = {'name': ''}
        res = self.client.post(TAGS_URL, tag)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
