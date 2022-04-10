#coding:utf-8
import cv2
cap = cv2.VideoCapture(0)
flag = cap.isOpened()
 
index = 1
while(flag):
    ret, frame = cap.read()
    cv2.imshow("Captures",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord ('s'): #Presione la tecla s para ingresar a la siguiente operación de guardado de imágenes
        ruta = "C:/Users/Usuario/Documents/UDEA/Robotica/Proyecto/"+"foto"+str(index) + ".jpg"
        cv2.imwrite(ruta,frame)
       
        index += 1
    elif k == ord ('q'): #Presione la tecla q, el programa sale
            break
cap.release()
cv2.destroyAllWindows()