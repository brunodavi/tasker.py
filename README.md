# TaskerPy

Ferramenta para programar automações do Tasker pelo python


## Pré Requisitos
- Python3.7 ou superior
- Tasker e Projeto Importado ou App do tasker.py
- App com essa biblioteca instalada (ex: Termux, Qpython3, Pydroid e etc...)


## Guia Rápido

### Instalação

```bash
pip install tasker.py
```

### Demonstrações

- [ ] Crie tarefas e as execute de forma simples

```python
from tasker.py import TaskerPy, Task
from tasker.actions.alert import Flash


app = TaskerPy()


@app.add_task(name='Mostrar Popup')
def hello_world(t: Task):
  yield Flash('Olá, mundo', long=True)


# Importa a tarefa temporária e a executa
hello_world.play()
```

- [ ] Sincronizar Projetos

```python
from tasker.py import TaskerPy, Task
from tasker.actions.alert import Flash


app = TaskerPy()
project_demo = app.add_project('Project Demo')


@project_demo.add_profile.time(
  name='10h at 12h',
  start='10:00',
  end='12:00',
)
@project_demo.add_task('Alert')
def alert(t: Task):
  yield Flash('Alerting...')
  yield Beep(1000, 100)


# Sincroniza os arquivos do Tasker
# Adicionando/alterando os  projetos, tarefas, perfis e etc...
app.sync()
```