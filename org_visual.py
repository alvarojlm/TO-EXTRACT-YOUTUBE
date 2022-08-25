from painel import Ui_Principal
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
from controle import *
from dw import *
from pytube import YouTube
from tkinter.filedialog import askdirectory

def seletor_res():
    b_ad=ui.button_audio
    resol=ui.select_resolution
    if ui.button_video.isChecked():
        b_ad.setChecked(False)
        b_ad.hide()
        resol.show()
    else:
        b_ad.show()
        resol.hide()

def baixar():
    print('clicou')
    aud=ui.button_audio.isChecked()
    vd=ui.button_video.isChecked()
    if ((aud == False) and (vd == False)):
        print('Não selc')
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle('Ops... atenção!')
        msg.setText('Você não selecionou como deseja baixar o arquivo! Por favor, selecione para fazer o download.')
        msg.exec()
    else: 
        print('chegando')
        if verifica_origem(ui.link.toPlainText()):
            print('verificou')
            sv=askdirectory()
            lk=YouTube(ui.link.toPlainText())
            if ui.button_audio.isChecked():
                centro_dw(sv, lk, 2)
            elif ui.button_video.isChecked():
                centro_dw(sv, lk, 1)
            ui.link.clear()
        else:
            t_invalido=QtWidgets.QMessageBox()
            t_invalido.setText('Link inválido! Tente novamente.')
            t_invalido.exec()




app = QtWidgets.QApplication(sys.argv)
Principal = QtWidgets.QWidget()
ui = Ui_Principal()
ui.setupUi(Principal)
ui.button_video.clicked.connect(seletor_res)
ui.Gerar_stream.clicked.connect(baixar)
Principal.show()
sys.exit(app.exec_())


