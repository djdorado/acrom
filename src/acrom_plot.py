from __future__ import division
import fileinput, time
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from numpy import linspace, loadtxt, ones, convolve
import numpy as numpy



# ***************************************************************************************************************************************************************
# ===<>=== Astronomia y Astrofisica - VIU 2014 ===version 2017-10-25===
# Acrom_Graph: Codigo para graficar Curvas de luz
# ***************************************************************************************************************************************************************



print ""
print "========================================================================================================================"
print "Acrom_Plot que permite graficar una curva de luz de CoRoT desde un archivo con dos columnas: Flujo (e-/s)vs Tiempo (DJH)"
print "========================================================================================================================"
print ""
print "INGRESE NOMBRE DE ARCHIVO (p.ej: filename.txt):"


# ====== Parametros de Entrada ======
filename=raw_input()

print "INGRESE Escala (Y):"
escala = int(input())

print "INGRESE color:"
col = raw_input()


# ======== Plot Curvas de Luz ========


data = loadtxt(filename,float)
x = data[:,0]
y = data[:,1]

tig=len(y)
f=x[tig-1]

plot(x,y,"k.", color=col)

# ======== // ========

xlim(x[0],f)
ylim(0,escala)
xlabel("DJH")
ylabel("Flux")
grid(True)

show()
