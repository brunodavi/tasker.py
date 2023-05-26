class Action:
    _params = {}

    _NEW_INIT = (
        'lambda self, {params}: '
        '[ '
            'setattr(self, k, v) '
            'for k, v in locals().items() '
            'if self != v and v is not None '
        '] and None or None'
    )


    def __init__(self):
        cls = self.__class__
        attrs =  vars(cls)

        for key, value in attrs.items():
            if self.__is_static(key, value):
                cls._params[key] = value

        if not len(cls._params):
            raise AttributeError(
                'Nenhum parametro encontrado, '
                'defina um parâmetro na classe: '
                f'{cls.__name__}.'
            )

    # def __new__(cls):
        params = cls._params.keys()
        params = map(
            lambda key: f'{key}=None',
            params,
        )

        params = ', '.join(params)

        code = (
            cls
                ._NEW_INIT
                .format(params=params)
        )

        __new_init = eval(code, {}, {})
        __new_init.__name__ = '__init__'

        cls.__init__ = __new_init


    def __is_static(self, attr_name, attr_value):
        not_dunder = attr_name[0] != '_'
        is_alpha_numeric = attr_name.isalnum()

        return (
            not_dunder
            and
            is_alpha_numeric
        )
