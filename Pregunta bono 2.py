# Electro I. Pregunta bono 2: Análisis en DC gráfico.
# Autor : Rafael Moreno
# Fecha : 24/01/20
# Prof  : Anibal Carpio

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Open file
filename = 'Grafica Diodo 1-n4004 GP.csv'
data = pd.read_csv(filename)

# Diode I-V characteristics
Vd = data['X--Trace 1::[V_pn]']
Id = data['Y--Trace 1::[V_pn]']    

# Load line
Il = 5 / 2000 - np.dot(Vd, 1/2000)      # Il = Vps / R - Vd / R

# (A) to (mA)
Id = np.dot(Id,1000)
Il = np.dot(Il,1000)

# primero se calcula Il - Id
# se obtienen los signos correspondientes con np.sign
# se determina el cambio de signo con np.diff (donde se cruzan las lineas)
# se determina el índice de dicho cambio con np.argwhere
# flatten devuelve el arreglo en una dimension
idx = np.argwhere(np.diff(np.sign(Il - Id))).flatten()


# Plotting
plt.plot(Vd, Id, label = 'Característica I-V del Diodo')
plt.plot(Vd, Il, label = 'Linea de carga')
plt.ylim(0, 3)
plt.grid()
plt.ylabel('Id (mA)')
plt.xlabel('Vd (V)')
plt.title('Análisis en DC Gráfico')
plt.plot(Vd[idx], Id[idx], 'ro', label = f'Q-point ({Vd[int(idx)]} V,{float(Id[idx])} mA)')
plt.legend(loc = 'best')
plt.show()
