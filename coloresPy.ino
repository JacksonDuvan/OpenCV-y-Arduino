/*
Interaccion entre Arduino y OpenCV
Codigo para Arduino
 
*/

#include <Servo.h>

Servo servo;
char lectura; //Variable para guardar la lectura del Serial
 
void setup()
{
   //Iniciamos el Serial:
   Serial.begin(9600);
 
   //Inicializamos el pin 13
   servo.attach(3);
   pinMode(13,OUTPUT);
}
 
void loop()
{
   //Si recibimos algo por serial, lo guardamos
   if(Serial.available() >= 1)
   {
      lectura = Serial.read();
 
      //-Si recibiste 'h' -> enciende LED
      //-Si recibiste otro caracter -> apaga el LED
      //verde
      if(lectura == 'h')
      {
         servo.write(180);
         digitalWrite(13,HIGH);
      }
      
      //azul
      if(lectura == 'a')
      {
        servo.write(110);
        digitalWrite(13,HIGH);
        }
       //rojo 
       if(lectura == 'b')
      {
        servo.write(30);
        digitalWrite(13,HIGH);
        }
        
   }
}
