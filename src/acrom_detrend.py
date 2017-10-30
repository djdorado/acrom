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
print "A partir de las subcurvas de luz R,G,B filtradas y separadas en respectivos archivos, acrom_detrend.py" 
print "aplica un caso especifico de Convolucion (Promedios Moviles) para eliminar la tendencia de largo" 
print "termino de las curvas de luz (R,G,B) de CoRoT"
print "==================================================o==================================================="
print ""
print "INGRESE LOS NOMBRES DE LOS ARCHIVOS OBTENIDOS CON ACROM_FILTER"



# ====== Parametros de Entrada ======
date=time.strftime("%H%M%S")

print "INGRESE valor n (sugerido n = Numero total de puntos de datos de la CL/Numero de dias de observacion):"
nvalor = float(input())

nvalh= nvalor/2

# Definicion de funcion para el procedimiento de convolucion sobre la curva de luz Roja

def movingaverage(interval, window_size):
    window= numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'valid')


# ============ RED LC =================#
print "Nombre del archivo de la subcurva de luz roja (P. ej: R__222043.txt):"
filenameR=raw_input()

# Acceso al file con la curva de luz ROJA
datar = loadtxt(filenameR , float)
xr = datar[:,0]
yr = datar[:,1]
tir=len(yr)

media_lred = numpy.mean(yr)  
stdl = numpy.std(yr)                    

# Aplicacion de la convolucion sobre la columna de flujo del archivo lred.txt [movingaverage()] . Numero de elementos [len()] . Desviacion Estandar [numpy.std()]

y_avr = movingaverage(yr, nvalor)
av_red = open("det_R"+"_"+str(date)+".txt",'w')
tr = len(y_avr) 
media_avred=numpy.mean(y_avr)
stdav=numpy.std(y_avr)

# Normalizacion del flujo resultado de la convolucion
lredavnorm1=[]
for i in range(0,tr):
  lredavnorm = yr[i+nvalh]/y_avr[i]
  lredavnorm1.append(lredavnorm)
stdr = numpy.std(lredavnorm1)
mediaredavnorm=numpy.mean(lredavnorm1)

print "=== INICIA Algoritmo Sigma-clipping para curva de luz Roja (R): ==="
print "Desviacion Estandar (STD) - dataset de la curva de luz Roja (R) =" + str(stdl)
print "INGRESE valor Sigma para Sigma-clipping (Un rango sugerido para este valor es {0 a 3}). 4 para omitir Sigma-Clipping:"


sigmaR = float(input())
# Aplicacion de Sigma Clipping para remocion de puntos
lcrmin=mediaredavnorm - sigmaR*stdr

if sigmaR <= 3: 
# Asignacion de valores al archivo avred.txt
 for i in range(0,tr):
  if lredavnorm1[i] < lcrmin:
   av_red.write(str('%s\t') % xr[i+nvalh]) 
   #av_red.write(str('%s\t') % y_avr[i] ) Eliminar comentario si se desea la columna de flujo sin normalizar
   av_red.write(str('%s\n') % lredavnorm1[i] )
else:
 for i in range(0,tr):
   av_red.write(str('%s\t') % xr[i+nvalh]) 
   #av_red.write(str('%s\t') % y_avr[i] ) Eliminar comentario si se desea la columna de flujo sin normalizar
   av_red.write(str('%s\n') % lredavnorm1[i] )
 

# =============== GREEN LC =================#
print "Nombre del archivo de la curva de luz Verde (G) (P. ej: G__222043.txt):"
filenameG=raw_input()

# Acceso al file con la curva de luz VERDE
datag = loadtxt(filenameG,float)
xg = datag[:,0]
yg = datag[:,1]
tig=len(yg)

media_lgreen = numpy.mean(yg)  
stdlg = numpy.std(yg)    

y_avg = movingaverage(yg,nvalor)
av_green = open("det_G"+"_"+str(date)+".txt", 'w')
tg = len(y_avg)
media_avgreen=numpy.mean(y_avg)
stdavg=numpy.std(y_avg) 

lgreenavnorm2=[]
for i in range(0,tg):
  lgreenavnorm = yg[i+nvalh]/y_avg[i]
  lgreenavnorm2.append(lgreenavnorm)
stdg = numpy.std(lgreenavnorm2)
mediagreenavnorm=numpy.mean(lgreenavnorm2)

print "=== INICIA Algoritmo Sigma-clipping para curva de luz Verde (G): ==="
print "Desviacion Estandar (STD) - dataset de la curva de luz Verde (G) =" + str(stdlg)
print "INGRESE valor Sigma para Sigma-clipping (Un rango sugerido para este valor es {0 a 3}):"
sigmaG = float(input())

# Aplicacion de Sigma Clipping para remocion de puntos
lcgmin=mediagreenavnorm - sigmaG*stdg

if sigmaG <= 3: 
# Asignacion de valores al archivo avred.txt
 for i in range(0,tg):
  if lgreenavnorm2[i] < lcgmin:
   av_green.write(str('%s\t') % xg[i+nvalh]) 
   #av_green.write(str('%s\t') % y_avg[i] ) Eliminar comentario si se desea la columna de flujo sin normalizar
   av_green.write(str('%s\n') % lgreenavnorm2[i] )
else:
 for i in range(0,tg):
   av_green.write(str('%s\t') % xg[i+nvalh]) 
   #av_green.write(str('%s\t') % y_avg[i] ) Eliminar comentario si se desea la columna de flujo sin normalizar
   av_green.write(str('%s\n') % lgreenavnorm2[i] )


# =============== BLUE LC =================#
print "Nombre del archivo de la subcurva de lu azul (P. ej: B__222043.txt):"
filenameB=raw_input()

# Acceso al file con la curva de luz VERDE
datab = loadtxt(filenameB,float)
xb = datab[:,0]
yb = datab[:,1]
tib=len(yb)
media_lblue = numpy.mean(yb)  
stdlb = numpy.std(yb)    

y_avb = movingaverage(yb,nvalor)
av_blue = open("det_B"+"_"+str(date)+".txt", 'w')
tb = len(y_avb)
media_avblue=numpy.mean(y_avb)
stdavb=numpy.std(y_avb) 

lblueavnorm3=[]
for i in range(0,tb):
  lblueavnorm = yb[i+nvalh]/y_avb[i]
  lblueavnorm3.append(lblueavnorm)
stdb = numpy.std(lblueavnorm3)
mediablueavnorm=numpy.mean(lblueavnorm3)


print "=== INICIA Algoritmo Sigma-clipping para curva de luz Azul (B): ==="
print "Desviacion Estandar (STD) - dataset de la curva de luz Azul (B) =" + str(stdlb)
print "INGRESE valor Sigma para Sigma-clipping (Un rango sugerido para este valor es {0 a 3}):"
sigmaB = float(input())

# Aplicacion de Sigma Clipping para remocion de puntos
lcbmin=mediablueavnorm - sigmaB*stdb

if sigmaB <= 3: 
# Asignacion de valores al archivo avred.txt
 for i in range(0,tb):
  if lblueavnorm3[i] < lcbmin:
   av_blue.write(str('%s\t') % xb[i+nvalh]) 
   #av_blue.write(str('%s\t') % y_avb[i] ) Eliminar comentario si se desea la columna de flujo sin normalizar
   av_blue.write(str('%s\n') % lblueavnorm3[i] )
else:
 for i in range(0,tb):
   av_blue.write(str('%s\t') % xb[i+nvalh]) 
   #av_blue.write(str('%s\t') % y_avb[i] ) Eliminar comentario si se desea la columna de flujo sin normalizar
   av_blue.write(str('%s\n') % lblueavnorm3[i] )



# =============== Resultados =================#

print "\n==== NOTIFICACION DE RESULTADOS - [acrom_detrend.py] --- A&A - VIU - 2013  ==== \n"

print "=== 1.- LC RED ==="
print "1.1.- Numero de puntos en curva de luz roja (R) =" + str(tir)
print "1.2.- Media - en curva de luz Roja =" + str(media_lred)  
print "1.3.- Desviacion Estandar (STD) del flujo en curva de luz Roja =" + str(stdl)
print "1.4.- valor n aplicado =" + str(nvalor)
print "1.5.- Numero de puntos en dataset y_avr (Curva de luz Roja ajustada por Convolucion) =" + str(tr)
print "1.6.- Media - dataset y_avr =" + str(media_avred)
print "1.7.- Desviacion Estandar (STD) dataset y_avr =" + str(stdav)

print "1.8.- Media - dataset lredavnorm (Curva de luz Roja ajustada por Convolucion Normalizada) =" + str(mediaredavnorm)
print "1.9.- Desviacion Estandar (STD) - dataset lredavnorm  es:" + str(stdr)            
  
print "1.10.- Valor - Algoritmo ajuste Sigma-Clipping (lcrmin = Media-n*Sigma) lcrmin es:" + str(lcrmin)
print "1.11.- Factor de ajuste (n) aplicado - Sigma Clipping =" + str(sigmaR)

print "1.12.- Se ha generado el archivo det_R_...txt que contiene las columnas DateHel, Convolucion de Redflux, Convolucion_Redflux Normalizado\n"

print "=== 2.- LC GREEN ==="
print "2.1.- Numero de puntos en curva de luz verde (G) =" + str(tig)
print "2.2.- Media - en curva de luz verde (G) =" + str(media_lgreen)  
print "2.3.- Desviacion Estandar (STD) del flujo en curva de luz verde (G):" + str(stdlg)

print "2.4.- Numero de puntos en dataset y_avg (Curva de luz verde ajustada por Convolucion) =" + str(tg)  
print "2.5.- Media - dataset y_avg=" + str(media_avgreen)
print "2.6.- STD - dataset y_avg =" + str(stdavg)

print "2.7.- Media - dataset lgreenavnorm (Curva de luz verde ajustada por Convolucion Normalizada) =" + str(mediagreenavnorm)
print "2.8.- STD - dataset lgreenavnorm  es:" + str(stdg) 

print "2.9.- Valor - Algoritmo ajuste Sigma-Clipping (lcgmin = Media-n*Sigma) lcrmin es:" + str(lcgmin)
print "2.10.- Factor de ajuste (n) aplicado - Sigma Clipping = " + str(sigmaG)

print "2.11.- Se ha generado el archivo det_G_...txt que contiene las columnas DateHel, Convolucion de Greenflux, Convolucion_Greenflux Normalizado\n"

print "=== 3.- LC BLUE ==="
print "3.1.- Numero de puntos en curva de luz Azul (B) =" + str(tib)
print "3.2.- Media - en curva de luz azul (B) =" + str(media_lblue)  
print "3.3.- Desviacion Estandar -STD- del flujo en curva de luz azul (B):" + str(stdlb)

print "3.4.- Numero de puntos en dataset y_avb (Curva de luz azul (B) ajustada por Convolucion) =" + str(tb)  
print "3.5.- Media - dataset y_avb =" + str(media_avblue)
print "3.6.- STD - dataset y_avb =" + str(stdavb)

print "3.7.- Media - dataset lblueavnorm (curva de luz Azul ajustada por Convolucion Normalizada) =" + str(mediablueavnorm)
print "3.8.- STD - dataset lgreenavnorm  es:" + str(stdb) 

print "3.9.- Valor - Algoritmo ajuste Sigma-Clipping (lcgmin = Media-n*Sigma) lcrmin es:" + str(lcbmin)
print "3.10.- Factor de ajuste (n) aplicado - Sigma Clipping = " + str(sigmaB)

print "3.11.- Se ha generado el archivo det_B_...txt que contiene las columnas DateHel, Convolucion de Blueflux, Convolucion_Blueflux Normalizado\n"

