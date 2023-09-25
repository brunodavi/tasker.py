# TaskerPy

Ferramenta para criar automações no Android


## Pré Requisitos
- Tasker v6.2.0-beta
- Projeto TaskerPy no Tasker


## Inicio Rápido

### Instalação
```bash
pip install tasker.py
```

### Projeto TaskerPy Server
Esse projeto faz a comunicação
entre o Python e o Tasker

Pode ser importado [nesse link][tasker-py]

### Demonstração

```python
from tasker.py import TaskerPy, Task

from tasker.actions.alert import (
  Flash as Toast,
  Beep
)


app = TaskerPy()

# Mostra uma mensagem na tela e faz 3 beeps
@app.add_task(name='Mostrar Popup')
def hello_world(t: Task):
  yield Toast('Olá, Mundo', long=True)

  yield Beep(frequency=8_000, duration=100)
  yield Beep(frequency=9_000, duration=100)
  yield Beep(frequency=10_000, duration=100)


# Importa para o projeto e executa a ação
hello_world.play()

# Exporta o projeto em formato xml em:
# /sdcard/Tasker/tasks/Mostrar_Popup.tsk.xmll
hello_world.export()
```

### Como Contribuir
Depois de instalar o projeto vá em [Projects][gh-projects]
para ver as tarefas pendentes

Nesse projeto uso o `pdm` como gerenciador de pacotes

Para ativar no `.venv` tem que usar esse comando:

```bash
eval $(pdm venv activate)
```

### Scripts
Os scripts são criados no `pyproject.toml` como:
- test
- test-all
- docs
- lint
- format

#### Exemplo
```bash
# Testa sem depender do Android
pdm run test
```

ou

```bash
# Testa depdendo de um Android conectado
pdm test-all
```

### Conectar no Android
Se executar diretamente do celular ele já fica conectado

Para conectar o Android no projeto crie um `.env`
usando essa variável `TASKER_PY_ADDRESS` armazenando
o IP do seu aparelho


#### Exemplo
```bash
TASKER_PY_ADDRESS=192.168.1.25
```

#### Observações
Essa versão do Tasker com a função de servidor
está meio instável, então depois de importar o projeto
TaskerPy, clique em salvar (o botão de ✓),
em seguida, clique nos 3 pontinhos e em sair

[gh-projects]: https://github.com/users/brunodavi/projects/1
[tasker-py]: https://taskernet.com/shares/?user=AS35m8nXHtAHUb3g429CktIgI9aKlA1%2FEglWKHxy0IyPwx0q7aeQMBH2ekF4AG%2F7FRqn58T5R5q3qrGmIPwa&id=Project%3Atasker.py 
