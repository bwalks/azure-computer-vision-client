class VisualFeatures(object):

    option_name = 'visualFeatures'

    def __init__(self,
                 categories=False,
                 tags=False,
                 description=False,
                 faces=False,
                 image_type=False,
                 color=False,
                 adult=False):
        self.props = dict(
            Categories=categories,
            Tags=tags,
            Description=description,
            Faces=faces,
            ImageType=image_type,
            Color=color,
            Adult=adult
        )

    def as_dict(self):
        filtered_props = [prop for prop, value in self.props.iteritems() if value]
        if filtered_props:
            return { self.option_name: ",".join(filtered_props) }

    @staticmethod
    def default():
        return VisualFeatures(
            categories=True,
            tags=True,
            description=True,
            faces=True,
            image_type=True,
            color=True,
            adult=True
        )
