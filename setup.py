import sys
from cx_Freeze import setup, Executable

# Aumentar a profundidade máxima de recursão
sys.setrecursionlimit(5000)

# Include additional packages here
build_exe_options = {
    "packages": ["os", "sys", "PIL", "PyQt5", "pytesseract", "clipboard"],
    "include_files": [],  # Include any additional files if necessary
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use "Win32GUI" to suppress the console window

setup(
    name="printOCR",
    version="1.0",
    description="Ferramenta de Captura de Tela com OCR",
    options={"build_exe": build_exe_options},
    executables=[Executable("printOCR.py", base=base)],
)
