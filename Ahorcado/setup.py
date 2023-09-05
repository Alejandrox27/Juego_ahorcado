import sys
from cx_Freeze import setup, Executable
import os
from PIL import Image
icon_path = os.path.abspath("../Ahorcado/Juego/images/icon.png")
imagen_original = Image.open(icon_path)

nuevo_tamano = (512, 512)
imagen_redimensionada = imagen_original.resize(nuevo_tamano, Image.LANCZOS)
imagen_redimensionada.save("Juego/images/imagen_redimensionada.ico")

imagen_original.close()
imagen_redimensionada.close()
icon_path = os.path.abspath("../Ahorcado/Juego/images/imagen_redimensionada.ico")


base = None
if sys.platform == "win32":
    base = "Win32GUI"  

options = {
    "build_exe": {
        "packages": ["os", "sys", "PyQt6"],
        "include_files": ["Juego/images/", "Juego/styles/"] 
    }
}

executables = [
    Executable("Juego/__main__.py", base=base, icon=icon_path, target_name="Ahorcado")
]

setup(
    name="Ahorcado",
    version="1.0",
    description="Juego de ahorcado",
    options=options,
    executables=executables
)
#python setup.py build
