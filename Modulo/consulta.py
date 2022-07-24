# coding: utf-8
from Modulo.gera_hash import ConverteHash
from Modulo.gera_hash import GeraHash
from Modulo.infoarquivo import Getsha256File, InfoArquivo
from imutils import paths
from Controller.ImagemCTR import ImagemCTR
import argparse
import pickle
import time
import cv2
import pathlib


def Consulta(**parametros):

	args = parametros

	# carregar o VP-Tree e o dicionário de hashes
	tree = pickle.loads(open(args["tree"], "rb").read())
	hashes = pickle.loads(open(args["hashes"], "rb").read())

	# carregar a imagem de entrada da consulta
	image = cv2.imread(args["consulta"])
	

	# calcula o hash da imagem da consulta e converte
	consultaHash = GeraHash(image)
	consultaHash = ConverteHash(consultaHash)

	# Realiza a pesquisa
	inicial = time.time()
	results = tree.get_all_in_range(consultaHash, int(args["distance"]))
	results = sorted(results)
	final = time.time()
	tempo = format(final - inicial)
	
	if (len(results)) != 0:
		# faz o loop dos resultados
		for (d, h) in results:
			# pega todos os caminho de imagem em um conjunto de dados com o mesmo hash
			resultPaths = hashes.get(h, [])

			# Faz um loop sobre os caminhos do resultado
			for resultPath in resultPaths:
				
				resultPath = resultPath
			
			resp = True	

		return resultPath, d, tempo
	else:

		resultPaths = None
		d = None
		tempo = None
		return resultPaths, d, tempo



def ConsultaPasta(**parametros):

	args = parametros

	# carregar o VP-Tree e o dicionário de hashes
	tree = pickle.loads(open(args["tree"], "rb").read())
	hashes = pickle.loads(open(args["hashes"], "rb").read())

	# pega o caminho de entrada das imagens e inicializa o dicionário de hashes
	imagePaths = list(paths.list_images(args["consulta"]))

	for (i, imagePath) in enumerate(imagePaths):

		# carregar a imagem de entrada da consulta
		image = cv2.imread(imagePath)
		# calcula o hash da imagem da consulta e converte
		consultaHash = GeraHash(image)
		consultaHash = ConverteHash(consultaHash)


		# Realiza a pesquisa
		start = time.time()
		results = tree.get_all_in_range(consultaHash, int(args["distance"]))
		results = sorted(results)
		end = time.time()
		tempo = format(end - start)
		
		# faz o loop dos resultados
		for (d, h) in results:
			# pega todos os caminho de imagem em um conjunto de dados com o mesmo hash
			resultPaths = hashes.get(h, [])
			# Faz um loop sobre os caminhos do resultado
			for resultPath in resultPaths:
				# carrega a imagem e exibi na tela
				resultPath = resultPath
				

		imagemCTR = ImagemCTR()
		# Gera o Hash do arquivo consultado
		hasharquivo = Getsha256File(imagePath)
		# Troca a '\' para '\\' e obtem a data de acesso, alteração e modificação do arquivo
		caminhoarquivo = imagePath.replace("%\%", "\\")
		caminho = pathlib.Path(caminhoarquivo)
		data_acesso, data_alteracao, data_criacao = InfoArquivo(caminho)
		# Grava no banco de dados as informações do arquivo consultado
		imagemCTR.CadastrarImagens(imagePath, resultPath, hasharquivo, data_acesso, data_alteracao, data_criacao, d, tempo)


	return resultPaths

if __name__ == "__main__":

	