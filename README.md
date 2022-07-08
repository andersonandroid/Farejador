[![author](https://img.shields.io/badge/author-andersonsantana-red.svg)](https://www.linkedin.com/in/anderson-santana-53a51a69) [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/andersonandroid)

<p align="center">
  <img src="banner.png" >
</p>

# Ferramenta de busca de imagem de pornografia infentojuvenil
<sub>*Software Architec* da AI-HUB</sub>

O FAREJADOR é um software de código aberto portável que pode ser usado para buscar imagem de pornografia infantojuvenil, que muitos casos, o perito de informática se depara com situações que precisam analisar no local imagens que comprovem a materalidade da prisão em flagrante do individuo.

## Introdução:

Esse software foi um trabalho de conclusão do curso da pôs-graduação em Computação Forense e Perícia Digital (instituição IPOG). Um software focado em desempenho e na eficacia na busca de imagem usando tecnologias modernas.

<p align="center">
  <img src="farejador.png?w=100">
</p>

**Tecnologias utilizadas:** Python, Hash, OpenCV, VP-Tree, SQLite.

**Características:**
* Suporte multiplataforma, testado em sistemas Windows e Linux
* Não precisa de instalação podendo ser executado em unidade removíveis
* Alto desempenho na indexação e na busca das imagens
* Relatório com as evidências encontradas com seus metadados
* Gera o hash das imagens encontradas para garantir a cadeia de custodia. 



## Setup:
Configuração do ambiente de desenvolvimento:

Instalação do Python no Windows:

Para instalar o Python no Windows acesse o site oficial (https://www.python.org/downloads/) e baixe a versão 3.9.4 ou posterior. Nesse mesmo site possui a documentação de instalação para cada sistema operacional.

Instalação do Python no Linux:

Atualize o gerenciador de pacotes com o comando:
```sh
sudo apt-get update
```
Para o Python 3.9, use este comando:
```sh
sudo apt-get install python3.9
```

Instalação das Bibliotecas no Python:
```sh
pip install numpy
```
```sh
pip install opencv-contrib-python
```
```sh
pip install imutils
```
```sh
pip install vptree
```

[![Watch the video](https://img.youtube.com/vi/T-D1KVIuvjA/maxresdefault.jpg)](https://youtu.be/T-D1KVIuvjA)

## Referências:

* **BARELI, Felipe da Costa. Introdução à Visão Computacional. São Paulo: Casa do Código, 2019.
* **MENEZES, Nilo Ney Coutinho. Introdução à Programação com Python . São Paulo: Novatec, 2017.
* **ELEUTÉRIO, Pedro Monteiro da Silva; MACHADO, Marcio Pereira. Desvendando a Computação Forense . São Paulo: Novatec, 2011.
* **ELEUTÉRIO. Nudetective. [S.l.], 2022a. Disponível em: < http://www.eleuterio.com/nudetective.html>. Acesso em: 05 mai. 2022.
* **TINEYE. Reverse Image Search. [S.l.], 2022a. Disponível em: < https://tineye.com/>. Acesso em: 05 mai. 2022.

* **Como usar o Histograma para Data Science:** https://bit.ly/2L2cMwy
* **Como Implementar Regressão Linear com Python:** https://bit.ly/2Li5pzY
* **Data Science: Investigando o naufrágio do Titanic:** https://bit.ly/2Ubr5SH
* **Como Tratar Dados Ausentes com Pandas:** https://bit.ly/31KWSMN
* **XGBoost: aprenda este algoritmo de Machine Learning em Python:** https://bit.ly/2UbRhws
* **Como criar uma Wordcloud em Python:** https://bit.ly/2OxsphM
* **Como lidar com dados desbalanceados:** https://bit.ly/2ZlaNsV
