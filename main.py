from Calibracion import *
from posicion import *


ret, mtx, dist, rvecs, tvecs = calibrate('C:/Users/Usuario/Documents/UDEA/Robotica/Proyecto', 'foto', 'jpg', 0.015, 9, 6)
save_coefficients(mtx, dist,'data.YML')
print("Calibration is finished. RMS: ", ret,mtx, dist,rvecs, tvecs)


patron = np.array([[0, 12.5,0], # Punto 1: X = 0, Y = 10
                   [12.5, 15.6,0], # Punto 2: X = 5, Y = 10 
                   [0,  0,0], # Punto 3: X = 0, Y = 0 (Origen de coordenadas)
                   [15.6,  0,0]],dtype=np.float64)# Ultimo punto

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    img = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)
    centro_rojo = getCentroRojo(frame,img)
    
    centro_verde = getCentroVerde(frame,img)
    
    centro_azul = getCentroAzul(frame,img)
    
    centro_amarillo = getCentroAmarillo(frame,img)


    centro_rojox = centro_rojo[0]
    centro_rojoy = centro_rojo[1]

    camera_mtx = np.array(mtx).reshape((3, 3))
    

    centros_ordenados = [ centro_azul , centro_verde, centro_rojo, centro_amarillo ] 
    
    #print("CENTROS ORDENADOS",centros_ordenados)
    
    flag = cv2.SOLVEPNP_ITERATIVE # tried with SOLVEPNP_EPNP, same error.
    
    rets, rvec, tvec = cv2.solvePnP(patron, np.array(centros_ordenados), camera_mtx,dist,flags=flag) 
    
    posXYZ = CalcularXYZ(centro_rojox,centro_rojoy,mtx,rvec,tvec)

    print("POSICION XYZ",posXYZ)

    cv2.imshow('frame', frame)

    

    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()