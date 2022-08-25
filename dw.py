from pytube import YouTube



def dw_video(sv, lik: YouTube, res=str):
    lik=lik.streams.get_by_resolution(resolution=res)
    lik.download(output_path=sv)


def dw_audio(sv,lik: YouTube):
    lik=lik.streams.get_audio_only()
    lik.download(output_path=sv)


def centro_dw(sv: str, lik: YouTube, tp: int, res=str):

    if tp == 1: return dw_video(sv, lik, res)
    else: return dw_audio(sv, lik) 
