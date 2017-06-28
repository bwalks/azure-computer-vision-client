from mock import patch
from unittest import TestCase

from computer_vision_client import ComputerVisionClient, VisualFeatures


class TestClient(TestCase):

    def setUp(self):
        # Requires AZURE_COMPUTER_VISION_KEY environment variable to be set.
        self.client = ComputerVisionClient('eastus2')
        self.image_url = 'https://upload.wikimedia.org/wikipedia/commons/1/12/Broadway_and_Times_Square_by_night.jpg'

    def test_client_with_no_features(self):
        image_response = self.client.analyze_image_url(self.image_url)
        self.assertIsNotNone(image_response)
        self.assertIn('categories', image_response.data)
        self.assertIn('metadata', image_response.data)

        self.assertNotIn('faces', image_response.data)
        self.assertNotIn('adult', image_response.data)
        self.assertNotIn('tags', image_response.data)
        self.assertNotIn('description', image_response.data)
        self.assertNotIn('imageType', image_response.data)
        self.assertNotIn('color', image_response.data)
        self.assertNotIn('detail', image_response.data)

    def test_client_without_subscription_key(self):
        test_env_variable = 'DIFFERENT_VARIBLE_FOR_TEST'
        with patch('computer_vision_client.client.ComputerVisionClient.ENVIRONMENT_VARIABLE',
                   new=test_env_variable):
            with self.assertRaises(Exception) as cm:
                ComputerVisionClient('eastus2')
            self.assertEqual(
                cm.exception.message,
                "subscription_key is required as a parameter or as the environment variable {}"
                    .format(test_env_variable)
            )

    def test_client_with_invalid_region(self):
        with self.assertRaises(Exception) as cm:
            ComputerVisionClient('wrong_region', 'key')
        self.assertEqual(cm.exception.message, "wrong_region is not a supported region")

    def test_client_with_visual_features(self):
        image_response = self.client.analyze_image_url(self.image_url, VisualFeatures.default())

        self.assertIsNotNone(image_response)
        self.assertIn('faces', image_response.data)
        self.assertIn('adult', image_response.data)
        self.assertIn('categories', image_response.data)
        self.assertIn('tags', image_response.data)
        self.assertIn('description', image_response.data)
        self.assertIn('imageType', image_response.data)
        self.assertIn('color', image_response.data)

    def test_client_with_limited_visual_features(self):
        image_response = self.client.analyze_image_url(
            self.image_url, VisualFeatures(adult=True, faces=True))

        self.assertIsNotNone(image_response)
        self.assertIn('faces', image_response.data)
        self.assertIn('adult', image_response.data)

        self.assertNotIn('categories', image_response.data)
        self.assertNotIn('tags', image_response.data)
        self.assertNotIn('description', image_response.data)
        self.assertNotIn('imageType', image_response.data)
        self.assertNotIn('color', image_response.data)

    def test_analyze_image_file(self):
        image_response = self.client.analyze_image_file('image.jpg')
