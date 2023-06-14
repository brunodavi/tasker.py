# TaskerPy

Automatize seu Android com Python3 + Tasker


## Pré Requisitos
- Tasker e Projeto Importado ou App do TaskerPy
- Algum app com essa biblioteca instalada (ex: Termux, Qpython3, Pydroid e etc...)


## Guia Rápido

### Instalação

```bash
pip install tasker.py
```

### Demonstrações

Crie tarefas e as execute de forma simples

```python
#!/usr/bin/env python3

from tasker.py import TaskerPy

from tasker.actions.alert import (
  Flash as Toast,
  Notify
)


app = TaskerPy()


@app.add_task(name='Mostrar Popup')
def hello_world():
  show_popup = Toast('Olá, Mundo')
  show_popup.long = True

  show_popup.add_action()


@app.add_task('Tarefa para notificar')
def notify_hello_world(title: str):
  notify = Notify(title, text='Um subtitulo')
  notify.priority = 5

  notify.add_button1(
    label='Mostrar Mensagem',
    hello_world,
  )

  notify.add_action()

notify_hello_world('Notifique um olá, mundo')
```

Exporte tarefas do TaskerPy

```python
#!/usr/bin/env python3

from tasker.py import TaskerPy

from tasker.actions.alert import (
  Flash as Toast
)


app = TaskerPy()

@app.add_task()
def task():
    toast = Toast('Olá')
    toast.long = True

    toast.add_action()

# Exporta a tarefa para /sdcard/Tasker/tasks/task.tsk.xml
task.export_xml()
```
