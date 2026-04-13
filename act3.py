
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# -------------------------------
# 1. Definición del tiempo
# -------------------------------
fs = 1000  # frecuencia de muestreo
t = np.linspace(0, 1, fs)

# -------------------------------
# 2. Señal de prueba (mezcla + ruido)
# -------------------------------
# Señales de diferentes frecuencias
senal = (np.sin(2*np.pi*5*t) +
         np.sin(2*np.pi*50*t) +
         np.sin(2*np.pi*120*t))

# Ruido blanco
ruido = np.random.normal(0, 0.5, len(t))

senal_ruidosa = senal + ruido

# -------------------------------
# 3. Diseño de filtros
# -------------------------------

# Filtro pasa bajas (Butterworth)
b_low, a_low = signal.butter(4, 20, btype='low', fs=fs)

# Filtro pasa altas
b_high, a_high = signal.butter(4, 40, btype='high', fs=fs)

# Filtro pasa bandas
b_band, a_band = signal.butter(4, [40, 100], btype='band', fs=fs)

# -------------------------------
# 4. Aplicar filtros
# -------------------------------
senal_low = signal.filtfilt(b_low, a_low, senal_ruidosa)
senal_high = signal.filtfilt(b_high, a_high, senal_ruidosa)
senal_band = signal.filtfilt(b_band, a_band, senal_ruidosa)

# -------------------------------
# 5. Función para graficar
# -------------------------------
def graficar(original, filtrada, titulo):
    plt.figure(figsize=(10,4))
    plt.plot(t, original, label="Original")
    plt.plot(t, filtrada, label="Filtrada")
    plt.title(titulo)
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.show()

# -------------------------------
# 6. Graficar resultados
# -------------------------------
graficar(senal_ruidosa, senal_low, "Filtro Pasa Bajas")
graficar(senal_ruidosa, senal_high, "Filtro Pasa Altas")
graficar(senal_ruidosa, senal_band, "Filtro Pasa Bandas")
