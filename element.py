from .node import Node
from io import StringIO
import html

class Element(Node):

    def __init__(self, parent, indent, tagname, idname="", classname="", name=""):
        super().__init__(parent, indent)
        self.tagname = tagname
        self.idname = idname
        self.classname = classname
        self.name = name
        self.attributes = []
        self.children = []
        self.inline = False

    def html(self):
        builder = StringIO()
        if not self.inline:
            builder.write(" " * self.totalindent)
        builder.write("<")
        builder.write(self.tagname)
        if self.idname:
            builder.write(' id="%s"' % self.idname)
        if self.classname:
            builder.write(' class="%s"' % self.classname)
        if self.name:
            builder.write(' name="%s"' % self.name)
        for attribute in self.attributes:
            builder.write(" ")
            builder.write(attribute.html())
        if self.children:
            builder.write(">")
            for child in self.children:
                if not child.inline and builder.getvalue()[-1] != "\n":
                    builder.write("\n")
                builder.write(child.html())
            #builder.write("\n")
            if builder.getvalue()[-1] == "\n":
                builder.write(" " * self.totalindent)
            builder.write("</%s>" % self.tagname)
        else:
            builder.write(" />")
        if not self.inline:
            builder.write("\n")
        result = builder.getvalue()
        builder.close()
        return result

    def yarh(self):
        pass
