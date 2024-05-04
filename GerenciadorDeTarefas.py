class No:
    def __init__(self, tarefa, prioridade=0):
        self.tarefa = tarefa
        self.prioridade = prioridade
        self.proximo = None
        self.concluida = False

class GerenciadorTarefas:
    def __init__(self):
        self.inicio = None

    def adicionar_tarefa(self, tarefa, prioridade=0):
        novo_no = No(tarefa, prioridade)
        if self.inicio is None or self.inicio.prioridade < prioridade:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo and atual.proximo.prioridade >= prioridade:
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

    def remover_tarefa(self, tarefa):
        atual = self.inicio
        anterior = None
        while atual:
            if atual.tarefa == tarefa:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def marcar_concluida(self, tarefa):
        atual = self.inicio
        while atual:
            if atual.tarefa == tarefa:
                atual.concluida = True
                return True
            atual = atual.proximo
        return False

    def listar_tarefas(self):
        tarefas = []
        atual = self.inicio
        while atual:
            status = "Concluída" if atual.concluida else "Pendente"
            tarefas.append(f"{atual.tarefa} (Prioridade: {atual.prioridade}, Status: {status})")
            atual = atual.proximo
        return tarefas

def executar_gerenciador_tarefas():
    gerenciador = GerenciadorTarefas()

    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Marcar Tarefa Como Concluída")
        print("4. Listar Tarefas")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tarefa = input("Digite a tarefa: ")
            prioridade = int(input("Digite a prioridade (maior número = maior prioridade): "))
            gerenciador.adicionar_tarefa(tarefa, prioridade)
            print(f"Tarefa '{tarefa}' adicionada com sucesso.")

        elif escolha == '2':
            tarefa = input("Digite a tarefa a ser removida: ")
            if gerenciador.remover_tarefa(tarefa):
                print(f"Tarefa '{tarefa}' removida com sucesso.")
            else:
                print("Tarefa não encontrada.")

        elif escolha == '3':
            tarefa = input("Digite a tarefa que foi concluída: ")
            if gerenciador.marcar_concluida(tarefa):
                print(f"Tarefa '{tarefa}' marcada como concluída.")
            else:
                print("Tarefa não encontrada.")

        elif escolha == '4':
            tarefas = gerenciador.listar_tarefas()
            print("\nListas de Tarefas:")
            for tarefa in tarefas:
                print(tarefa)

        elif escolha == '5':
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 5.")

executar_gerenciador_tarefas()