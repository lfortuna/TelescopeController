#!/usr/bin/python

from astroapi import posizione

##### Ascenzione Retta, Declinazione, Longitudine, Latitudine, Ora legale  --> risultato Azimut e Altezza dall'orizzonte
print ("Arturo= " + str(posizione(14.261,19.172,12.452,41.922,1)))
print ("Spiga= " + str(posizione(13.420,-11.161,12.452,41.922,1)))
print ("Procione= " + str(posizione(7.670,5.178,12.452,41.922,1)))
