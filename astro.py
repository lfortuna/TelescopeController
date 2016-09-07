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
#JD = 2443825.69

T = (JD - 2415020.0)/36525

print ("T: " + str(T))

####### correzione nutazione  ######
lms = float(279.6967 + 36000.7689 * T + 0.000303 * T * T)
lml = float(270.4342 + 481267.8831 * T - 0.001133 * T * T)
ams = float(358.4758 + 35999.0498 * T - 0.000150 * T * T - 0.0000033 * T * T * T)
aml = float(296.1046 + 477198.8491 * T + 0.009192 * T * T)
lnal = float(259.1833 -1934.1420 * T + 0.002078 * T * T) 
e = float(0.01675104 - 0.0000418 * T - 0.000000126 * T * T)
m = float(3.07234 + 0.00186 * T)
n = float(20.0468 - 0.0085 * T)
epsi = float(23.452294 - 0.0130125 * T - 0.00000164 * T * T - 0.000000503 * T * T * T)

print (lms)
print lml
print (ams)
print (aml)
print (lnal)
print ("e: " + str(e))

dpsi = - float(17.2327+0.01737 * T) * np.sin(lnal) - float(1.2729+0.00013 * T) * np.sin(2*lms) + 0.2088 * np.sin(2*lnal)-0.2037 * np.sin(2*lml) +(0.1261 - 0.00031 * T) * np.sin(ams) + 0.0675 * np.sin(aml)-float(0.0497-0.00012 *T) * np.sin(2*lms+ams) -0.0342 * np.sin(2*lml - lnal)-0.0261*np.sin(2*lml + aml)+0.0214+np.sin(2*lms - ams)-0.0149*np.sin(2*lms-2*lml+ams)+0.0124 *np.sin(2*lms - lnal)+0.0114*np.sin(2*lml-aml)
print ("dpsi: " + str(dpsi))

depsi = float(9.2100+0.00091 * T) *np.cos(lnal)+float(0.5522-0.00029 * T)* np.cos(2*lms) - 0.0904 * np.cos(2*lnal) +0.0884 * np.cos(2*lml) + 0.0216 * np.cos(2*lml+ams)+0.0183* np.cos(2*lml-lnal)+0.0113 * np.cos(2*lml +aml)-0.0093 *np.cos(2*lms-ams)-0.0066*np.cos(2*lms-lnal)
print ("depsi: " + str(depsi))

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
print ("")
print ("AR e Decl inserite")
print ("AR = " + str(ar))
print (de)
print (np.radians(de))


da = float(m+n*np.sin(np.radians(ar/15))*np.tan(np.radians(de)))
dd = float(n*np.cos(ar))

ar = ar + da/3600
de = de + dd/(3600*15)
print ("")
print ("AR e Decl alla data")
print ("AR corretta = " + str(int(ar)) + "h " + str(int((ar-int(ar))*60)) + "m " + str(int((((ar-int(ar))*60) - (int((ar-int(ar))*60)))*60))+ "s")         
print ("Decl corretta = " + str(int(de)) + "h " + str(int((de-int(de))*60)) + "m " + str(int((((de-int(de))*60) - (int((de-int(de))*60)))*60))+ "s")
print ("")

da = float((np.cos(np.radians(epsi))+np.sin(np.radians(epsi))*np.sin(np.radians(ar/15))*np.tan(np.radians(de)))*dpsi - (np.cos(np.radians(ar/15))*np.tan(np.radians(de)))*depsi)
dd = float((np.sin(np.radians(epsi))*np.cos(np.radians(ar/15)))*dpsi+(np.sin(np.radians(ar/15)*depsi)))

print ("correzioni --> Dar= " +str(da) + " Ddelta= "+ str(dd))

da = float (da/3600)
dd = float (dd/3600)

ar = float(ar + da)
de = float(de + dd)

print ("")
print ("AR e d -J2000 correz --> ")
print ("AR corretta = " + str(int(ar)) + "h " + str(int((ar-int(ar))*60)) + "m " + str(int((((ar-int(ar))*60) - (int((ar-int(ar))*60)))*60))+ "s")         
print ("Decl corretta = " + str(int(de)) + "h " + str(int((de-int(de))*60)) + "m " + str(int((((de-int(de))*60) - (int((de-int(de))*60)))*60))+ "s")
print "________________ finora corretto _______________________"

H = TSG + (float(L)/float(15)) - ar


print ("Angolo Orario= " + str(H))

Hh = int(H)
p = (H - Hh)*60
print("p " + str(p))
Hm = int(p)
Hs = ( p - Hm )*60

print ("Angolo Orario= " + str(Hh) +"h " +str(Hm) + "m "+str(Hs))

alt = np.arcsin(np.sin(np.radians(de))*np.sin(np.radians(la))+np.cos(np.radians(de))*np.cos(np.radians(la))*np.cos(np.radians(H*15)))

Azimut = float(H*15.0+180)
Altezza = float(np.degrees(alt))
print ("Azimut - altezza --> " + str(Azimut) + " " + str(Altezza))
print ("Azimut = " + str(int(Azimut)) + "h " + str(int((Azimut-int(Azimut))*60)) + "m " + str(int((((Azimut-int(Azimut))*60) - (int((Azimut-int(Azimut))*60)))*60))+ "s")
print ("Altezza = " + str(int(Altezza)) + "h " + str(int((Altezza-int(Altezza))*60)) + "m " + str(int((((Altezza-int(Altezza))*60) - (int((Altezza-int(Altezza))*60)))*60))+ "s")

