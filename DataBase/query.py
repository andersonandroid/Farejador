import sqlite3


class sqlite_db:
    def __init__(self,banco = None):
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)
            

    def open(self, banco):

        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()


        except sqlite3.Error as e:
            print("Não foi possivel estabelecer conexão")

    def inserir_apagar_atualiza(self, query):

        cur = self.cursor
        cur.execute(query)
        self.conn.commit()


    def pega_dados(self, query):

        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()


if __name__ == "__main__":
    db = sqlite_db("Imagem.db")
    img_pesquisada = "C:/Users/ander/PycharmProjects/pythonFarejador/consulta\sanfona_OLD.jpg"
    img_encontrada = "C:/Users/ander/PycharmProjects/pythonFarejador/consulta\sanfona_OLD.jpg"
    
    #dados = db.pega_dados("SELECT * from usuario WHERE login = '{}' and senha = '{}'". format(usuario, senha))
    dados = db.inserir_apagar_atualiza("INSERT INTO imagens(img_pesquisada, img_encontrada, hash, data_criacao) VALUES ('C:/Users/ander/PycharmProjects/pythonFarejador/consulta\sanfona_OLD.jpg', 'C:/Users/ander/PycharmProjects/pythonFarejador/consulta\sanfona_OLD.jpg', '12345678', '2022-06-16 11:51:30.238981')")
    retorno = db.pega_dados("SELECT * FROM imagens WHERE codigo = 50")
    #dados = db.inserir_apagar_atualiza('DELETE FROM imagens')
    print(retorno)
    #print(dados)


