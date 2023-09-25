from enum import Enum


class TaskCollision(int, Enum):
    """
    Configuração do fluxo de colisões entre tarefas

    ---

    O que fazer ao executar a mesma tarefas mais de uma vez
    """

    ABORT_NEW_TASK = 0
    ABORT_EXISTING_TASK = 1
    RUN_BOTH_TOGETHER = 2
