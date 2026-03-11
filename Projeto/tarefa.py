class tarefa():
    contadorid = 0
    
    def __init__(self, descricao=None, titulo=None, status=False):
        tarefa.contadorid += 1
        self.id = tarefa.contadorid
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def defineTitulo(self, novoTitulo):
        self.titulo = novoTitulo

    def defineDescricao(self, novaDescricao):
        self.descricao = novaDescricao
    
    def defineStatus(self, novoStatus):
        self.status = novoStatus
    
    def mostraID(self):
        return self.id

    def mostraTitulo(self):
        return self.titulo

    def mostraDescricao(self):
        return self.descricao
    
    def mostraStatus(self):
        return self.status