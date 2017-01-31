# ***************************************************************************************************************************************************************
# ACROM
# Astronomy and Astrophysics - VIU 2014 ===<v.04122014>== Derian Jesus Dorado-Daza
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
# Acrom_Filter: Codigo para dividir los colores (R,G,B) de las Curvas de luz CoRoT y filtrar los puntos etiquetados como 'malos' (aquellos con status > 0)
# ***************************************************************************************************************************************************************

import fileinput, time
import numpy as numpy


print ""
print "====================================================================================================="
print "A partir de una curva de luz cruda de CoRoT en formato ASCII sin cabeceras (p.ej: corot-2b.txt)," 
print "acrom_filter.py permite filtrar puntos 'malos' (status > 0) y generar las subcurvas de luz"
print "Roja(R), Verde(G) y Azul(B)."
print "====================================================================================================="
print ""
print "INGRESE NOMBRE DE ARCHIVO (p.ej: filename.txt):"

# ====== Parametros de Entrada ======
date=time.strftime("%H%M%S")
filename=raw_input()


# Preparacion de Listas/Arrays para separacion de las respectivas Columnas de datos
datehel = []
red = []
green = []
blue = []
status = []



# Acceso al file con la curva de luz CoRoT y asignacion de los colores, tiempo (DateHel), Status a las respectivas listas

with open(filename) as f:
    for l in f.readlines():
        l = l.split()
        datehel.append(float(l[2]))
        red.append(float(l[3]))
        green.append(float(l[5]))
        blue.append(float(l[7]))
        status.append(float(l[10]))

nlineas=len(open(filename).readlines())


# Preparacion de Archivos para guardar los colores filtrados

alred   =   open("R"+"_"+str(date)+".txt",'w')
algreen =   open("G"+"_"+str(date)+".txt",'w')
alblue  =   open("B"+"_"+str(date)+".txt",'w')


# Separacion de colores y copia de los datos a los respectivos archivos

for i in range(0,nlineas):
  if status[i] == 0.0:

     alred.write(str('%s\t\t') % datehel[i])
     alred.write(str('%s\n') % red[i] )
     
     algreen.write(str('%s\t\t') % datehel[i])
     algreen.write(str('%s\n') % green[i])

     alblue.write(str('%s\t\t') % datehel[i])
     alblue.write(str('%s\n') % blue[i])


# =============== Resultados =================#

print "\n==== NOTIFICACION DE RESULTADOS - [acrom_filter.py] --- A&A - VIU - 2014  ==== \n"

print "El archivo tiene:" + str(nlineas) + "\tpuntos de datos"
print "Se crearon los archivos:" + "R"+"_"+str(date)+".txt" + "," + "G"+"_"+str(date)+".txt" + "," + "B"+"_"+str(date)+".txt"


