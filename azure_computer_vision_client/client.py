import os, urllib

import requests

from azure_computer_vision_client.image_response import ImageResponse


class ComputerVisionClient(object):

    def __init__(self, region_name, subscription_key=None, env_variable='AZURE_COMPUTER_VISION_KEY'):
        subscription_key = subscription_key or os.environ.get(env_variable)
        if subscription_key is None:
            raise Exception("subscription_key is required")

        self.subscription_key = subscription_key
        self.region_name = region_name
        self.env_variable = env_variable

    def analyze_image_file(self, image_file, **kwargs):
        return self.analyze_image_bytes(open(image_file,'rb'), **kwargs)

    def analyze_image_bytes(self, bytes, **kwargs):
        return self.__analyze(
            files=dict(file=bytes),
            headers={
                'Ocp-Apim-Subscription-Key': self.subscription_key,
            },
            **kwargs
        )

    def analyze_image_url(self, image_url, **kwargs):
        return self.__analyze(
            json=dict(url=image_url),
            headers={
                'Content-Type': 'application/json',
                'Ocp-Apim-Subscription-Key': self.subscription_key,
            },
            **kwargs
        )

    def __analyze(self, visual_features=None, version='v1.0', **kwargs):
        params = dict(language='en')
        if visual_features:
            params.update(visual_features.as_dict())
        response = requests.post(
            'https://{0}.api.cognitive.microsoft.com/vision/{1}/analyze?{2}'.format(
                self.region_name,
                version,
                urllib.urlencode(params)
            ),
            **kwargs
        )
        if response.status_code != 200:
            response.raise_for_status()

        return ImageResponse(response.json())
