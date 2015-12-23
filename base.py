class YarhBase:

    def __init__(self, parent):
        self.parent = parent

    def html(self):
        raise NotImplementedError()

    def yarh(self):
        raise NotImplementedError()
