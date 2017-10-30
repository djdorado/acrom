from __future__ import division
import fileinput, time
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from numpy import linspace, loadtxt, ones, convolve
import numpy as numpy

# ***************************************************************************************************************************************************************
# ===<>=== Astronomia y Astrofisica - VIU 2014 ===<>===
# Acrom_Detrend: Codigo que aplica Convolucion y Sigma-Clipping para ajuste de las curvas de luz cromaticas y eliminar la tendencia de largo plazo de las curvas.
# ***************************************************************************************************************************************************************

print ""
print "==================================================o==================================================="
print "A partir de las subcurvas con Detrending DR,DG,DB, acrom_split.py" 
print "aplica recorte a los transitos mas fuertes como entrada al binning-phase y folding-phase" 
print "termino de las curvas de luz (R,G,B) de CoRoT"
print "==================================================o==================================================="
print ""
print "INGRESE LOS NOMBRES DE LOS ARCHIVOS OBTENIDOS CON ACROM_DETREND"



# ====== Parametros de Entrada ======
date=time.strftime("%H%M%S")

print "INGRESE valor umbral 1:"
umbral1 = float(input())
print "INGRESE valor umbral 2:"
umbral2 = float(input())

# Definicion de funcion para el procedimiento de convolucion sobre la curva de luz Roja

# ============ RED LC =================#
print "Nombre del archivo de la subcurva -detrend- de luz roja (P. ej: det_R__222043.txt):"
filenameR=raw_input()

# Acceso al file con la curva de luz ROJA
datar = loadtxt(filenameR , float)
xr = datar[:,0]
yr = datar[:,1]
tir=len(yr)
cut_red = open("cut_R"+"_"+str(date)+".txt",'w')

media_lred = numpy.mean(yr)  
stdl = numpy.std(yr)                    

for i in range(0,tir):
 if  umbral1 <= xr[i] <= umbral2:
  cut_red.write(str('%s\t') % xr[i]) 
  cut_red.write(str('%s\n') % yr[i] )
 

# =============== GREEN LC =================#
print "Nombre del archivo de la curva de luz Verde (G) (P. ej: G__222043.txt):"
filenameG=raw_input()

# Acceso al file con la curva de luz VERDE
datag = loadtxt(filenameG,float)
xg = datag[:,0]
yg = datag[:,1]
tig=len(yg)
cut_green = open("cut_G"+"_"+str(date)+".txt",'w')

media_lgreen = numpy.mean(yg)  
stdlg = numpy.std(yg)    


for i in range(0,tig):
 if  umbral1 <= xg[i] <= umbral2:
  cut_green.write(str('%s\t') % xg[i]) 
  cut_green.write(str('%s\n') % yg[i] )
  

# =============== BLUE LC =================#
print "Nombre del archivo de la subcurva de lu azul (P. ej: B__222043.txt):"
filenameB=raw_input()

# Acceso al file con la curva de luz VERDE
datab = loadtxt(filenameB,float)
xb = datab[:,0]
yb = datab[:,1]
tib=len(yb)
cut_blue = open("cut_B"+"_"+str(date)+".txt",'w')

media_lblue = numpy.mean(yb)  
stdlb = numpy.std(yb)    


for i in range(0,tib):
 if  umbral1 <= xb[i] <= umbral2:
  cut_blue.write(str('%s\t') % xb[i]) 
  cut_blue.write(str('%s\n') % yb[i] )

# =============== Resultados =================#

print "\n==== NOTIFICACION DE RESULTADOS - [acrom_detrend.py] --- A&A - VIU - 2013  ==== \n"

print "=== 1.- LC RED ==="
print "1.1.- Numero de puntos en curva de luz roja (R) =" + str(tir)
print "1.2.- Media - en curva de luz Roja =" + str(media_lred)  
print "1.3.- Desviacion Estandar (STD) del flujo en curva de luz Roja =" + str(stdl)
print "1.12.- Se ha generado el archivo cut_R_...txt que contiene las columnas DateHel, Redflux\n"

print "=== 2.- LC GREEN ==="
print "2.1.- Numero de puntos en curva de luz verde (G) =" + str(tig)
print "2.2.- Media - en curva de luz verde (G) =" + str(media_lgreen)  
print "2.3.- Desviacion Estandar (STD) del flujo en curva de luz verde (G):" + str(stdlg)
print "2.11.- Se ha generado el archivo cut_G_...txt que contiene las columnas DateHel, Greenflux\n"

print "=== 3.- LC BLUE ==="
print "3.1.- Numero de puntos en curva de luz Azul (B) =" + str(tib)
print "3.2.- Media - en curva de luz azul (B) =" + str(media_lblue)  
print "3.3.- Desviacion Estandar -STD- del flujo en curva de luz azul (B):" + str(stdlb)
print "3.11.- Se ha generado el archivo cut_B_...txt que contiene las columnas DateHel, Blueflux Normalizado\n"
