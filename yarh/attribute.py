from .base import YarhBase
import html


class Attribute(YarhBase):

    def __init__(self, parent, key, value=None):
        super().__init__(parent)
        self.key = key
        self.value = value

    def html(self):
        if self.value:
            return '{0}="{1}"'.format(self.key, html.escape(self.value, quote=True))
        else:
            return '{0}'.format(self.key)

    def yarh(self):
        if self.value:
            return '{0}="{1}"'.format(self.key, html.escape(self.value, quote=True))
        else:
            return '{0}'.format(self.key)
