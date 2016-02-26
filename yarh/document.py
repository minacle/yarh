from .base import YarhBase
from io import StringIO


class Document(YarhBase):

    def __init__(self, dtd):
        super().__init__(None)
        self.dtd = dtd
        self.children = []

    @property
    def level(self):
        return 0

    @property
    def totalindent(self):
        return 0

    def html(self):
        builder = StringIO()
        builder.write(self.dtd.html())
        for child in self.children:
            builder.write(child.html())
        result = builder.getvalue()
        builder.close()
        return result

    def yarh(self):
        builder = StringIO()
        builder.write(self.dtd.yarh)
        for child in self.children:
            builder.write(child.yarh())
        result = builder.getvalue()
        builder.close()
        return result

    def isxhtml(self):
        if "http://www.w3.org/TR/xhtml" in self.dtd.content:
            return True
        return False
