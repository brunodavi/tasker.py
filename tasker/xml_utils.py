from dataclasses import astuple

from lxml.builder import E

from tasker.py import Action
from tasker import Stream


class XmlUtils:
   def _create_data(self, *datas: E):
      return E.TaskerData(*datas, sr="", dvi="1")
   
   def _action_to_args(self, action: Action):
      action_args = astuple(action)

      for index, value in enumerate(action_args):
            kwargs = {'sr': f"arg{index}"}

            match value:
               case Stream():
                  int_stream = int(value)
                  yield E.Int(**kwargs, val=str(int_stream))
               case int():
                  yield E.Int(**kwargs, val=str(value))
               case str():
                  yield E.Str(**kwargs, val=str(value))

   def _actions_to_xml(self, *actions: Action):
      for index, action in enumerate(actions):
         if isinstance(action, tuple):
            [action] = action

         yield E.Action(
               E.code(f'{action._code_}'),
               *self._action_to_args(action),

               sr=f"act{index}",
               ve="7"
         )                    


   def create_task(self, task_id: int, task_name: str, *actions: Action):
      return self._create_data(
            E.Task(
               E.id(f'{task_id}'),
               E.nme(task_name),
               *self._actions_to_xml(actions),

               sr=f"task{task_id}"
            )
         )
