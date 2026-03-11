from repositoriotarefas import RepositorioTarefas
from controladordetarefas import Controladordetarefas
from tarefa import tarefa
from autenticadorTarefa import Autenticador
from impressao import impressao

class main:
    def __init__(self):
        self.repositorio = RepositorioTarefas()

    def main(self):
        self.repositorio.criacaoTabelaTarefa()
        while True:
            print("-"*50)
            print("O que você deseja fazer?\n[1]Criar [2]Editar [3]Excluir [4]Listar")
            x = int(input(">>  "))

            if x == 1:
                self.criaTarefa() 
            elif x == 2:
                self.editaTarefa()
            elif x == 3:
                self.removeTarefa()
            elif x == 4:
                self.visualizaTarefa()

    def visualizaTarefa(self):
        self.repositorio.VisualizaTarefas(self)

    def criaTarefa(self):
        novatarefa = tarefa()
        
        while True:
            novoTitulo = input("Título")
            novatarefa.defineTitulo(novoTitulo)
            verificacao = Autenticador.verificaTitulo(self, novatarefa)
            if verificacao is False:
                impressao.erroTitulo(self)
                continue
            break

        descricao = input("Descrição")
        novatarefa.defineDescricao(descricao)
            
        while True:
            try:
                status = int(input("Está a ser concluida ou foi concluida? 0/1"))
                status = bool(status)
                verificacao = Autenticador.verificaStatus(self, novatarefa)                
                if verificacao is False:
                    impressao.AFazerInicial(self)
                    break
                else:
                    impressao.TarefaConcluida(self)
                    break

            except ValueError:
                impressao.erroValor(self)

        Controladordetarefas.SalvaTarefa(self, novatarefa)


    def editaTarefa(self):
        tarefas = self.repositorio.VisualizaTarefas()
        while True:
            try:
                ID = int(input("Qual tarefa você deseja editar? Digite o ID.\n>>"))
                if 1 <= ID <= len(tarefas):
                    impressao.TarefaSelecionada(self)

                    while True:
                        try:
                            opcao = int(input("O que você deseja editar?\n[1] Título\n[2] Descrição\n[3] Status\n>>"))
                            if opcao not in [1, 2, 3]:
                                impressao.erroValor(self)
                                continue
                            else:
                                if opcao is 3:
                                    try:
                                        NovoStatus = int(input("Insira o novo status (0/1):\n>>"))
                                        NovoStatus = bool(NovoStatus)
                                        Controladordetarefas.editaTarefa(self, opcao, NovoStatus, ID)
                                    except ValueError:
                                        impressao.erroValor(self)
                                else:
                                    Edicao = input("Escreva a atualização:\n>>")
                                    Controladordetarefas.editaTarefa(self, opcao, Edicao, ID)
                                
                                break

                        except ValueError:
                            impressao.erroValor(self)
                    break

                else:
                    impressao.erroValor(self)
                    continue

            except ValueError:
                impressao.erroValor(self)
                continue
      
        impressao.EdicaoConcluida(self)


    def removeTarefa(self):
        tarefas = self.repositorio.VisualizaTarefas()
        while True:
            try:
                ID = int(input("Qual tarefa você deseja remover? Digite o ID.\n>>"))
                if 1 <= ID <= len(tarefas):
                    impressao.TarefaSelecionada(self)
                    verificacao = input("Você tem certeza? [S/N]\n>>")
                    if verificacao in ["N, n"]:
                        impressao.acaoCancelada(self)
                    elif verificacao in ["S","s"]:
                        impressao.acaoConcluida(self)
                        Controladordetarefas.removeTarefa(self, ID)
                        break
                else:
                    impressao.erroValor()
                    continue

            except ValueError:
                impressao.erroValor()
                continue

maina = main()

maina.main()