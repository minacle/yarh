from .node import Node
from io import StringIO
import html

class Text(Node):

    def __init__(self, parent, indent, rawtext, inline=True, escape=True):
        super().__init__(parent, indent)
        self.rawtext = rawtext
        self.inline = inline
        self.escape = escape

    @property
    def text(self):
        childrenindent = " " * self.totalindent
        return self.rawtext[len(childrenindent):].replace("\n" + childrenindent, "\n")

    @text.setter
    def text(self, value):
        childrenindent = " " * self.totalindent
        self.rawtext = childrenindent + value.replace("\n", "\n" + childrenindent)

    def html(self):
        builder = StringIO()
        if self.inline:
            text = self.rawtext.strip()
            builder.write(html.escape(text) if self.escape else text)
        else:
            childrenindent = " " * (self.totalindent - self.indent)
            for line in self.text.split("\n"):
                builder.write(childrenindent)
                builder.write(line)
                builder.write("\n")
        result = builder.getvalue()
        builder.close()
        return result

    def yarh(self):
        return self.rawtext
