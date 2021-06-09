import cv2
import os
import numpy as np

direccion  = 'C:\Users\gerar\Pictures\Cubrebocas\fotos'
lista = os.listdir(direccion)

etiquetas = []
rostros = []
con = 0

for nameDir in lista:
    nombre = direccion + '/' + nameDir

    for fileName in os.listdir(nombre)
    etiquetas.append(con)
    rostros.append(cv2.imred(nombre + '/' + dileName,0))

    con = con + 1

reconocimiento = cv2.face.LBPHFaceRecognizet_create()
reconocimiento.train(rostros, np.array(etiquetas))

reconocimiento.write('modeloLBP.xml')
