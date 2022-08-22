import urllib.request

def verifica_origem(lk: str ) -> bool:
    if 'https://www.youtube.com' in lk: return True
    else: return False

def tip_dw():
    print('Tipo de Downloas:')
    print('1) Video completo')
    print('2) Somente audio')
    tp=int(input())
    if tp == 1 or 2:
        return tp
        