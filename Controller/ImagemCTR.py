from Model.DTO.ImagemDTO import ImagemDTO
from Model.DAO.ImagemDAO import ImagemDAO


class ImagemCTR:

    
    def CadastrarImagens(self, pesquisada, encontrada, hash, data_criacao, data_alteracao, data_acesso, distancia, tempo):

        imagemDTO = ImagemDTO()
        imagemDTO.img_pesquisada = pesquisada
        imagemDTO.img_encontrada = encontrada
        imagemDTO.hash = hash
        imagemDTO.data_criacao = data_criacao
        imagemDTO.data_alteracao = data_alteracao
        imagemDTO.data_acesso = data_acesso
        imagemDTO.distancia = distancia
        imagemDTO.tempo = tempo
        imagemDAO = ImagemDAO()
        resultado = imagemDAO.CadastrarImagens(imagemDTO)



        #return resultado

    def ConsultaImagem(self, codigo):

        dados = ImagemDAO()
        resultado = dados.ConsultaImagens(codigo)

        return resultado
        
    def CarregarImagens(self):

        carregadados = ImagemDAO()
        query = carregadados.CarregarImagens()
        
        return query

    def ApagarDados(self):
        deleta = ImagemDAO()
        query = deleta.ApagaDados()

        return query
    