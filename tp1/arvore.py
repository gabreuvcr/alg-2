class No:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        self.arestas = {}


class Arvore:
    def __init__(self, string):
        self.raiz = No(0, 0)
        self.string = string + '$'
        self.string_acumulada = ''
        self.repeticoes = 0
        self._constroi_arvore()
    

    def _letras_comuns(self, substring_no, substring):
        index = min(len(substring_no), len(substring))
        letras_comuns = 0
        for i in range(index): 
            if substring_no[i] != substring[i]:
                break
            letras_comuns += 1
        return letras_comuns


    def _constroi_arvore_rec(self, atual, substring, i):
        if substring[0] in atual.arestas:
            atual = atual.arestas[substring[0]]
            letras_comuns = self._letras_comuns(self.string[atual.inicio : atual.final], substring)
            if len(self.string[atual.inicio : atual.final]) == letras_comuns:
                self._constroi_arvore_rec(atual, substring[letras_comuns:], i + letras_comuns)
            else:
                atual_restante = self.string[atual.inicio + letras_comuns : atual.final][0]
                arestas_atual_restante = atual.arestas
                substring_restante = substring[letras_comuns:][0]
                atual.arestas = {}
                atual.arestas[atual_restante] = No(atual.inicio + letras_comuns, atual.final)
                atual.arestas[atual_restante].arestas = arestas_atual_restante
                atual.arestas[substring_restante] = No(i + letras_comuns, len(self.string))
                atual.final = atual.inicio + letras_comuns
        else:
            atual.arestas[substring[0]] = No(i, len(self.string))


    def _constroi_arvore(self):
        for i in range(len(self.string)):
            self._constroi_arvore_rec(self.raiz, self.string[i:], i)


    def _imprime_ocorrencias(self):            
        index, repeticao = 0, 1
        while True:
            index = self.string.find(self.string_acumulada, index)
            if index >= 0:
                print(f'{repeticao}º ocorrência: [{index}, {index + len(self.string_acumulada) - 1}]')
                index += 1
                repeticao += 1
            else:
                break


    def _encontra_rec(self, atual, acumulo_local = ''):
        if not self.string[atual.inicio : atual.final].endswith('$'):
            acumulo_local += self.string[atual.inicio : atual.final]
            for aresta in atual.arestas.values():   
                self._encontra_rec(aresta, acumulo_local)
            if len(acumulo_local) > len(self.string_acumulada):
                self.string_acumulada = acumulo_local
                self.repeticoes = len(atual.arestas)


    def maior_substring_repetida(self):
        atual = self.raiz
        for aresta in atual.arestas.values():
            self._encontra_rec(aresta)
        if self.string_acumulada == '':
            print('\nNão há string que se repete.') 
        else:
            print(f'\nMaior string que se repete: {self.string_acumulada}\nNúmero de repetições: {self.repeticoes}')
            self._imprime_ocorrencias()
