# coding: utf-8

import sys
import time
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox

from Templates.tela_principal2 import TelaSecundaria




class TelaPrincipal():
    def __init__(self):
        super(TelaPrincipal, self).__init__()
        
        # Setup da Tela - App
        self.tela = uic.loadUi("UI/Tela_principal.ui")
        #self.tela.setFixedSize(590, 440)
        self.tela.setGeometry(300, 200, 929, 595)
        self.tela.setMinimumHeight(595)
        self.tela.setMinimumWidth(929)
        self.tela.setMaximumHeight(595)
        self.tela.setMaximumWidth(929)



        self.tela.setAutoFillBackground(True)
        self.tela.pushButton.clicked.connect(self.Entrar_Click)



    def Entrar_Click(self):

        self.windows = TelaSecundaria()
        self.windows.tela.show()
        self.tela.close()
            

            
           
            
        
            
       
        
        


 