#!/usr/bin/python
 
import math as m
import numpy as np 
import datetime

print ('{:%Y%m%d%H%M%S}'.format(datetime.datetime.now()))
anno = str('{:%Y}'.format(datetime.datetime.now()))
mese = str('{:%m}'.format(datetime.datetime.now()))
giorno = str('{:%d}'.format(datetime.datetime.now()))
ora1 = str('{:%H}'.format(datetime.datetime.now()))
min1 = str('{:%M}'.format(datetime.datetime.now()))
sec1 = str('{:%S}'.format(datetime.datetime.now()))

L = 12.452
la = 41.922
Legale = 2.0


#anno = "1978"
#mese = "11"
#giorno = "13"
ora = "0"
min = "0"
sec = "0"
ora1 = str(float(ora1) - Legale)
#min1 = "34"
#sec1 = "0"

mese = mese.zfill(2)
giorno = giorno.zfill(2)

print (anno,mese, giorno, ora, min , sec)

dd = int(((float(ora)/24)+ (float(min)/(24*60)) + (float(sec)/(24*3600)))*100)
DD = float(giorno) + float(dd)/100

print ("calcolo 1: " + str(dd))
print ("calcolo 2: " + str(DD))

data = float(anno+"."+mese+giorno+str(dd))

print ("stringa corretta numerica: " + str(data))

mese = int(mese)
anno = int(anno)

if ( mese > 2 ):
	y = anno
	m = mese
elif ( mese == 1 or mese == 2 ):
		y = anno-1
		m = mese+12
else:
	print ("non ho capito nulla")

print ("anno y: " + str(y))
print ("il mese m:" + str(m))	
	
if ( data < 1582.1015 ):
	A = 0
	B = 0
	print ("caso inferiore a 1582")
else:
	A = int(float(y)/100)
	B = 2 - A + int((A/4))
	print ("caso superiore a 1582")

print (A, B)

JD = int(365.25*(y+4716)) + int(30.6001*(m+1)) + DD + B - 1524.5

print ("Giulian Day = ",JD)

T = (JD - 2415020.0)/36525


th0 = float(0.276919398 + 100.0021359 * T + 0.000001075 * T * T )

print (T)
print (th0)
th0 = (th0-int(th0))*24
print (th0)

err = float(ora1)+float(min1)/60+float(sec1)/3600
print(err)

TSG = th0 + err * 1.002737908
TSG = TSG - (int(TSG/24)*24)

print ("Tempo Siderale medio: " + str(TSG))

arh = input('Inserisci AR: +hh --> ')
arm = input('Inserisci AR: +mm --> ')
ars = input('Inserisci AR: +ss --> ')

ar = (float(arh) + float(arm)/60 + float(ars)/3600)
print ("AR = " + str(ar))
deh = input('Inserisci Decl: +gg --> ')
dem = input('Inserisci Decl: +mm --> ')
des = input('Inserisci Decl: +ss --> ')
de = float(deh) + float(dem)/60 + float(des)/3600

H = TSG + (float(L)/float(15)) - ar


print ("Angolo Orario= " + str(H))

Hh = int(H)
p = (H - Hh)*60
print("p " + str(p))
Hm = int(p)
Hs = ( p - Hm )*60

print ("Angolo Orario= " + str(Hh) +"h " +str(Hm) + "m "+str(Hs))

print (de)
print (np.radians(de))
alt = np.arcsin(np.sin(np.radians(de))*np.sin(np.radians(la))+np.cos(np.radians(de))*np.cos(np.radians(la))*np.cos(np.radians(H*15)))

print ("altezza = " + str(np.degrees(alt)))
print ("Azimut = " + str(((H*15.0))))
