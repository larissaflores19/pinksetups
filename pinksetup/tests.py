from django.test import TestCase
from pinksetup.models import PinkSetup
from pinksetup.models import Favorites
from pinksetup.utils.model_testing import get_model_fields


class TestPinkSetupModels(TestCase):
    # testModelName (camel case)
    # test_model_name (snake case)

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


class TestFavoriteModel(TestCase):
    pass
    # def test_model_item_text(self):
    #     item_text = Favorites.objects.create(item_text='')
    #     self.assertEqual(str(item_text), '')
    #
    # def test_model_comment_text(self):
    #     comment_text = Favorites.objects.create(comment_text='')
    #     self.assertEqual(str(comment_text), '')
