import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

from Templates.tela_principal import TelaPrincipal

app = QtWidgets.QApplication(sys.argv)
janela = TelaPrincipal()
janela.tela.show()
sys.exit(app.exec_())
 