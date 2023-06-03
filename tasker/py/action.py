from re import match

class Action:
    _NEW_INIT = (
        'lambda self, {params}: '
        '[ '
            'setattr(self, k, v) '
            'for k, v in locals().items() '
            'if self != v and v is not None '
        '] and None or None'
    )

    _is_context_creator = False


    def __init__(self, *args, **kwargs):
        cls = self.__class__
        params = self.__get_params(cls)

        if not len(params):
            raise AttributeError(
                'Nenhum parametro encontrado, '
                'defina um parâmetro na classe: '
                f'{cls.__name__}.'
            )

        cls.__init__ = self.__create_init(params)

    def __call__(self):
        if self._is_context_creator:
            return self.create_action()

        return self.take_action()

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
        result = []

        for key in vars(cls).keys():
            if self.__is_static(key):
                result.append(key)

        return result

    def __is_static(self, attr_name: str):
        result = match(
            r'^[A-Za-z0-9][A-Za-z_0-9]*[A-Za-z0-9]?$',
            attr_name
        )

        not_is_dunder_and_is_alphanum = (
            result is not None
        )

        return not_is_dunder_and_is_alphanum


    def create_action(self):
        return None

    def take_action(self):
        return None
