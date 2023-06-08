from re import match

class Action:
    _is_context_creator = False


    def __init__(self, *args, **kwargs):
        cls = self.__class__

        props, max_props = self.__get_props(cls)
        max_args = len(args)

        if max_args > max_props:
            raise IndexError(
                f"{max_args} passou do limite "
                f"de propriedades ({max_props})"
            )

        for index, arg in enumerate(args):
            key = props[index]
            setattr(self, key, arg)

        for index, key in enumerate(kwargs):
            if key in props:
                arg = kwargs[key]
                setattr(self, key, arg)
            else:
                raise KeyError(
                    f"'{key}' não existe como "
                    "propriedade dessa ação."
                )


    def __get_props(self, cls):
        props = []

        all_props = vars(cls).keys()
        all_props = tuple(all_props)
        all_props = all_props[1:-1]

        for key in all_props:
            if self.__is_static(key):
                props.append(key)
            else:
                delattr(cls, key)

        max_props = len(props)

        if not max_props:
            raise AttributeError(
                'Nenhum parametro encontrado, '
                'defina um parâmetro na classe: '
                f'{cls.__name__}.'
            )

        return props, max_props

    def __is_static(self, attr_name: str):
        result = match(
            r'^[A-Za-z0-9][A-Za-z_0-9]*[A-Za-z0-9]?$',
            attr_name
        )

        not_is_dunder_and_is_alphanum = (
            result is not None
        )

        return not_is_dunder_and_is_alphanum


    def add_action(self):
        ...
