import numpy as np
import statistics as st

dados = list(map(float, input('Digite os números:\n').split()))

print("Media: ", np.mean(dados))
print("Mediana: ", np.median(dados))
print("Moda: ", st.mode(dados))
print("Amplitude: ", np.ptp(dados))
print("Desvio padrão: ", np.std(dados))
print("Variancia: ", np.var(dados))
