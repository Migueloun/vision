# Visión RPA papá

Click en "me gusta" de facebook automático.

## Instalación

Instalar pip

Módulos a instalar en Windows
    opencv-python (Para visión)
    mss (Para tomar capturas de pantalla)
    win32api, win32con (Para simular clics de ratón en la pantalla)

## Opencv

```bash
python -m pip install opencv-python
```

Es necesario asegurar que se tiene instalada la versión 3 de python
    Si por algún motivo opencv se instaló en python2, utilizar:

```bash
python3 -m pip install opencv-python
```

## mss

```bash
python -m pip install mss
```

## Instalar win32api, win32con

Probablemente sólo se tengan que importar los módulos y no se tiene que correr nada
Si no funciona, intentar

utilizando pip

```bash
python -m pip install pywin32
```

ó descargar el codigo fuente
        Navegar a https://github.com/mhammond/pywin32 y descargar la carpeta .zip del código y descomprimirla
        Abrir la carpeta y localizar el archivo setup.py
        En consola correr:

```bash
python setup.py install
```
