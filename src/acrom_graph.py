# ***************************************************************************************************************************************************************
# ACROM
# Astronomy and Astrophysics - VIU (Valencian International University) 2014 ===<v.04122014>== Derian Jesus Dorado-Daza
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Acrom_Graph: Codigo para graficar y verificar el ajuste realizado en acrom_detrend.py, Compara las curvas de luz con y sin detrending.
# ***************************************************************************************************************************************************************


from __future__ import division
import fileinput
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from numpy import linspace, loadtxt, ones, convolve
import numpy as numpy


# ======== Plot Curva ROJA ========
print "Nombre del archivo de la curva de luz Roja filtrada (p.ej: R_222043.txt):"
filenameR=raw_input()

data = loadtxt(filenameR, float)
x = data[:,0]
y = data[:,1]
plot(x,y,"k.", color='red')

print "Nombre del archivo de la curva de luz Roja con detrending (p.ej: det_R_222043.txt):"
filenameRd=raw_input()

data1 = loadtxt(filenameRd, float)
x1 = data1[:,0]
y_av = data1[:,1]
#t1 = len(x1)
plot(x1, y_av,"r", color='black') 




# ======== Plot Curva VERDE ========
print "Nombre del archivo de la curva de luz Verde (G) filtrada (p.ej: G_222043.txt):"
filenameG=raw_input()

datag = loadtxt(filenameG, float)
xg = datag[:,0]
yg = datag[:,1]
plot(xg,yg,"k.", color='green')
 
print "Nombre del archivo de la curva de luz Verde (G) con detrending (p.ej: det_G_222043.txt):"
filenameGd=raw_input()

data1g = loadtxt(filenameGd, float)
x1g = data1g[:,0]
y_avg = data1g[:,1]
plot(x1g, y_avg,"r", color='black')


# ======== Plot Curva AZUL ========
print "Nombre del archivo de la curva de luz Azul (B) filtrada (p.ej: B_222043.txt):"
filenameB=raw_input()
datab = loadtxt(filenameB, float)
xb = datab[:,0]
yb = datab[:,1]
plot(xb,yb,"k.", color='blue')

print "Nombre del archivo de la curva de luz Azul (B) con detrending (p.ej: det_B_222043.txt):"
filenameBd=raw_input()
data1b = loadtxt(filenameBd, float)
x1b = data1b[:,0]
y_avb = data1b[:,1]
plot(x1b, y_avb,"r", color='black')

# ======== // ========

xlim(2690,2840)
ylim(50000,600000)
xlabel("DateHel")
ylabel("Flux")
grid(True)

show()
