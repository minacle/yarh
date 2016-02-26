from .base import YarhBase


class Node(YarhBase):

    def __init__(self, parent, indent):
        super().__init__(parent)
        self.indent = indent if indent > 0 else 0
        self.inline = False
        self.inlinenext = False
        self.inlinechild = False

    @property
    def level(self):
        return 1 + (self.parent.level if self.parent else 0)

    @property
    def totalindent(self):
        return self.indent + (self.parent.totalindent if self.parent else 0)

    def before(self):
        last = None
        if self.parent:
            for child in self.parent.children:
                if child is self:
                    return last
                last = child

    def after(self):
        last = None
        if self.parent:
            for child in reversed(self.parent.children):
                if child is self:
                    return last
                last = child
