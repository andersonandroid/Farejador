
from DataBase.query import sqlite_db

class ImagemDAO:
    
    def CadastrarImagens(self, imagem):

        db = sqlite_db("DataBase/Imagem.db")
        data_criacao = str(imagem.data_criacao)
        data_alteracao = str(imagem.data_alteracao)
        data_acesso = str(imagem.data_acesso)
        distancia = str(imagem.distancia)
        tempo = str(imagem.tempo)

        query = "INSERT INTO imagens (img_pesquisada, img_encontrada, hash, data_criacao, data_alteracao, data_acesso, distancia, tempo) VALUES ('"+imagem.img_pesquisada+"','" +imagem.img_encontrada+"','" +imagem.hash+"','" +data_criacao+"','" +data_alteracao+"','" +data_acesso+"','" +distancia+"','" +tempo+"')"
        dados = db.inserir_apagar_atualiza(query)

        #return dados

    def CarregarImagens(self):


        db = sqlite_db("DataBase/Imagem.db")
        dados = db.pega_dados("SELECT codigo, img_pesquisada, hash, data_criacao, data_alteracao, data_acesso FROM imagens")
        
        return dados

    def ConsultaImagens(self, codigo):
        db = sqlite_db("DataBase/Imagem.db")
        dados = db.pega_dados("SELECT * FROM imagens WHERE codigo = '{}'".format(codigo))

        return dados

    def ApagaDados(self):

        db = sqlite_db("DataBase/Imagem.db")
        query = "DELETE FROM imagens"
        dados = db.inserir_apagar_atualiza(query)
        dados = db.pega_dados("VACUUM")
        dados = db.inserir_apagar_atualiza(query)

        return dados