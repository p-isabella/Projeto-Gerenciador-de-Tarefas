class Autenticador:
    def verificaTitulo(self, tarefa):
        if tarefa.mostraTitulo():
            return True
        else:
            return False

    def verificaStatus(self, tarefa):
        if tarefa.mostraStatus():
            return True
        
    

