from django.contrib.auth.models import User
from django.test import TestCase
from pinksetup.models import PinkSetup, Post
from pinksetup.utils.model_testing import get_model_fields


class TestPinkSetupModels(TestCase):

    def test_model_name_str(self):
        pink_setup = PinkSetup.objects.create(name='Name Testing')
        self.assertEqual(str(pink_setup), 'Name Testing')

    def test_model_fields(self):
        NAME = 'Name Testing'
        DESCRIPTION = 'Description Test'

        pink_setup = PinkSetup.objects.create(name=NAME, description=DESCRIPTION, image=None)
        fields = get_model_fields(PinkSetup, pink_setup)

        self.assertEqual(fields.get('name'), NAME)
        self.assertEqual(fields.get('description'), DESCRIPTION)
        self.assertEqual(fields.get('image'), None)

    def test_post_like_users(self):
        testusers = User.objects.create_user(
            username='testuser', password='12345')
        testusers2 = User.objects.create_user(
            username='testuser2', password='12345')
        title = Post.objects.create(
            title='test', content='New Content')
        title.likes.set([testusers.pk, testusers2.pk])
        self.assertEqual(title.likes.count(), 2)
