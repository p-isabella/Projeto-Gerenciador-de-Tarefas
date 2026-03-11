import mysql.connector
import os
from tarefa import tarefa

class RepositorioTarefas:
    def __init__(self):

        self.meubd = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.environ.get("BD_TAREFA"),
            database='bdtarefa'
        )

        self.usobd = self.meubd.cursor()

    def criacaoTabelaTarefa(self):
        self.usobd.execute("""CREATE TABLE IF NOT EXISTS tarefa (
                    id INT NOT NULL AUTO_INCREMENT,
                    titulo VARCHAR(100) NOT NULL,
                    descricao VARCHAR(350),
                    status BOOLEAN DEFAULT 0,
                    PRIMARY KEY (id)
                      )""")
        self.meubd.commit()

    def InserirTarefa(self, titulo, descricao, status):
        self.usobd.execute("""INSERT INTO tarefa (titulo, descricao, status)
                         VALUES (%s, %s, %s)""", (titulo, descricao, status))
        self.meubd.commit()
    
    def EditarTarefaTitulo(self, oNovoTitulo, idrecebido):
        self.usobd.execute("""UPDATE tarefa
                           SET titulo = %s
                           WHERE id= %s""", (oNovoTitulo, idrecebido))
        self.meubd.commit()

    def EditarTarefaDescricao(self, aNovaDescricao, idrecebido):
        self.usobd.execute("""UPDATE tarefa
                           SET descricao = %s
                           WHERE id=%s""", (aNovaDescricao, idrecebido))
        self.meubd.commit()
        
    def EditarTarefaStatus(self, oNovoStatus, idrecebido):
        self.usobd.execute("""UPDATE tarefa
                           SET status = %s
                           WHERE id=%s""", (oNovoStatus, idrecebido))
        self.meubd.commit()

    def ExcluiTarefa(self, idrecebido):
        self.usobd.execute("""DELETE FROM tarefa
                           WHERE id= %s""", (idrecebido,))
        self.meubd.commit()

    def VisualizaTarefas(self):
        self.usobd.execute("""SELECT * FROM tarefa""")
        visualizacao = self.usobd.fetchall()
        print("|ID | TAREFA | DESCRIÇÃO | STATUS |")
        for linhas in visualizacao: print(linhas) # somente para visualização por enquanto, depois mudar para interface
        return visualizacao

    def deletaTabela(self):
        self.usobd.execute("""DROP TABLE tarefa""")
        self.meubd.commit()
        


