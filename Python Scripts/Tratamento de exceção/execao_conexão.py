import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen(url='https://bibliotecaelfica.org/category/dd-5e/')
except urllib.error.URLError:
    print('\033[0;31m Erro! O site não esta acessível no momento.\033[m')
else:
    print('\033[0;34m Oba! Consegui acessar o site com sucesso!\033[m')
