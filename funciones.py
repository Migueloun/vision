import cv2 #Detección de imagenes
from mss import mss #Para tomar capturas de pantalla con codigo
import win32api, win32con #Para dar click en con el ratón con windows

#https://stackoverflow.com/questions/2846947/get-screenshot-on-windows-with-python
def tomar_captura_de_pantalla():
    with mss() as sct:
        return sct.shot()

#https://stackoverflow.com/questions/7853628/how-do-i-find-an-image-contained-within-an-image
def encontrar_coordenadas_en_pantalla(imagen_a_encontrar):    
    small_image = cv2.imread(imagen_a_encontrar) #imagen a buscar
    screenshot = cv2.imread(tomar_captura_de_pantalla()) #Screenshot de la pantalla

    # Utilizar funcion matchTemplate de opencv
    method = cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(small_image, screenshot, method)

    # Extraer la diferencia minima cuadrada
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Dibujar un rectangulo:
    # Extraer las coordenadas del match
    MPx,MPy = mnLoc

    # Paso 2: Obtener las dimesniones de la imagen a buscar.
    trows,tcols = small_image.shape[:2]

    # Paso 3: Dibujar rectangulo en el screenshot
    cv2.rectangle(screenshot, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    # Paso 4: Calcular coordenada para hacer clic
    coordenadas = (MPx+(tcols/2),MPy+(trows/2))
    print(coordenadas)

    # Mostrar screenshot con rectangulo y salvar una nueva imagen.
    #resized_screenshot = cv2.resize(screenshot,(800,600))
    #cv2.imshow('output', resized_screenshot)
    #cv2.waitKey(0)
    #cv2.imwrite('result.png',screenshot)
    return coordenadas

#https://stackoverflow.com/questions/1181464/controlling-mouse-with-python
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def click_en_imagen(imagen, repeticiones):
    coordenadas = encontrar_coordenadas_en_pantalla(imagen)

    while (repeticiones > 0):
        click(int(coordenadas[0]), int(coordenadas[1]))
        repeticiones = repeticiones - 1
    

    
