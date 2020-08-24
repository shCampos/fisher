import numpy as np
import statistics as st

def tratarDados(d):
    dSeparado = d.split(',')
    if len(dSeparado)>1:
        return [float(dSeparado[0]), int(dSeparado[1])]
    else:
        return [float(dSeparado[0]), 1]

dados = list(map(tratarDados, input('Digite os números:\n').split()))
print(dados)

print("Media: ", np.average(dados))
print("Mediana: ", np.median(dados))
#print("Moda: ", st.mode(dados))
print("Amplitude: ", np.ptp(dados))
print("Desvio padrão: ", np.std(dados))
print("Variancia: ", np.var(dados))
