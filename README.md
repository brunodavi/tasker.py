# TaskerPy

Ferramenta para criar automações no Android


## Pré Requisitos
- [Python][python-org] v3.10 ou superior
- [Tasker][tasker-trial] v6.2 ou superior
- Projeto [TaskerPy][tasker-py] no Tasker

## Inicio Rápido

### Instalação
```bash
pip install git+https://github.com/brunodavi/tasker.py
```

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
def hello_world():
  yield Toast('Olá, Mundo', long=True)

  yield Beep(frequency=8_000, duration=100)
  yield Beep(frequency=9_000, duration=100)
  yield Beep(frequency=10_000, duration=100)


# Importa para o projeto e executa a tarefa
hello_world.play()

# Exporta o projeto em formato xml em:
# /sdcard/Tasker/tasks/Mostrar_Popup.tsk.xml
hello_world.export()
```

## Como Contribuir
Depois de clonar o projeto vá em [Projects][gh-projects]
para ver as tarefas pendentes

Nesse projeto uso o [pdm][pdm-org] como gerenciador de pacotes

Como usar o `pdm`:

```sh
# Instala as dependências
pdm install

# Ativa o ambiente virtual
eval $(pdm venv activate)

# No Windows com PowerShell
Invoke-Expression (pdm venv activate)
```

### Scripts
Os scripts são criados no `pyproject.toml` como:
- test
- docs
- lint
- format

#### Exemplo
```bash
# Para testar o projeto
pdm test

# Obs: Conecte-se ao tasker.py no Tasker para testar as ações e testes unitários estão funcionando corretamente

# Caso só precise ignorar os testes das ações use:
pdm test -k 'not action'
```

### Conectar no Android
Se o tasker.py do Tasker estiver importado e for executado no celular ele já deve estar funcionando, por padrão o ip é `localhost`

Para conectar o Android no projeto fora do celular use o arquivo `.env`

Usando essa variável `TASKER_PY_ADDRESS` que armazena
o IP do seu aparelho

#### Exemplo
```env
TASKER_PY_ADDRESS=192.168.1.25
```

### Observações
Ao importar o projeto no Tasker, clique em salvar (o botão de ✓),
em seguida, clique nos 3 pontinhos e em sair

[python-org]: https://www.python.org
[pdm-org]: https://pdm-project.org
[tasker-trial]: https://tasker.joaoapps.com/download.html
[gh-projects]: https://github.com/users/brunodavi/projects/1
[tasker-py]: https://taskernet.com/shares/?user=AS35m8nXHtAHUb3g429CktIgI9aKlA1%2FEglWKHxy0IyPwx0q7aeQMBH2ekF4AG%2F7FRqn58T5R5q3qrGmIPwa&id=Project%3Atasker.py 
