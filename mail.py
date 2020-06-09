from funciones import *

import time

print("El programa empezará en 5 segundos")
time.sleep(5)

while(True):    
    click_en_imagen('draft.png', 1)
    time.sleep(0.1)
    click_en_imagen('draft.png', 2)
    time.sleep(2)
    click_en_imagen('enviar.png', 1)

    time.sleep(5)





