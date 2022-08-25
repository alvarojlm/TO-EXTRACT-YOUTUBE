from pytube import YouTube
from org_visual import Principal, Ui_Principal
imp=Ui_Principal(Principal)
def dw_video(sv, lik):
    '''print('Digite a resolução que deseja: 720p, 480p, 360p')
    res = input('Res: ')'''
    res = imp.select_resolution.itemText()
    lik=lik.streams.get_by_resolution(res)
    lik.download(output_path=sv)


def dw_audio(sv,lik):
    lik=lik.streams.get_audio_only()
    lik.download(output_path=sv)


def centro_dw(sv: str, lik: YouTube, tp: int):

    if tp == 1: return dw_video(sv, lik)
    else: return dw_audio(sv, lik) 
