from functools import partial
from yaml import load, Loader


class Parser:
    @classmethod
    def parse(cls, content, parser=partial(load, Loader=Loader)):
        return parser(content)

    @classmethod
    def from_file(cls, path, parser=partial(load, Loader=Loader)):
        with open(path, 'r') as f:
            return cls.parse(f.read(), parser)
