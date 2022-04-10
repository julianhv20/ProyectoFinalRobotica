from asyncio.windows_events import NULL
import cv2
import numpy as np

color = (255,0,0)

# La entrada es el frame en formato HSV
def getCentroRojo(frame,frame_hsv):
    #Definimos los limites HSV para elegir el rojo
    #limites_rojo = ((162,153,61),(193,255,178))
    limites_rojo = ((0,46,0),(11,255,255))

    #Generamos la mascara y obtenemos los contornos
    mask_rojo = cv2.inRange(frame_hsv, limites_rojo[0], limites_rojo[1])
    cnts, _ = cv2.findContours(mask_rojo, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cnts = imutils.grab_contours(cnts)
    

    x = 0
    y = 0
    
    # Si tenemos algún contorno
    if len(cnts) > 0:
       # Buscamos el que tenga más área
       c = max(cnts, key=cv2.contourArea)
       cv2.drawContours(frame, [c], 0, color, 3)

       #Cogemos el círculo que más se aproxime. x,y serán las coordenadas de nuestra detección.
       ((x, y), radius) = cv2.minEnclosingCircle(c)
      
    return (x,y)

def getCentroVerde(frame,frame_hsv):
    #Definimos los limites HSV para elegir el rojo
    limites_rojo = ((39,38,67),(91,255,180))

    #Generamos la mascara y obtenemos los contornos
    mask_rojo = cv2.inRange(frame_hsv, limites_rojo[0], limites_rojo[1])
    cnts, _ = cv2.findContours(mask_rojo, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cnts = imutils.grab_contours(cnts)

    x = 0
    y = 0
    
    # Si tenemos algún contorno
    if len(cnts) > 0:
       # Buscamos el que tenga más área
       c = max(cnts, key=cv2.contourArea)
       cv2.drawContours(frame, [c], 0, color, 3)

       #Cogemos el círculo que más se aproxime. x,y serán las coordenadas de nuestra detección.
       ((x, y), radius) = cv2.minEnclosingCircle(c)
      
    return (x,y)

def getCentroAzul(frame,frame_hsv):
    #Definimos los limites HSV para elegir el rojo
    #limites_rojo = ((100,100,20),(125,255,255))
    limites_rojo = ((94,94,36),(141,255,165))

    #Generamos la mascara y obtenemos los contornos
    mask_rojo = cv2.inRange(frame_hsv, limites_rojo[0], limites_rojo[1])
    cnts, _ = cv2.findContours(mask_rojo, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cnts = imutils.grab_contours(cnts)
    x = 0
    y = 0
    # Si tenemos algún contorno
    if len(cnts) > 0:
       # Buscamos el que tenga más área
       c = max(cnts, key=cv2.contourArea)
       cv2.drawContours(frame, [c], 0, color, 3)

       #Cogemos el círculo que más se aproxime. x,y serán las coordenadas de nuestra detección.
       ((x, y), radius) = cv2.minEnclosingCircle(c)
    
      
    return (x,y)

def getCentroAmarillo(frame,frame_hsv):
    #Definimos los limites HSV para elegir el rojo
    #limites_rojo = ((15,100,20),(45,255,255))
    limites_rojo = ((21,100,0),(40,255,255))

    #Generamos la mascara y obtenemos los contornos
    mask_rojo = cv2.inRange(frame_hsv, limites_rojo[0], limites_rojo[1])
    cnts, _ = cv2.findContours(mask_rojo, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cnts = imutils.grab_contours(cnts)

    x = 0
    y = 0
    
    # Si tenemos algún contorno
    if len(cnts) > 0:
       # Buscamos el que tenga más área
       c = max(cnts, key=cv2.contourArea)
       cv2.drawContours(frame, [c], 0, color, 3)

       #Cogemos el círculo que más se aproxime. x,y serán las coordenadas de nuestra detección.
       ((x, y), radius) = cv2.minEnclosingCircle(c)
      
    return (x,y)





def CalcularXYZ(u,v, A, rvec, tvec):
    # Generamos el vector m
    uv = np.array([[u,v,1]], dtype=np.float).T

    # Obtenemos R a partir de rvec
    R, _ = cv2.Rodrigues(rvec)
    Inv_R = np.linalg.inv(R)
    
    # Parte izquierda m*A^(-1)*R^(-1)
    Izda = Inv_R.dot(np.linalg.inv(A).dot(uv))

    # Parte derecha
    Drch = Inv_R.dot(tvec)

    # Calculamos S porque sabemos Z = 0
    s = 0 + Drch[2][0]/Izda[2][0]
    
    XYZ = Inv_R.dot( s * np.linalg.inv(A).dot(uv) - tvec)
   
    return XYZ





