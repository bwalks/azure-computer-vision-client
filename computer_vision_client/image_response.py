class ImageResponse(object):

    def __init__(self, data):
        self.data = data

    @property
    def is_racy_content(self):
        return self.data.get('adult', {}).get('isRacyContent', None)

    @property
    def is_adult_content(self):
        return self.data.get('adult', {}).get('isAdultContent', None)

    @property
    def categories(self):
        return self.data.get('categories', [])

    @property
    def tags(self):
        return self.data.get('tags', [])

    @property
    def metadata(self):
        return self.data.get('metadata', {})

    @property
    def color(self):
        return self.data.get('color', {})

    @property
    def description(self):
        return self.data.get('description', {})
