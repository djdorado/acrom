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
# Acrom_ph: Codigo que aplica folding phase a las curvas de luz R,G,B 
# ***************************************************************************************************************************************************************


from __future__ import division
import fileinput, time
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from numpy import linspace, loadtxt, ones, convolve
import numpy as numpy


# ===<*>=== Parametros de Entrada ===<*>===
date=time.strftime("%H%M%S") 

print "INGRESE PERIODO ORBITAL DEL EXOPLANETA (P.ej: para corot-2b el periodo orbital=1.7429):"
periodo_orb= float(input())





# ============ RED LC =================#
print "Nombre del archivo de la curva de luz Roja:"
filenameR=raw_input()
# Acceso al file con la curva de luz ROJA con detrending
datar = loadtxt(filenameR,float)
xr = datar[:,0]
yr = datar[:,1]
zr = datar[:,2]
tir=len(yr)
#print "ctl -> tir=" + str(tir)   # linea de control

media_lred = numpy.mean(zr)  
stdl = numpy.std(zr)                    


red_ph = open("ph_R_"+str(date)+".txt",'w')

x_ph=[]
for i in range (0,tir):
  x_dif = xr[i]-xr[0]
  x_div = x_dif/periodo_orb
  x_phd = x_div - int(x_div)
  x_ph.append(x_phd)

# Asignacion de valores al archivo avred.txt
for i in range(0,tir):
  red_ph.write(str('%s\t') % x_ph[i]) 
  red_ph.write(str('%s\n') % zr[i])


# ============ GREEN LC =================#
print "Nombre del archivo de la curva de luz Verde:"
filenameG=raw_input()

# Acceso al file con la curva de luz ROJA con detrending
datag = loadtxt(filenameG,float)

xg = datag[:,0]
yg = datag[:,1]
zg = datag[:,2]
tig=len(yg)
 

media_lgreen = numpy.mean(zg)  # Media del flujo normalizado
stdlg = numpy.std(zg)         # Desviacion Estandar del flujo normalizado           

green_ph = open("ph_G_"+str(date)+".txt",'w')

xg_ph=[]
for i in range (0,tig):
  xg_dif = xg[i]-xg[0]
  xg_div = xg_dif/periodo_orb
  xg_phd = xg_div - int(xg_div)
  xg_ph.append(xg_phd)

# Asignacion de valores al archivo avred.txt
for i in range(0,tig):
  green_ph.write(str('%s\t') % xg_ph[i]) 
  green_ph.write(str('%s\n') % zg[i])


# ============ BLUE LC =================#

print "Nombre del archivo de la curva de luz Azul:"
filenameB=raw_input()

# Acceso al file con la curva de luz ROJA con detrending
datab = loadtxt(filenameB,float)
xb = datab[:,0]
yb = datab[:,1]
zb = datab[:,2]
tib=len(yb)

media_lblue = numpy.mean(zb)  # Media del flujo normalizado
stdlb = numpy.std(zb)         # Desviacion Estandar del flujo normalizado           


blue_ph = open("ph_B_"+str(date)+".txt",'w')

xb_ph=[]
for i in range (0,tib):
  xb_dif = xb[i]-xb[0]
  xb_div = xb_dif/periodo_orb
  xb_phd = xb_div - int(xb_div)
  xb_ph.append(xb_phd)

# Asignacion de valores al archivo
for i in range(0,tib):
  blue_ph.write(str('%s\t') % xb_ph[i]) 
  blue_ph.write(str('%s\n') % zb[i])


# =============== Resultados =================#

print "\n==== NOTIFICACION DE RESULTADOS - [acrom_ph.py] --- A&A - VIU - 2014  ==== \n"

print "=== 1.- FASE - LC RED ==="
print "1.1.- Numero de puntos en la curva de luz roja (R) =" + str(tir)
print "1.2.- Media - dataset flujo normalizado det_red.txt =" + str(media_lred)  
print "1.3.- Desviacion Estandar (STD) - dataset det_red.txt - flujo normalizado =" + str(stdl)
print "1.4.- Periodo orbital =" + str(periodo_orb)

print "=== 1.- FASE - LC GREEN ==="
print "2.1.- Numero de puntos en la curva de luz verde (G) =" + str(tig)
print "2.2.- Media - dataset flujo normalizado det_green.txt =" + str(media_lgreen)  
print "2.3.- Desviacion Estandar (STD) - dataset det_green.txt - flujo normalizado =" + str(stdlg)
print "2.4.- Periodo orbital =" + str(periodo_orb)

print "=== 1.- FASE - LC BLUE ==="
print "3.1.- Numero de puntos en la curva de luz azul (B) =" + str(tib)
print "3.2.- Media - dataset flujo normalizado det_green.txt =" + str(media_lblue)  
print "3.3.- Desviacion Estandar (STD) - dataset det_green.txt - flujo normalizado =" + str(stdlb)
print "3.4.- Periodo orbital =" + str(periodo_orb)

print "4.- Se han generado los archivo de fase plegada para cada color (R,G,B) que contienen las columnas DateHel rango 0-1, flujo normalizado\n"
