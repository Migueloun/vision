from funciones import *
import win32api, win32con
import time

print("El programa empezará en 5 segundos")
time.sleep(5)

coordenadas = encontrar_coordenadas_en_pantalla('me_gusta.png')
print(coordenadas)
print(coordenadas[0])

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


click(int(coordenadas[0]), int(coordenadas[1]))



