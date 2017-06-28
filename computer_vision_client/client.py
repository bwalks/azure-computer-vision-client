import os, urllib

import requests

from computer_vision_client.image_response import ImageResponse

class ComputerVisionClient(object):

    ENVIRONMENT_VARIABLE = 'AZURE_COMPUTER_VISION_KEY'
    SUPPORTED_REGIONS = frozenset(
        ['eastus2', 'westus', 'westcentralus', 'westeurope', 'southeastasia']
    )

    def __init__(self, region_name, subscription_key=None):
        if subscription_key is None:
            subscription_key = os.environ.get(self.ENVIRONMENT_VARIABLE)

        if subscription_key is None:
            raise Exception(
                "subscription_key is required as a parameter or as the environment variable {}"
                    .format(self.ENVIRONMENT_VARIABLE))

        if region_name not in self.SUPPORTED_REGIONS:
            raise Exception("{0} is not a supported region".format(region_name))

        self.subscription_key = subscription_key
        self.region_name = region_name
        self.headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': subscription_key,
        }

    def analyze_image_file(self, image_file, visual_features=None, version='v1.0'):
        return self._analyze(
            visual_features=visual_features,
            version=version,
            files=dict(file=open(image_file,'rb'))
        )

    def analyze_image_url(self, image_url, visual_features=None, version='v1.0'):
        return self._analyze(
            visual_features=visual_features,
            version=version,
            json=dict(url=image_url)
        )

    def _analyze(self, visual_features=None, version='v1.0', **kwargs):
        params = dict(language='en')
        if visual_features:
            params.update(visual_features.as_dict())
        response = requests.post(
            'https://{0}.api.cognitive.microsoft.com/vision/{1}/analyze?{2}'.format(
                self.region_name,
                version,
                urllib.urlencode(params)
            ),
            headers=self.headers,
            **kwargs
        )
        if response.status_code != 200:
            response.raise_for_status()

        return ImageResponse(response.json())
