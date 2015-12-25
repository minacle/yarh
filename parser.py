from .attribute import Attribute
from .comment import Comment
from .document import Document
from .dtd import DTD, doctypes
from .element import Element
from .text import Text
import re

re_indent = re.compile(r"^ +")
re_dtd = re.compile(r"^!(?P<dtd>.*)")
re_tag = re.compile(r"^(?P<tag>[A-Za-z_][\w-]*)")
re_id = re.compile(r"^#(?P<id>[A-Za-z_][\w-]*)")
re_class = re.compile(r"^\.(?P<class>[A-Za-z_][\w-]*)")
re_attrib = re.compile(r"^(?P<key>[A-Za-z_][\w-]*)(?:=(\"|')(?P<value>.*?)\2)?")
re_scrap = re.compile(r"^(\"|')(?P<scrap>.*?)?\1")

def parseyarh(data):
    lines = data.split("\n")
    root = None
    stack = []
    for line in lines:
        origin = line
        match = re_indent.match(line)
        lineindent = len(match.group(0)) if match else 0
        if not lineindent:
            stack = []
        while stack and sum(item[0] for item in stack) >= lineindent:
            del stack[-1]
        line = line[lineindent:]
        indent = lineindent - sum(item[0] for item in stack)
        parent = stack[-1][1] if stack else None
        node = None
        if isinstance(parent, (Text, Comment)):
            if parent.rawtext.strip():
                parent.rawtext += "\n" + " " * (lineindent) + line
            else:
                parent.rawtext = " " * (lineindent) + line
        else:
            inline = False
            while line:
                if not root:
                    if line.startswith("!"): #dtd
                        text = line[1:].strip()
                        if text in doctypes:
                            dtd = doctypes[text]
                        else:
                            dtd = DTD(text)
                        root = Document(dtd)
                        line = ""
                    else:
                        root = Document(doctypes["html"])
                if line.startswith(":"): #text
                    if node:
                        node.inlinechild = True
                        if parent:
                            parent.children.append(node)
                        else:
                            root.children.append(node)
                        stack.append((indent, node))
                        parent = node
                        inline = True
                    node = Text(parent, indent, " " * (lineindent + indent) + line[1:].strip(), inline=inline)
                    line = ""
                elif line.startswith("-"): #comment
                    if node:
                        if parent:
                            parent.children.append(node)
                        else:
                            root.children.append(node)
                        stack.append((indent, node))
                        parent = node
                        inline = True
                    node = Comment(parent, indent, " " * (lineindent + indent) + line[1:], inline=inline)
                    if node.rawtext.strip():
                        node.inline = True
                    line = ""
                elif line.startswith("#"): #id
                    match = re_id.match(line)
                    if not match:
                        line = line[1:].lstrip()
                        continue
                    if node:
                        node.idname = match.group("id")
                    else:
                        node = Element(parent, indent, "div", idname=match.group("id"))
                    line = line[len(match.group(0)):]
                elif line.startswith("."): #class
                    match = re_class.match(line)
                    if not match:
                        line = line[1:].lstrip()
                        continue
                    if node:
                        node.classname = (node.classname + " " + match.group("class")).lstrip()
                    else:
                        node = Element(parent, indent, "div", classname=match.group("class"))
                    line = line[len(match.group(0)):]
                elif line.startswith(";"): #inline
                    if node:
                        node.inlinechild = True
                        if parent:
                            parent.children.append(node)
                        else:
                            root.children.append(node)
                        stack.append((indent, node))
                        parent = node
                        node = None
                    elif parent:
                        parent.inlinenext = True
                        del stack[-1]
                        if stack:
                            parent = stack[-1][1]
                        else:
                            parent = None
                    inline = True
                    line = line[1:]
                elif line.startswith("'") or line.startswith('"'): #scrap
                    if node:
                        if parent:
                            parent.children.append(node)
                        else:
                            root.children.append(node)
                        stack.append((indent, node))
                        parent = node
                        node = None
                    match = re_scrap.match(line)
                    if not match:
                        line = line[1:].lstrip()
                        continue
                    inline = True
                    parent.children.append(Text(parent, 0, match.group("scrap"), inline=inline))
                    line = line[len(match.group(0)):]
                else:
                    if not node:
                        match = re_tag.match(line)
                        if not match:
                            line = line[1:].lstrip()
                            continue
                        node = Element(parent, indent, match.group("tag"))
                        node.inline = inline
                    else:
                        match = re_attrib.match(line)
                        if not match:
                            line = line[1:].lstrip()
                            continue
                        node.attributes.append(Attribute(node, match.group("key"), match.group("value")))
                    line = line[len(match.group(0)):]
        if node:
            if parent:
                parent.children.append(node)
            else:
                root.children.append(node)
            stack.append((indent, node))
    return root
