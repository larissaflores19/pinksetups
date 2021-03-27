from pprint import pprint

from django.test import TestCase
from pinksetup.models import PinkSetup, Post
from pinksetup.utils.model_testing import get_model_fields
from model_bakery import baker


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


class TestNew(TestCase):
    def setUp(self):
        self.post = baker.make('pinksetup.Post')
        pprint(self.post.__dict__)

    def test_model_str(self):
        title = Post.objects.create(title='django test')
        content = Post.objects.create(content='this is some content')
        self.assertEqual(str(title), 'django test')

