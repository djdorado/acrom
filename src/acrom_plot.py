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
# Acrom_plot: Codigo para graficar Curvas de luz
# ***************************************************************************************************************************************************************


from __future__ import division
import fileinput, time
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from numpy import linspace, loadtxt, ones, convolve
import numpy as numpy


print ""
print "========================================================================================================================"
print "Acrom_Plot que permite graficar una curva de luz de CoRoT desde un archivo con dos columnas: Flujo (e-/s)vs Tiempo (DJH)"
print "========================================================================================================================"
print ""
print "INGRESE NOMBRE DE ARCHIVO (p.ej: filename.txt):"


# ====== Parametros de Entrada ======
filename=raw_input()


# ======== Plot Curvas de Luz ========

data = loadtxt(filename,float)
x = data[:,0]
y = data[:,1]

tig=len(y)
f=x[tig-1]

plot(x,y,"k.", color='red')

# ======== // ========

xlim(x[0],f)
ylim(0,600000)
xlabel("DJH")
ylabel("Flux")
grid(True)

show()
