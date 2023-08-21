import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6"],
}


includes = []
include_files = [
    r'C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\Classificacao_e_Pesquisa_de_Dados\TrabFinal\dados\rating.csv',
    r'C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\Classificacao_e_Pesquisa_de_Dados\TrabFinal\dados\players.csv',
    r'C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\Classificacao_e_Pesquisa_de_Dados\TrabFinal\dados\tags.csv',
    r'C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\Classificacao_e_Pesquisa_de_Dados\TrabFinal\pesquisas\playersExtras.csv',
    r"C:\Users\biaso\anaconda3\DLLs\_tkinter.pyd"]
packages=[]

setup(
    name="ConsultaJogadores",
    version="0.1",
    description="Consulta a jogadores de futebol",
    options={"build_exe": {'includes':includes, 'include_files':include_files, 'packages':packages}},
    executables=[Executable("main.py", base=None)],
)