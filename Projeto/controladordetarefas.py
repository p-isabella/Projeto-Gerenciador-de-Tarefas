class Controladordetarefas:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def SalvaTarefa(self, novatarefa):
        self.repositorio.InserirTarefa(novatarefa.mostraTitulo(), novatarefa.mostraDescricao(), novatarefa.mostraStatus())
        return novatarefa

    def editaTarefa(self, valorEdicao, edicao, tarefaID):
        
        if valorEdicao == 1:
            self.repositorio.EditarTarefaTitulo(edicao, tarefaID)
        elif valorEdicao == 2:
            self.repositorio.EditarTarefaDescricao(edicao, tarefaID)
        else:
            self.repositorio.EditarTarefaStatus(edicao, tarefaID)

    def removeTarefa(self, IDaRemover):
        self.repositorio.ExcluiTarefa(IDaRemover)

    def visualizaTarefas(self):
        self.repositorio.VisualizaTarefas()