from .node import Node
from io import StringIO
import re

class Comment(Node):

    def __init__(self, parent, indent, rawtext, inline=True, escape=True):
        super().__init__(parent, indent)
        self.rawtext = rawtext.replace("--/>", "-->") if escape else rawtext
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
        baseindent = " " * (self.totalindent - self.indent)
        builder.write(baseindent)
        builder.write("<!--")
        if self.inline:
            text = self.rawtext.rstrip()
            space = " " * (len(text) - len(text.lstrip(" ")))
            builder.write(text.replace("-->", "--/>") if self.escape else text)
            builder.write(space)
        else:
            childrenindent = baseindent + " " * self.indent
            builder.write("\n")
            for line in self.text.split("\n"):
                builder.write(childrenindent)
                builder.write(line)
                builder.write("\n")
            builder.write(baseindent)
        builder.write("-->\n")
        result = builder.getvalue()
        builder.close()
        return result

    def yarh(self):
        raise NotImplementedError()
