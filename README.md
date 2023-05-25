# TaskerPy

Automatize seu android com python


## Pré Requisitos
- Tasker e Projeto Importado ou App do TaskerPy
- Algum app com essa biblioteca instalada (ex: Termux, Qpython3, Pydroid e etc...)


## Guia Rápido

### Instalação

```bash
pip install tasker.py
```

### Demonstrações

Execute ações nativas do android pelo python

```python
#!/usr/bin/env python3
from tasker.actions.alert import Torch

# Cria um objeto para alterar as propriedades
torch = Torch(enabled=True)
torch.enabled = False

# Alterna entre ligado/desligado (True/False)
torch.toogle()

# Executa a ação
torch()
```

Crie tarefas e as execute de forma simples

```python
#!/usr/bin/env python3

from tasker.py import TaskerPy

from tasker.actions.alert import (
  Flash as Toast,
  Notification as Notify
)


app = TaskerPy()


@app.add_task(name='Mostrar Popup')
def hello_world():
  show_popup = Toast('Olá, Mundo')
  show_popup()


@app.add_task('Task to notify')
def notify_hello_world(title: str):
  notify = Notify(title, text='Um subtitulo')
  notify.priority = 5

  notify.add_button(
    label='Mostrar Mensagem',
    hello_world,
  )

  notify()

notify_hello_world('Notifique um olá, mundo')
```
