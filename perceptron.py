import random, copy


class Perceptron:

    def __init__(self, entradas, saidas, taxa_aprendizado, ciclos, limiar):

        self.entradas = entradas
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.ciclos = ciclos
        self.limiar = limiar  # limiar
        self.numEntradas = len(entradas)
        self.numPorEntrada = len(entradas[0])  # quantidade de elementos por entrada
        self.pesos = []

    def treinar(self):

        # adiciona a entrada limiar(x0)
        for entrada in self.entradas:
            entrada.insert(0, self.limiar)

        # inicia o vetor de pesos com valores aleatórios
        for i in range(self.numPorEntrada):
            self.pesos.append(random.random())

        # insere o limiar(w0) no vetor de pesos
        self.pesos.insert(0, random.random())

        numCiclos = 0

        while (numCiclos <= self.ciclos):

            erro = False

            for i in range(self.numEntradas):

                net = 0

                #Calculando o net para cada neurônio
                for j in range(self.numPorEntrada + 1):
                    net += self.pesos[j] * self.entradas[i][j]

                #calculo da função de ativação
                y = self.sinal(net)

                # A saída é o desejada ? Se sim n reajusta os pesos. Se não, reajusta !
                if y != self.saidas[i]:

                    # calcula o erro: (desejado - Y)
                    erro_aux = self.saidas[i] - y

                    # faz o ajuste dos pesos
                    for j in range(self.numPorEntrada + 1):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.entradas[i][j]

                    erro = True  # ainda existe erro

            # incrementa o número de épocas
            numCiclos += 1

    # utiliza a função sinal, se é -1 então é classe1, se não é classe2
    def testar(self, amostra, classe1, classe2, limiar):

        amostra.insert(0, limiar)

        # utiliza o vetor de pesos que foi ajustado na fase de treinamento
        net = 0
        for i in range(self.numPorEntrada + 1):
            net += self.pesos[i] * amostra[i]

        # calcula a saída da rede
        y = self.sinal(net)

        # verifica a qual classe pertence
        if y == 0:
            print('A amostra pertence a classe %s' % classe1)
        else:
            print('A amostra pertence a classe %s' % classe2)


    # função de ativação: degrau bipolar (sinal)
    def sinal(self, net):
        return 1 if net >= 0 else 0


print('\nClasse 0 ou classe 1 ?\n')

entradas = [[-1, -1, 1],
            [1, -1, 1],
            [-1, -1, -1],
            [1, 1, -1],
            [-1, 1, 1],
            [1, -1, -1]]

# saídas desejadas de cada amostra
saidas = [0, 1, 0, 1, 0, 1]

# conjunto de amostras de testes
testes = copy.deepcopy(entradas)

# cria uma rede Perceptron
rede = Perceptron(entradas=entradas, saidas=saidas, taxa_aprendizado=0.06, ciclos=1000, limiar=1)

# treina a rede
rede.treinar()

# testando a rede
for teste in testes:
    rede.testar(teste, '0', '1', limiar=1)