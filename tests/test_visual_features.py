from unittest import TestCase

from azure_computer_vision_client import VisualFeatures


class TestVisualFeatures(TestCase):

    def test_as_dict_with_one_feature(self):
        self.assertEqual(
            VisualFeatures(categories=True).as_dict(),
            {'visualFeatures': 'Categories'}
        )

    def test_as_dict_with_multiple_feature(self):
        self.assertEqual(
            VisualFeatures(categories=True, tags=True).as_dict(),
            {'visualFeatures': 'Tags,Categories'}
        )