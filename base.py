class YarhBase:

    def __init__(self, parent):
        self.parent = parent

    def html(self):
        raise NotImplementedError()

    def yarh(self):
        raise NotImplementedError()

    def findparent(self, **kwargs):
        keys = ["type"]
        findable = False
        for kwarg in kwargs:
            if kwarg in keys:
                findable = True
                break
        if not findable:
            return self.parent
        #type
        if isinstance(self.parent, kwargs["type"]):
            return self.parent
        elif self.parent:
            return self.parent.findparent(**kwargs)
        #i have no parent...
        return None
