/*
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                 Created 22 March 2014                                   *
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



const int buttonAlign = 53;    // pin in cui l'interruttore abilita l'allineamento con una stella
int buttonState = 0;
int arHH = 6;                  // AR ore
int arMM = 11;                 // AR minuti
int arSS = 40;                 // AR secondi
char decSIGN = 43;             // segno della DEC: 43 = +    45 = -
int decDEG = 9;                // DEC gradi
int decMM = 45;                // DEC minuti
int decSS = 5;                 // DEC secondi
int rxarHH;                    // AR ore del target
int rxarMM;                    // AR minuti del target
int rxarSS;                    // AR secondi del target
char rxdecSIGN;                // segno della DEC del target
int rxdecDEG;                  // DEC gradi del target
int rxdecMM;                   // DEC minuti di grado del target
int rxdecSS;                   // DEC secondi di grado del target
String inputString = "";       //dichiaro una stringa vuota per memorizzare i dati in entrata


void setup() {
  pinMode(buttonAlign, INPUT);
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
    
    
     /* questa parte del programma serve per ricevere le coordinate di una una stella presa come riferimento premendo su stellarium i tasti ctrl-1
        ATTENZIONE: questa funzione serve in realtà per il GOTO, però con um accorgimento la sfruttiamo per impostare le coordinate del telescopio
        durannte la messa in stazione */
   
    // ricezione della coordiata di AR
    
    if (inputString.substring(0,4) == "#:Q#"){            // con il comando #:Q# stellarium chiede l'arresto dei motori
      // inviare l'arresto ai motori
    }
      
       
    if (inputString.substring(4,7) == ":Sr"){
      rxarHH = inputString.substring(8,10).toInt();       // preleva solo HH dalla stringa (il comando .toInt() converte il valore in un intero)
      rxarMM = inputString.substring(11,13).toInt();      // preleva solo MM dalla stringa (il comando .toInt() converte il valore in un intero)
      rxarSS = inputString.substring(14,16).toInt();      // preleva solo SS dalla stringa (il comando .toInt() converte il valore in un intero)
      inputString = "";                                   // cancella la stringa
      Serial.print ("1");                                 // invia "1" per avvisare stellarium di aver ricevuto le coordiate 
     }
    
    // ricezione della coordiata di DEC

    if (inputString.substring(0,3) == ":Sd"){
      (inputString.substring(4,5)=="+") ? rxdecSIGN = 43 : rxdecSIGN = 45;    //if else in versione contratta: (espressione) ? se vero : se falso
      rxdecDEG = inputString.substring(5,7).toInt();                          // preleva solo i gradi dalla stringa (il comando .toInt() converte il valore in un intero)
      rxdecMM = inputString.substring(8,10).toInt();                          // preleva solo minuti dalla stringa (il comando .toInt() converte il valore in un intero)
      rxdecSS = inputString.substring(11,13).toInt();                         // preleva solo secondi dalla stringa (il comando .toInt() converte il valore in un intero)
      inputString = "";                                                       // cancella la stringa
      Serial.print ("1");                                                     // invia "1" per avvisare stellarium di aver ricevuto le coordiate 
    }
   
      
    if (inputString == ":MS#"){
       Serial.print ("O");
       buttonState = digitalRead(buttonAlign);             // legge se l'interruttore per l'allineamento iniziale è su ON o OFF
       if (buttonState == HIGH) {                          // se ON aggiorna le coordinate, altrimenti proseguià con il GOTO (non ancora presente in questo Sketch)
       decSIGN = rxdecSIGN;
       arHH = rxarHH;                                      // aggiorna le variabili
       arMM = rxarMM;                                      // aggiorna le variabili
       arSS = rxarSS;                                      // aggiorna le variabili
       decDEG = rxdecDEG;                                  // aggiorna le variabili
       decMM = rxdecMM;                                    // aggiorna le variabili
       decSS = rxdecSS;                                    // aggiorna le variabili
       }
       inputString = "";                                   // cancella la stringa

     }
   }
