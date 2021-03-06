from .document import Document
from .node import Node
from io import StringIO
import html

void_elements = ["area", "base", "br", "col", "embed", "hr", "img", "input", "keygen", "link", "meta", "param", "source", "track", "wbr"]
raw_text_elements = ["script", "style"]
escapable_raw_text_elements = ["textarea", "title"]


class Element(Node):

    def __init__(self, parent, indent, tagname, idname="", classname=""):
        super().__init__(parent, indent)
        self.tagname = tagname
        self.idname = idname
        self.classname = classname
        self.attributes = []
        self.children = []

    def html(self):
        builder = StringIO()
        root = self.findparent(type=Document)
        before = self.before()
        inline = before and before.inlinenext or self.parent and isinstance(self.parent, Node) and self.parent.inlinechild or self.inline
        if not inline:
            builder.write(" " * self.totalindent)
        builder.write("<")
        builder.write(self.tagname)
        if self.idname:
            builder.write(' id="%s"' % self.idname)
        if self.classname:
            builder.write(' class="%s"' % self.classname)
        for attribute in self.attributes:
            builder.write(" ")
            builder.write(attribute.html())
        if root.isxhtml() and (self.isvoid() or not self.children):
            builder.write(" />")
        else:
            builder.write(">")
        if not self.isvoid():
            if self.children and not inline and not self.inlinechild:
                builder.write("\n")
            if self.children:
                for child in self.children:
                    builder.write(child.html())
                if builder.getvalue()[-1] == "\n":
                    builder.write(" " * self.totalindent)
            builder.write("</%s>" % self.tagname)
        if not (self.inline or self.inlinenext):
            builder.write("\n")
        result = builder.getvalue()
        builder.close()
        return result

    def yarh(self):
        pass

    def isvoid(self):
        return self.tagname.lower() in void_elements

    def isrt(self):
        return self.tagname.lower() in raw_text_elements

    def isert(self):
        return self.tagname.lower() in escapable_raw_text_elements
