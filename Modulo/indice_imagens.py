# impotação dos pacotes necessários
from Modulo.gera_hash import ConverteHash
from Modulo.gera_hash import DistanciaHamming
from Modulo.gera_hash import GeraHash
from imutils import paths

import pickle
import vptree
import cv2
import time


def GerarIndex(**parametros):

	args = parametros
	
	# pega o caminho de entrada das imagens e inicializa o dicionário de hashes
	imagePaths = list(paths.list_images(args["images"]))
	hashes = {}
	# percorrer os caminhos da imagem
	for (i, imagePath) in enumerate(imagePaths):
		# Pega o time inicial para calcular com o time final(end)
		#print(imagePath)
		start = time.time()
		# carregando a imagem de entrada
		image = cv2.imread(imagePath)
		# calcula o hash da imagem e faz a conversão
		h = GeraHash(image)
		h = ConverteHash(h)

		# atualiza o dicionário de hashes
		l = hashes.get(h, [])
		l.append(imagePath)
		hashes[h] = l

	# Construi o VP-Tree
	points = list(hashes.keys())
	tree = vptree.VPTree(points, DistanciaHamming)
	

	# serilizar o VP-Tree no disco
	f = open(args["tree"], "wb")
	f.write(pickle.dumps(tree))
	f.close()
	# serializa os hashes para o dicionário
		f = open(args["hashes"], "wb")
	f.write(pickle.dumps(hashes))
	f.close()
	# Pega o time final(end) para calcular com time inicial(start)
	end = time.time()
	quantidade = len(imagePaths)
	mensagem = ("Foi indexado {} imagens com tempo de processamento de {} segundos".format(quantidade, end - start))
	
	return mensagem

if __name__ == "__main__":


	
