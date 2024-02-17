def meta_attr(func: callable):
    class Meta(type):
        def __getattribute__(cls, name):
            return func(super().__getattribute__(name))

    return Meta
