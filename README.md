Azure Computer Vision Client
====================

Lightweight client for the [Azure Computer Vision API](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/).


## Usage

You can create a client to interact with the Vision API by doing:

```
from computer_vision_client import ComputerVisionClient
client = ComputerVisionClient('eastus2', 'subscription_key')
```

`subscription_key` is an optional parameter. If not supplied, the client will check for the environment variable `AZURE_COMPUTER_VISION_KEY`.

The methods `analyze_image_url` and `analyze_image_file` can be used to query the API:

```
# Returns ImageResponse object with only categories (default from API)
image_response = client.analyze_image_url('http://www.example.com/image')
```

An instance of `VisualFeatures` can be supplied to the `analyze` methods to return additional data from the API
```
# Returns ImageResponse object with faces and adult
image_response = client.analyze_image_url('http://www.example.com/image', VisualFeatures(faces=True, adult=True)
```

There is a default methond on `VisualFeatures` that returns an instance with all features set to `True`:
```
image_response = client.analyze_image_url('http://www.example.com/image', VisualFeatures.default())
```

## Tests

Tests require the environment variable to be set, and are hard-coded to use the `eastus2` region.
