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



String inputString = "";                   //dichiaro una stringa vuota per memorizzare i dati in entrata


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
      Serial.print ("00");                 // invia a stellarium il valore della coordinata AR: 00h
      Serial.print (":");
      Serial.print ("00");                 // invia a stellarium il valore della coordinata AR: 00m
      Serial.print (":");
      Serial.print ("00");                 // invia a stellarium il valore della coordinata AR: 00s
      Serial.print ("#");
      inputString = "";                    // cancella la stringa
    }
    if (inputString == "#:GD#"){           // se il comando ricevuto da stellarium è #:GD# (coordinata di DEC)   
      Serial.print ("+");                  // invia a stellarium il segno della coordinata DEC
      Serial.print ("45");                 // invia a stellarium il valore della coordinata DEC: 45°
      Serial.print ((char)223);            // char(223) si usa al posto di * per indicare il grado ° altrimenti ci sarà un errore nel file di log.
      Serial.print ("00");                 // invia a stellarium il valore della coordinata DEC: 00'
      Serial.print (":");
      Serial.print ("00");                 // invia a stellarium il valore della coordinata DEC: 00''
      Serial.print ("#");
      inputString = "";                    // cancella la stringa
    }
   }
