# coding: utf-8
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView
from Modulo.consulta import Consulta, ConsultaPasta
from Modulo.infoarquivo import Getsha256File, InfoArquivo
from Modulo.indice_imagens import GerarIndex
from Controller.ImagemCTR import ImagemCTR
from datetime import datetime
from pytz import timezone
import pathlib
import configparser

def DataHora():
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    #data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
    data = data_e_hora_sao_paulo.strftime('%d%m%Y')
    return data


class TelaSecundaria():
    def __init__(self):
        super(TelaSecundaria, self).__init__()
        
        # Setup da Tela - App

        self.telaversao = uic.loadUi("UI/Tela_versao.ui")
        self.telaversao.setGeometry(400, 300, 777, 473)
        self.telaversao.setMinimumHeight(473)
        self.telaversao.setMinimumWidth(777)
        self.telaversao.setMaximumHeight(473)
        self.telaversao.setMaximumWidth(777)

        self.tela = uic.loadUi("UI/Tela_principal2.ui")
        self.tela.setGeometry(300, 200, 929, 633)
        self.tela.setMinimumHeight(633)
        self.tela.setMinimumWidth(929)
        self.tela.setMaximumHeight(633)
        self.tela.setMaximumWidth(929)
        self.tela.setAutoFillBackground(True)
        self.tela.gridImagens.verticalHeader().hide()
        self.tela.gridImagens.cellClicked.connect(self.cell_Visitante_clicked)
        #self.CarregarImagem()
        self.ArquivoConfig()

        #self.tela.gridImagens.cellClicked.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.tela.gridImagens.cellClicked.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #self.tela.gridImagens.cellClicked.setSelectionMode(QAbstractItemView.SingleSelection)

        # Ocultar campos do form
        self.tela.pasta_arquivo.hide()
        self.tela.tree.hide()
        self.tela.hashes.hide()
        self.tela.processando.hide()



        # Botões do Formulario
        self.tela.pushButton.clicked.connect(self.SelecionarArquivo)
        self.tela.pushButton_3.clicked.connect(self.ProcessarConsulta)
        self.tela.pushButton_2.clicked.connect(self.SelecionarIndexador)
        self.tela.pushButton_4.clicked.connect(self.ProcessarIndexacao)
        self.tela.pushButton_5.clicked.connect(self.SelecionarPastas)
        self.tela.pushButton_6.clicked.connect(self.ExtrairEvidencia)
        self.tela.pushButton_7.clicked.connect(self.LimpaPesquisa)

        # Imagen padrão dos campos Foto Pesquisa e Banco de dados
        self.tela.fotops.setPixmap(QtGui.QPixmap('./UI/imagem/image_bd.png'))
        self.tela.fotops_2.setPixmap(QtGui.QPixmap('./UI/imagem/image_bd.png'))

        # ----------- Menu do sistema --------------------#
        self.tela.actionVersao.triggered.connect(self.MenuVersao)
        # ----------- Fim: Menu do sistema --------------------#
    def LimpaPesquisa(self):

        print("Limpa Pesquisa")
        self.tela.fotops.setPixmap(QtGui.QPixmap('./UI/imagem/image_bd.png'))
        self.tela.fotops_2.setPixmap(QtGui.QPixmap('./UI/imagem/image_bd.png'))
        self.tela.hash_linha.setText("")
        self.tela.arquivo_linha.setText("")
        self.tela.dtc_linha.setText("")
        self.tela.dta_linha.setText("")
        self.tela.dtac_linha.setText("")
        self.tela.dh.setText("")
        self.tela.tempo.setText("")
        self.tela.consulta.setText("")
        self.tela.pasta_arquivo.setText("")
        imagemCTR = ImagemCTR()
        imagemCTR.ApagarDados()
        self.CarregarImagem()

    def ArquivoConfig(self):

        config = configparser.ConfigParser()
        config.read("config.ini")

        distancia = config.get("Default", "hamming")
        self.tela.hamming.setText(distancia)
        pasta = config.get("Default", "indexPasta")
        self.tela.pasta_indexa.setText(pasta)
        tree = config.get("Default", "tree")
        hashes = config.get("Default", "hashes")
        self.tela.tree.setText(tree)
        self.tela.hashes.setText(hashes)

        # Colocar essa funcionalidade de pesquisa por palavras conhecidas de pedofilia
        pesquisanome = config.get("Pesquisa", "pesquisanome")
        print(pesquisanome)
        if pesquisanome == 'true':

            palavras = config.get("Pesquisa", "palavras")
            try:
                lista = palavras.split(",")
                print(lista)
                print(lista.index('amor'))
            except:
                lista = -1
                print(lista)



    def MenuVersao(self):
        self.telaversao.show()



    def CarregarImagem(self):

        carregadados = ImagemCTR()
        self.dados = carregadados.CarregarImagens()

        self.tela.gridImagens.setRowCount(len(self.dados))
        self.tela.gridImagens.setColumnCount(6)
        count = 0
        for i in range(0, len(self.dados)):
            count = count + 1
            for j in range(0, 6):
                self.tela.gridImagens.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.dados[i][j])))

        self.tela.total2.setText(str(count))

    def cell_Visitante_clicked(self):

        linha = self.tela.gridImagens.currentItem().row()
        self.numero = self.tela.gridImagens.item(linha, 0).text()
        resultado = ImagemCTR()
        dados = resultado.ConsultaImagem(self.numero)

        if self.tela.pasta_arquivo.text() == 'A':
            self.tela.fotops_2.setPixmap(QtGui.QPixmap(dados[0][2]))
            self.tela.hash_linha.setText(dados[0][3])
            self.tela.arquivo_linha.setText(dados[0][1])
            self.tela.dtc_linha.setText(dados[0][4])
            self.tela.dta_linha.setText(dados[0][5])
            self.tela.dtac_linha.setText(dados[0][6])
            self.tela.dh.setText(dados[0][7])
            self.tela.tempo.setText(dados[0][8])

        else:
            self.tela.fotops.setPixmap(QtGui.QPixmap(dados[0][1]))
            self.tela.fotops_2.setPixmap(QtGui.QPixmap(dados[0][2]))
            self.tela.hash_linha.setText(dados[0][3])
            self.tela.arquivo_linha.setText(dados[0][1])
            self.tela.dtc_linha.setText(dados[0][4])
            self.tela.dta_linha.setText(dados[0][5])
            self.tela.dtac_linha.setText(dados[0][6])
            self.tela.dh.setText(dados[0][7])
            self.tela.tempo.setText(dados[0][8])
        pass

    def ExtrairEvidencia(self, dados):

        linha = self.tela.gridImagens.rowCount()
        if linha >= 1:
            data = DataHora()
            nomearquivo = "Evidencias\evidencia" + data + ".txt"
            carregadados = ImagemCTR()
            dados = carregadados.CarregarImagens()

            with open(nomearquivo, "w") as arquivo:
                for i in range(0, len(self.dados)):
                    codigo = str(i + 1)
                    linha = str(codigo + ',' + dados[i][1] + ',' + dados[i][2] + ',' + dados[i][3] + ',' + dados[i][4] + ',' + dados[i][5])
                    print(linha)
                    arquivo.write("%s\n" % linha)

            QMessageBox.information(QMessageBox(), "Evidências!", "Arquivo Gerado com sucesso na pasta Evidencias")
        else:
            QMessageBox.critical(QMessageBox(), "Alerta!", "Não existe evidências na grade!")

    def SelecionarPastas(self):

        self.pastas = QtWidgets.QFileDialog.getExistingDirectory()
        # ---------- Pega o nome do arquivo que será importado ---------- #
        path = self.pastas
        delimiter = '/'  # - criar um parametro para informar o tipo de delimitador baseado no SO
        novo = path.split(delimiter)

        if len(novo) != 1:

            self.tela.consulta.setText(path)
            self.tela.pasta_arquivo.setText('P')

        else:
            self.tela.consulta.setText(path)
            self.tela.pasta_arquivo.setText('')


    # Seleciona a imagem que será pesquisado no banco de dados
    def SelecionarArquivo(self):

        self.arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]
        # ---------- Pega o nome do arquivo que será importado ---------- #
        path = self.arquivo
        delimiter = '/'  # - criar um parametro para informar o tipo de delimitador baseado no SO
        novo = path.split(delimiter)
        #nomearquivo = novo[int(len(novo) - 1)]

        if len(novo) != 1:

            self.tela.consulta.setText(path)
            self.tela.pasta_arquivo.setText('A')
            self.tela.fotops.setPixmap(QtGui.QPixmap(path))
        else:
            self.tela.consulta.setText(path)
            self.tela.pasta_arquivo.setText('')
            self.tela.fotops.setPixmap(QtGui.QPixmap('image_bd.png'))
            self.tela.fotops_2.setPixmap(QtGui.QPixmap('image_bd.png'))


    def ProcessarConsulta(self):

        distancia = self.tela.hamming.text()
        caminhoarquivo = self.tela.consulta.text()

        vptree = self.tela.tree.text()
        hashes = self.tela.hashes.text()


        if caminhoarquivo == '':

            QMessageBox.critical(QMessageBox(), "Alerta!", "Selecione um arquivo para poder processar a pesquisa!!")

        else:
            # Verifica se a pesquisa é por arquivo ou pasta.
            # Se for por arquivo o valor é "A" e pasta "P"
            if self.tela.pasta_arquivo.text() == 'A':
                #Passa os parametros de pesquisa para função Search
                #Verifica se os arquivos vptree e hashes são diferentes
                if (vptree == "default") and (hashes == "default"):
                    encontrado, distancia, tempo = self.imagem_consultada = Consulta(tree='./Dataset/data_vptree.pickle', hashes='./Dataset/data_hashes.pickle', consulta=caminhoarquivo, distance=distancia)
                else:
                    encontrado, distancia, tempo = self.imagem_consultada = Consulta(tree=vptree, hashes=hashes, consulta=caminhoarquivo, distance=distancia)

                if encontrado != None:
                    print("Verdadeiro")

                    #self.tela.fotops_2.setPixmap(QtGui.QPixmap(self.imagem_consultada))
                    #encontrado = self.imagem_consultada

                    # Criar a função que apaga e grava no banco de dados o resultado e a pesquisa
                    imagemCTR = ImagemCTR()
                    imagemCTR.ApagarDados()
                    hasharquivo = Getsha256File(caminhoarquivo)
                    caminhoarquivo = caminhoarquivo.replace("%\%", "\\" )
                    caminho = pathlib.Path(caminhoarquivo)
                    data_acesso, data_alteracao, data_criacao = InfoArquivo(caminho)
                    imagemCTR.CadastrarImagens(caminhoarquivo, encontrado, hasharquivo, data_acesso, data_alteracao, data_criacao, distancia, tempo)
                    self.CarregarImagem()
                else:

                    QMessageBox.information(QMessageBox(), "Pesquisa!", "Não foi encontrado imagem semelhante!")
            else:
                # Passa os parametros de pesquisa para função Search
                imagemCTR = ImagemCTR()
                imagemCTR.ApagarDados()

                # Passa os parametros de pesquisa para função Search
                # Verifica se os arquivos vptree e hashes são diferentes
                if (vptree == "default") and (hashes == "default"):
                    self.imagens_consultada = ConsultaPasta(tree='./Dataset/data_vptree.pickle', hashes='./Dataset/data_hashes.pickle', consulta=caminhoarquivo, distance=distancia)
                else:
                    self.imagens_consultada = ConsultaPasta(tree=vptree, hashes=hashes, consulta=caminhoarquivo, distance=distancia)

                #encontrado = self.imagens_consultada
                self.CarregarImagem()


            
    def SelecionarIndexador(self):

        self.pasta = QtWidgets.QFileDialog.getExistingDirectory()
        # ---------- Pega o nome do arquivo que será importado ---------- #
        path = self.pasta
        delimiter = '/'  # - criar um parametro para informar o tipo de delimitador baseado no SO
        novo = path.split(delimiter)

        if len(novo) != 1:

            self.tela.pasta_indexa.setText(path)

        else:
            self.tela.pasta_indexa.setText(path)


    def ProcessarIndexacao(self):

        pastaselecionada = self.tela.pasta_indexa.text()


        # Informações do arquivo config.ini
        vptree = self.tela.tree.text()
        hashes = self.tela.hashes.text()

        if pastaselecionada == '':

            QMessageBox.critical(QMessageBox(), "Alerta!", "Selecione uma pasta com imagem para indexar!!")

        else:

            if (vptree == "default") and (hashes == "default"):
                # images='imagens/', tree='vptree.pickle', hashes='hashes.pickleg'
                resp = GerarIndex(images=pastaselecionada, tree='./Dataset/data_vptree.pickle', hashes='./Dataset/data_hashes.pickle')
                QMessageBox.information(QMessageBox(), "Processamento das Imagens", resp)
                print(resp)
                #self.tela.processando.setHidden(True)
            else:
                # images='imagens/', tree='vptree.pickle', hashes='hashes.pickleg'
                resp = GerarIndex(images=pastaselecionada, tree=vptree, hashes=hashes)
                QMessageBox.information(QMessageBox(), "Processamento das Imagens", resp)

            
           
            
        
            
       
        
        

