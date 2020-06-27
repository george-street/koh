from functools import partial
from yaml import load, Loader


class Parser:
    def __init__(self, content, parser=partial(load, Loader=Loader)):
        self.content = parser(content)

    @classmethod
    def from_file(cls, path, parser=partial(load, Loader=Loader)):
        with open(path, 'r') as f:
            return cls(f.read(), parser)
