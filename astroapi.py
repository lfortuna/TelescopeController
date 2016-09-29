#!/usr/bin/python
 
import math as m
import numpy as np 
import datetime

def ridgrd(gradi):
	return(gradi - 360*int(gradi/360))

def posizione(aretta,declinazione,longitudine,latitudine,legale):
	
	anno = str('{:%Y}'.format(datetime.datetime.utcnow()))
	mese = str('{:%m}'.format(datetime.datetime.utcnow()))
	giorno = str('{:%d}'.format(datetime.datetime.utcnow()))
	oral = str('{:%H}'.format(datetime.datetime.utcnow()))
	minl = str('{:%M}'.format(datetime.datetime.utcnow()))
	secl = str('{:%S}'.format(datetime.datetime.utcnow()))

	L = longitudine
	la = latitudine
	Legale = legale
	ar = aretta
	de = declinazione


	ora = "0"
	min = "0"
	sec = "0"
#	oral = (float(oral))
	ora = oral 
	min = minl
	sec = secl

#  CALCOLO DEL GIORNO GIULIANO -- inizio	
	mese = mese.zfill(2)
	giorno = giorno.zfill(2)

	dd = int(((float(ora)/24)+ (float(min)/(24*60)) + (float(sec)/(24*3600)))*100)
	DD = float(giorno) + float(dd)/100

	data = float(anno+"."+mese+giorno+str(dd))

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

	if ( data < 1582.1015 ):
		A = 0
		B = 0
	else:
		A = int(float(y)/100)
		B = 2 - A + int((A/4))

	JD = int(365.25*(y+4716)) + int(30.6001*(m+1)) + DD + B - 1524.5

#	CALCOLO DEL GIORNO GIULIANO -- fine


#	CALCOLO DEI SECOLI -- inizio
	T = (JD - 2415020.0)/36525
#	CALCOLO DEI SECOLI -- fine

	DT = float(0.41 + 1.2053 * T * 0.4992 * T * T)

#	CALCOLO DEI CALCOLO SIDERALE -- inizio	

	th0 = float(0.276919398 + 100.0021359 * T + 0.000001075 * T * T )
	####moltiplicazione della parte frazionaria per avere il tempo siderale medio in ore
	th0 = (th0-int(th0))*24

	err = (float(oral)+float(minl)/60+float(secl)/3600) * 1.002737908
	th0 = th0 + err

	#	CALCOLO DEI CALCOLO SIDERALE -- fine

	####### correzione nutazione  ######
	lms = float(279.6967 + 36000.7689 * T + 0.000303 * T * T)
	lms = ridgrd(lms)
	lml = float(270.4342 + 481267.8831 * T - 0.001133 * T * T)
	lml = ridgrd(lml)
	ams = float(358.4758 + 35999.0498 * T - 0.000150 * T * T - 0.0000033 * T * T * T)
	ams = ridgrd(ams)
	aml = float(296.1046 + 477198.8491 * T + 0.009192 * T * T)
	aml = ridgrd(aml)
	lnal = float(259.1833 -1934.1420 * T + 0.002078 * T * T) 
	lnal = ridgrd(lnal)
	e = float(0.01675104 - 0.0000418 * T - 0.000000126 * T * T)
	m = float(3.07234 + 0.00186 * T)
	n = float(20.0468 - 0.0085 * T)
	ns = float(n/15)
	epsi = float(23.452294 - 0.0130125 * T - 0.00000164 * T * T + 0.000000503 * T * T * T)
	e0 = float(e*180/np.pi)
	ae = np.arctan(np.sin(np.radians(ams))/(np.cos(np.radians(ams))-e))

	v = (2* np.arctan((np.sqrt((1+e)/(1-e))*np.tan(ae/2))))*180/np.pi

	lv = float(lms + v - ams)
	lv = 230.45

	dpsi = -17.20 * np.sin(np.radians(lnal)) - 1.32 * np.sin(np.radians(2*lms)) - 0.23 * np.sin(np.radians(2*lml))-0.21 * np.sin(np.radians(2*lnal))#
	depsi = float(9.2100+0.00091 * T) *np.cos(np.radians(lnal))+float(0.5522-0.00029 * T)* np.cos(np.radians(2*lms)) - 0.0904 * np.cos(np.radians(2*lnal)) +0.0884 * np.cos(np.radians(2*lml)) + 0.0216 * np.cos(np.radians(2*lml+ams))+0.0183* np.cos(np.radians(2*lml-lnal))+0.0113 * np.cos(np.radians(2*lml +aml))-0.0093 *np.cos(np.radians(2*lms-ams))-0.0066*np.cos(np.radians(2*lms-lnal))

	TSG = th0 - (int(th0/24)*24)

	cor = float((dpsi * np.cos(np.radians(epsi))/15))
	TSG = TSG + cor/3600

	da = float(m+ns*np.sin(np.radians(ar/15))*np.tan(np.radians(de)))
	dd = float(n*np.cos(np.radians(ar/15)))
	ar = ar + da/(3600)
	de = de + dd/(3600)

	da = float((np.cos(np.radians(epsi))+np.sin(np.radians(epsi))*np.sin(np.radians(ar))*np.tan(np.radians(de)))*dpsi - (np.cos(np.radians(ar))*np.tan(np.radians(de)))*depsi)
	dd = float((np.sin(np.radians(epsi))*np.cos(np.radians(ar)))*dpsi+(np.sin(np.radians(ar)*depsi)))
	da = float (da/(3600))
	dd = float (dd/3600)
	ar = ar + da
	de = de + dd

	da = -20.49 * (np.cos(np.radians(ar))*np.cos(np.radians(lv))*np.cos(np.radians(epsi))+np.sin(np.radians(ar))*np.sin(np.radians(lv)))/(np.cos(np.radians(de)))
	dd = -20.49 * (np.cos(np.radians(lv))*np.cos(np.radians(epsi))*(np.tan(np.radians(epsi))*np.cos(np.radians(de))-np.sin(np.radians(ar))*np.sin(np.radians(de)))+np.cos(np.radians(ar))*np.sin(np.radians(de))*np.sin(np.radians(lv)))
	da = float (da/(3600))
	dd = float (dd/3600)

	ar = float(ar + da)
	de = float(de + dd)

	TSL = TSG + (float(L)/float(15))
	
#	CALCOLO ANGOLO ORARIO -- inizio
	
	H =  TSL - ar

	#	CALCOLO ANGOLO ORARIO -- fine

	Azi = np.arctan((np.sin(np.radians(H*15)))/(np.cos(np.radians(H*15))*np.sin(np.radians(la))-np.tan(np.radians(de))*np.cos(np.radians(la))))
	den = np.cos(np.radians(H*15))*np.sin(np.radians(la))-np.tan(np.radians(de))*np.cos(np.radians(la))
	if den < 0:
		fattore = 180
	else:
		fattore = 0
		
	alt = np.arcsin(np.sin(np.radians(de))*np.sin(np.radians(la))+np.cos(np.radians(de))*np.cos(np.radians(la))*np.cos(np.radians(H*15)))

	Azimut = float(np.degrees(Azi))+180+fattore
	Altezza = float(np.degrees(alt))

	return Azimut,Altezza
