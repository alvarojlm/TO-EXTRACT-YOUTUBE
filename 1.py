from pytube import YouTube
from controle import verifica_origem, tip_dw
from dw import centro_dw
from tkinter.filedialog import askdirectory

lik=str(input('Digite o link do YouTube: '))
print(lik)
print(verifica_origem(lik))
if verifica_origem(lik):
    lik=YouTube(lik)
    print(lik)

    #audio, video ou ambos
    tp=tip_dw()

    
    #local
    sv = askdirectory()

    centro_dw(sv, lik, tp)
print(lik)
