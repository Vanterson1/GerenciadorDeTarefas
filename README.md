# Gerenciador de Tarefas com Listas Encadeadas em Python

## Descrição

Este é um projeto simples de gerenciador de tarefas implementado em Python utilizando listas encadeadas. O objetivo é permitir que os usuários adicionem, removam, marquem tarefas como concluídas e listem todas as tarefas, mantendo uma ordem baseada na prioridade das tarefas.

## Estrutura de Dados

.

```bash
O programa faz uso de uma lista encadeada para armazenar as tarefas. Cada nó da lista representa uma tarefa e contém informações sobre a tarefa (nome, prioridade, estado de conclusão) e uma referência para o próximo nó na lista.
class No:
    def __init__(self, tarefa, prioridade=0):
        self.tarefa = tarefa
        self.prioridade = prioridade
        self.proximo = None
        self.concluida = False

class GerenciadorTarefas:
    def __init__(self):
        self.inicio = None
    # Métodos para adicionar, remover, marcar como concluída e listar tarefas

```

## Requisitos

Certifique-se de ter o Python 3 ou superior instalado em seu sistema.

## Como Usar

Execute o código Python e siga as instruções. 


## Obersevações

Se necessário, ajuste as configurações no código para melhorar a visualização ou alterar o comportamento do programa.

## Autores

Vanterson Venancio Rodrigues - 170051579@aluno.unb.br

## Referências
[Vídeo 1](https://www.youtube.com/watch?v=jIM87UqOq3g)

[Vídeo 2](https://www.youtube.com/watch?v=EUUlB4Rmhf0)

[Vídeo 3](https://www.youtube.com/watch?v=QFvqStqPCRU&list=WL&index=10)