from painel import Ui_Principal
from PyQt5 import QtWidgets, QtGui
import sys
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
    aud=ui.button_audio.isChecked()
    vd=ui.button_video.isChecked()
    if ((aud == False) and (vd == False)):
        msg_erro_selc_strem()
    else: 
        if verifica_origem(ui.link.toPlainText()):
            sv=askdirectory()
            lk=YouTube(ui.link.toPlainText())
            resolt = ui.select_resolution.currentText()
            if ui.button_audio.isChecked():
                centro_dw(sv, lk, 2)
            elif ui.button_video.isChecked():
                centro_dw(sv, lk, 1, resolt)

            msg_concl()
            ui.link.clear()
        else:
            t_invalido=QtWidgets.QMessageBox()
            t_invalido.setText('Link inválido! Tente novamente.')
            t_invalido.exec()

def msg_erro_selc_strem():
    msg=QtWidgets.QMessageBox()
    msg.setWindowTitle('Ops... atenção!')
    msg.setText('Você não selecionou como deseja baixar o arquivo! Por favor, selecione para fazer o download.')
    msg.exec()

def msg_concl():
    msg=QtWidgets.QMessageBox()
    ic = QtGui.QPixmap()
    ic.load('azul_ccl.png')
    ic=ic.scaledToWidth(190)
    ic=ic.scaledToHeight(90)
    msg.setIconPixmap(ic)
    msg.setWindowTitle('Tudo certo!')
    msg.setText('Seu download foi realizado com sucesso. Aproveito seu stream!')
    msg.exec()



app = QtWidgets.QApplication(sys.argv)
Principal = QtWidgets.QWidget()
ui = Ui_Principal()
ui.setupUi(Principal)
ui.button_video.clicked.connect(seletor_res)
ui.Gerar_stream.clicked.connect(baixar)
Principal.show()
sys.exit(app.exec_())