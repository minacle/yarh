from .element import Element
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
        before = self.before()
        after = self.after()
        if self.inline or before and before.inlinenext or self.parent and isinstance(self.parent, Node) and self.parent.inlinechild:
            text = self.rawtext.strip()
            if self.escape:
                parent = self.findparent(type=Element)
                escape = True
                if parent:
                    escape = parent.isrt()
                builder.write(html.escape(text, quote=False) if escape else text)
            if after and (not after.inline or self.inlinenext):
                builder.write("\n")
        else:
            childrenindent = " " * (self.totalindent - self.indent)
            for line in self.text.split("\n"):
                builder.write(childrenindent)
                builder.write(line)
                builder.write("\n")
                first = False
        result = builder.getvalue()
        builder.close()
        return result

    def yarh(self):
        return self.rawtext
