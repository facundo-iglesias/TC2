#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:47:48 2023

@author: facu
"""
# Inicialización e importación de módulos

# Módulos para Jupyter
import warnings
warnings.filterwarnings('ignore')

# Módulos importantantes
import scipy.signal as sig
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio
from pytc2.sistemas_lineales import plot_plantilla


############################## Nyquist
fs = 1000 # Hz
nyq_frec = fs / 2

############################## Plantilla
# filter design
ripple = 0.5 # dB
gpass= 0.5
atenuacion = 40 # dB
ws1 = 1.0 #Hz
wp1 = 3.0 #Hz
wp2 = 25.0 #Hz
ws2 = 35.0 #Hz

############################################### FILTRO IIR ##############################

############################### Diseño del filtro sos
H_z = sig.iirdesign(wp=[wp1,wp2], ws=[ws1,ws2], gpass=gpass,
                           gstop=atenuacion, analog=False, ftype='butter', output='sos', fs=fs)

############################### Diseño del filtro ba
numZ, denZ = sig.iirdesign(wp=[wp1,wp2], ws=[ws1,ws2], gpass=gpass,
                           gstop=atenuacion, analog=False, ftype='butter', output='ba', fs=fs)

print(len(numZ))

############################## Respuesta para sos
wrad, hh = sig.sosfreqz(H_z, worN=1000)
ww = wrad / np.pi
############################## Respuesta para ba
wrad2, hh2 = sig.freqz(numZ, denZ, worN=1000)
ww2 = wrad2 / np.pi

############################# Visualizacion
#Grafico de modulo
#plt.figure(1)
#plt.plot(ww,20*np.log10(np.abs(hh)))
#plt.plot(ww2,20*np.log10(np.abs(hh2)))
#plt.title('IIR filter')
#plt.xlabel('Frecuencia')
#plt.ylabel('Modulo [dB]')
#plt.grid(which='both',axis='both')

#Gráfico de fase 
#plt.figure(2)
#plt.plot(ww,20*np.log10(np.angle(hh)))
#plt.plot(ww2,20*np.log10(np.angle(hh2)))
#plt.title('IIR filter')
#plt.xlabel('Frecuencia')
#plt.ylabel('Fase')
#plt.grid(which='both',axis='both')

#Para calcular la respuesta al impulso:
    #A) Antitransformada Z da el impulso (buscando equivalencias, tabla etc.)
    #B) Teniendo la respuesta al impulso en modulo y fase (numericamente) se puede realizar
    #   la transformada de Fourier discreta.

############################################### FILTRO FIR ##############################
#Usar cualquiera de las siguientes o el de ventana (suboptimo)
numtaps =  1501
bands = 

sig.firls(numtaps, bands, desired)

#sig.remez(numtaps, bands, desired)
#La respuesta al impulso son los propios coefcientes ya que denominador=1

############################################### PARTE 2 ##############################
# Se deben usar los coeficientes del SOS.





