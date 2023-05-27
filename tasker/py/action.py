class Action:
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
        params = self.__get_params(cls)

        if not len(params):
            raise AttributeError(
                'Nenhum parametro encontrado, '
                'defina um parâmetro na classe: '
                f'{cls.__name__}.'
            )

        cls.__init__ = self.__create_init(params)


    def __create_init(self, params):
        serialized_params = (
            self
            .__serialize_params(params)
        )

        code = (
            self
            ._NEW_INIT
            .format(params=serialized_params)
        )

        new_init = eval(code, {}, {})
        new_init.__name__ = '__init__'

        return new_init

    def __serialize_params(self, params):
        params = map(
            lambda key: f'{key}=None',
            params,
        )

        params = ', '.join(params)

        return params

    def __get_params(self, cls):
        return [
            key
            for key in vars(cls).keys()
            if self.__is_static(key)
        ]

    def __is_static(self, attr_name):
        not_dunder = attr_name[0] != '_'
        is_alpha_numeric = attr_name.isalnum()

        return (
            not_dunder
            and
            is_alpha_numeric
        )
