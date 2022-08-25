from painel import Ui_Principal
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
from controle import *

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
        try:
            verifica_origem(ui.link.text()) 
            print(verifica_origem(ui.link.text()))
        except:
            QtWidgets.QMessageBox().setText('Link inválido! Tente novamente.') 




app = QtWidgets.QApplication(sys.argv)
Principal = QtWidgets.QWidget()
ui = Ui_Principal()
ui.setupUi(Principal)
ui.button_video.clicked.connect(seletor_res)
ui.Gerar_stream.clicked.connect(baixar)
Principal.show()
sys.exit(app.exec_())


