#plote

import matplotlib.pyplot as plt
import numpy as np


def diretorio(caso, nome):
	matriz = '/home/pc/Desktop/IC/caos/arestas'
	casos = ['/LM_p1','LM_int','LM_fbp','LM_c1','LM_c2','LM_fc']
	barra = '/'
	tipo = '.txt'
	
	
	nome = str(nome)
	caso = float(caso)
	
	string=''
	
	if (caso == 3.5):
		string = str(matriz+casos[0]+barra+nome+tipo)
	elif (caso == 3.56995):
		string = str(matriz+casos[1]+barra+nome+tipo)
	elif (caso == 3.857):
		string = str(matriz+casos[2]+barra+nome+tipo)
	elif (caso == 3.87):
		string = str(matriz+casos[3]+barra+nome+tipo)
	elif (caso == 3.89):
		string = str(matriz+casos[4]+barra+nome+tipo)
	elif (caso == 4):
		string = str(matriz+casos[5]+barra+nome+tipo)
	else:
		print("Caso invalido")

	return string

pasta = diretorio(3.5, 100)
pont = open("dado_2000_2.txt","r")#abrindo arquivo para ler


vec = pont.readlines()#lendo todo o arquivo linha a linha e adicionando ao vetor vec

for i in range(len(vec)):
	
	vec[i]=float(vec[i])-1 #transformando a string em float

v =np.arange(0,len(vec),1) #criando um vetor do tamanho do arquivo 	

plt.grid(True)
#plt.title("Autovalores em função dos vertices")
plt.xlabel("n° vertices")
lamb = "\u03BB"
plt.ylabel(lamb)
plt.plot(v,vec, color = 'k') #plotando um grafico de v por vec

plt.show()
pont.close()


