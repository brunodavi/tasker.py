from tasker.py.profile_variable import ProfileVariable
from tasker.py.action import Action

from tasker.icons import Icon, NoneIcon
from tasker.types import Stream

from .xml_builder import XmlBuilder


class TaskXml(XmlBuilder):
    def __init__(self, task):
        self.task = task

    def _action_to_args(self, action: Action):
        E = self.E

        for index, key in enumerate(action.__match_args__):
            value = getattr(action, key)
            kwargs = {'sr': f'arg{index}'}

            match value:
                case '':
                    yield E.Str(**kwargs)
                case None:
                    yield E.Int(**kwargs)
                case NoneIcon():
                    yield E.Img(**kwargs)

                case Stream():
                    int_stream = int(value)
                    yield E.Int(
                            **kwargs,
                            val=str(int_stream),
                        )
                case Icon():
                    yield E.Img(
                            E.nme(value.name),
                            E.tint(str(value.color)),
                            **kwargs,
                        )

                case bool():
                    int_bool = int(value)
                    yield E.Int(**kwargs, val=str(int_bool))
                case int():
                    yield E.Int(**kwargs, val=str(value))
                case str():
                    yield E.Str(**kwargs, val=str(value), ve='3')

    def _actions_to_xml(self, *actions: Action):
        E = self.E

        for index, action in enumerate(actions):
            yield E.Action(
                E.code(f'{action._code_}'),
                *self._action_to_args(action),
                sr=f'act{index}',
                ve='7',
            )

    def _profile_variables_to_xml(self, *variables: ProfileVariable):
        E = self.E

        for index, variable in enumerate(variables):
            same_value = str(variable.same_value).lower()
            immutable = str(variable.immutable).lower()
            config_on_imported = str(variable.config_on_imported).lower()
            structure_variable = str(variable.structure_variable).lower()

            yield E.ProfileVariable(
                E.clearout(same_value),
                E.exportval(variable.exported_value),
                E.immutable(immutable),
                E.pvci(config_on_imported),
                E.pvd(variable.prompt),
                E.pvdn(variable.display),
                E.pvid(f'{self.task.id}'),
                E.pvit('t'),
                E.pvn(variable.variable_name),
                E.pvt(variable.config_type),
                E.pvv(variable.value),
                E.strout(structure_variable),

                sr=f'pv{index}',
            )

    def to_xml(self):
        E = self.E
    
        task_collision = int(self.task.collision)
        notify = str(self.task.notify).lower()
        awake = str(self.task.awake).lower()
        profile_variables = self.task.profile_variables

        icon = []

        if self.task.icon is not None:
            icon.push(self.task.icon)
    
        return E.Task(
                E.cdate('0'),
                E.edate('1'),
                E.id(f'{self.task.id}'),
                E.nme(self.task.name),
                E.pri(f'{self.task.priority}'),
                E.rty(f'{task_collision}'),
                E.showinnot(notify),
                E.stayawake(awake),
                
                *self._actions_to_xml(*self.task()),

                *icon,
                *self._profile_variables_to_xml(*profile_variables),

                sr='task',
            )
