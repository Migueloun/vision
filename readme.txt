Módulos a instalar en Windows
    opencv-python (Para visión)
    mss (Para tomar capturas de pantalla)
    win32api, win32con (Para simular clics de ratón en la pantalla)

Instalar opencv en linea de comandos correr
    python -m pip install opencv-python 

    Es necesario asegurar que se tiene instalada la versión 3 de python 
    Si por algún motivo opencv se instaló en python2, utilizar python3 -m pip install opencv-python 

Instalar mss
    python -m pip install mss

Instalar win32api, win32con
    Probablemente sólo se tengan que importar los módulos y no se tiene que correr nada
    Si no funciona, intentar
    1) utilizando pip
        python -m pip install pywin32

    2) descargar el codigo fuente
        Navegar a https://github.com/mhammond/pywin32 y descargar la carpeta .zip del código y descomprimirla
        Abrir la carpeta y localizar el archivo setup.py
        En consola correr: python setup.py install
