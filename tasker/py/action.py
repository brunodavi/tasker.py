from re import match

from tasker.client import TaskerClient

class Action:
    def __call__(self, *args, **kwargs):
        cls = self.__class__
        module = cls.__module__

        (*_, category, action) = (
            module.split('.')
        )

        path = f'/{category}/{action}'
        data = self.__seralize_to_dict()

        tasker_client = TaskerClient()
        return tasker_client.post(path, json=data)


    def __get_props(self):
        props = []

        all_props = vars(self).keys()

        for key in all_props:
            if self.__is_static(key):
                props.append(key)

        return props

    def __is_static(self, attr_name: str):
        result = match(
            r'^[A-Za-z0-9][A-Za-z_0-9]*[A-Za-z0-9]?$',
            attr_name
        )

        not_dunder_and_is_alphanum = (
            result is not None
        )

        return not_dunder_and_is_alphanum


    def __seralize_to_dict(self):
        props = self.__get_props()
        data = {}

        for prop in props:
            data[prop] = getattr(self, prop)

        return data


    def add_action(self):
        ...
