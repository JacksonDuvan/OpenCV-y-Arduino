#Codigo de interaccion entre Arduino y OpenCV
#Por Glar3
 
import cv2
import numpy as np
import serial #cargamos la libreria serial
 
#Iniciamos la camara
captura = cv2.VideoCapture(0)
 
#Iniciamos la comunicacion serial
ser = serial.Serial('COM3', 9600)
 
while(1):
 
   #Capturamos una imagen y la convertimos de RGB -> HSV
   _, imagen = captura.read()
   hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
   #Establecemos el rango de colores que vamos a detectar
   #En este caso de verde oscuro a verde-azulado claro
   #verde
   verde_bajos = np.array([49,50,50], dtype=np.uint8)
   verde_altos = np.array([80, 255, 255], dtype=np.uint8)
   #azul
   azul_bajos = np.array([100,65,75], dtype=np.uint8)
   azul_altos = np.array([130, 255, 255], dtype=np.uint8)
   #amarillo
   amarillo_bajos = np.array([16,76,72], dtype=np.uint8)
   amarillo_altos = np.array([30, 255, 210], dtype=np.uint8)
   #Crear una mascara con solo los pixeles dentro del rango de verdes
   mask = cv2.inRange(hsv, verde_bajos, verde_altos)
   mask1 = cv2.inRange(hsv, azul_bajos, azul_altos)
   mask2 = cv2.inRange(hsv, amarillo_bajos, amarillo_altos )
   #Encontrar el area de los objetos que detecta la camara
   moments = cv2.moments(mask)
   area = moments['m00']
   
   moments1 = cv2.moments(mask1)
   area1 = moments1['m00']

   moments2 = cv2.moments(mask2)
   area2 = moments2['m00']

   #Descomentar para ver el area por pantalla
   #print area
 
   #Si el objeto tiene un area determinada, escribimos 'h'
   #Si no, escribimos un caracter erroneos
   #verde
   if(area > 2000000):
      ser.write('h')
 
   
   #azul
   if(area1 > 2000000):
      ser.write('a')
   

   #amarillo
   if(area2 > 2000000): 
      ser.write('b')
   
   else:
      ser.write('n')

   #Mostramos la imagen original y
   #la mascara
   cv2.imshow('mask', mask)
   cv2.imshow('Camara', imagen)
   tecla = cv2.waitKey(5) & 0xFF
   if tecla == 27:
      break
 
cv2.destroyAllWindows()