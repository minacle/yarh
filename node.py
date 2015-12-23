from .base import YarhBase

class Node(YarhBase):

    def __init__(self, parent, indent):
        super().__init__(parent)
        self.indent = indent if indent > 0 else 0

    @property
    def level(self):
        return 1 + (self.parent.level if self.parent else 0)

    @property
    def totalindent(self):
        return self.indent + (self.parent.totalindent if self.parent else 0)
