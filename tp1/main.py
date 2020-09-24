from arvore import Arvore
import sys


nome_arquivo = sys.argv[1]
with open(nome_arquivo, 'r') as arquivo:
    genoma = ''
    for linha in arquivo:
        if not linha.startswith('>'):
            genoma += linha.replace('\n', '')
            
arvore = Arvore(genoma)
arvore.maior_substring_repetida()
