/*
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                 Created 19 March 2014                                   *
*                                       by EDC                                            *
*                           http://epsilonphoto.weebly.com/                               *
*                                                                                         *
*      This program is free software, you can redistribute it and/or modify.              *
*      Is in the public domain, it only has a didactic purpose and you can modify it      *
*      to your liking. I do not provide any guarantee for any damage it may cause         *
*      to property or persons.                                                            *
*                                                                                         *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*/



int arHH = 6;                  // AR ore
int arMM = 11;                 // AR minuti
int arSS = 40;                 // AR secondi
char decSIGN = 43;             // 43 = +    45 = -
int decDEG = 9;                // DEC gradi
int decMM = 45;                // DEC minuti
int decSS = 5;                 // DEC secondi
String inputString = "";       //dichiaro una stringa vuota per memorizzare i dati in entrata


void setup() {
  Serial.begin(9600);
}

void loop() {
     while (Serial.available()>0){         // ottiene byte in entrata
      char inChar = Serial.read();         // legge il byte e lo memorizza nella variabile inChar
      inputString += String(inChar);       // aggiunge il byte corrente a inputString
      delay(5);
    }
    if (inputString == "#:GR#"){           // se il comando ricevuto da stellarium è #:GR# (coordinata di AR)
      if (arHH < 10){                      // se ARHH < 10 invia uno zero perché LX200 vuole il formato HH:MM:SS
        Serial.print ("0");
      }
      Serial.print (arHH);                 // invia a stellarium il valore delle ore della coordinata AR
      Serial.print (":");
      if (arMM < 10){                      // se ARMM < 10 invia uno zero perché LX200 vuole il formato HH:MM:SS
        Serial.print ("0");
      }
      Serial.print (arMM);                 // invia a stellarium il valore dei minuti della coordinata AR
      Serial.print (":");
      if (arSS < 10){                      // se ARSS < 10 invia uno zero perché LX200 vuole il formato HH:MM:SS
        Serial.print ("0");
      }
      Serial.print (arSS);                 // invia a stellarium il valore dei secondi della coordinata AR
      Serial.print ("#");
      inputString = "";                    // cancella la stringa
    }
    if (inputString == "#:GD#"){           // se il comando ricevuto da stellarium è #:GD# (coordinata di DEC)   
      Serial.print ((char)decSIGN);        // invia a stellarium il segno della coordinata DEC
      if (decDEG < 10){                    // se DECDEG < 10 invia uno zero perché LX200 vuole il formato + - DEG:MM:SS
        Serial.print ("0");
      }
      Serial.print (decDEG);               // invia a stellarium il valore dei gradi della coordinata DEC
      Serial.print ((char)223);            // char(223) si usa al posto di * per indicare il grado ° altrimenti ci sarà un errore nel file di log.
      if (decMM < 10){                     // se DECMM < 10 invia uno zero perché LX200 vuole il formato + - DEG:MM:SS
        Serial.print ("0");
      }
      Serial.print (decMM);                // invia a stellarium il valore dei minuti di grado della coordinata DEC
      Serial.print (":");
      if (decSS < 10){                     // se DECSS < 10 invia uno zero perché LX200 vuole il formato + - DEG:MM:SS
        Serial.print ("0");
      }
      Serial.print (decSS);                // invia a stellarium il valore dei secondi di grado della coordinata DEC
      Serial.print ("#");
      inputString = "";                    // cancella la stringa
    }
   }
