# impotação dos pacotes necessários
import numpy as np
import cv2
def dhash(image, hashSize=8):
	# converte a imagem em tom de cinza
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# redimensiona a imagem em tons de cinza, adicionando uma única coluna para poder calcular o gradiente horizontal
	resized = cv2.resize(gray, (hashSize + 1, hashSize))
	# calcula o gradiente horizontal(relativo) entre pixels da coluna adjacentes
	diff = resized[:, 1:] > resized[:, :-1]
	# converte a diferença da imagem em um hash
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


def convert_hash(h):
	# converte o hash para float 64 bits usando NumPy e, em seguida, retorna inteiro
	# Python's built in int
	return int(np.array(h, dtype="float64"))



def hamming(a, b):
	# calcula e retorna a distância de Hamming entre os inteiros
	return bin(int(a) ^ int(b)).count("1")
