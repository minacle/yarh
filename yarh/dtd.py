from .base import YarhBase

class DTD(YarhBase):

    def __init__(self, content, **kwargs):
        super().__init__(None)
        self.content = content

    def html(self):
        return "<!DOCTYPE %s>\n" % self.content

    def yarh(self):
        for k, v in doctypes.items():
            if self.content == v.content:
                return "!%s\n" % k
        return "!%s\n" % self.content

html4strict = DTD('HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"')
html4transitional = DTD('HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"')
html4frameset = DTD('HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd"')
xhtml11 = DTD('html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"')
html5 = DTD("html")

doctypes = {
    "strict": html4strict,
    "transitional": html4transitional,
    "frameset": html4frameset,
    "xhtml": xhtml11,
    "html": html5,
}
