class Track:
    def __init__(self, path, event_data):
        self.path = path
        self.event_data = event_data

    def __iter__(self):
        # first start by grabbing the Class items
        iters = dict((x, y) for x, y in Track.__dict__.items() if x[:2] != '__')

        # then update the class items with the instance items
        iters.update(self.__dict__)

        # now 'yield' through the items
        for x, y in iters.items():
            yield x, y