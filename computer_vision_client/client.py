import os, urllib

import requests

from computer_vision_client.image_response import ImageResponse


class ComputerVisionClient(object):

    ENVIRONMENT_VARIABLE = 'AZURE_COMPUTER_VISION_KEY'

    def __init__(self, region_name, subscription_key=None):
        subscription_key = subscription_key or os.environ.get(self.ENVIRONMENT_VARIABLE)
        if subscription_key is None:
            raise Exception(
                "subscription_key is required as a parameter or as the environment variable {}"
                    .format(self.ENVIRONMENT_VARIABLE))

        self.subscription_key = subscription_key
        self.region_name = region_name

    def analyze_image_file(self, image_file, **kwargs):
        return self.__analyze(
            files=dict(file=open(image_file,'rb')),
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
