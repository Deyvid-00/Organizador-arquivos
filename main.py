import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
print(caminho)

lista_arquivos = os.listdir(caminho)

locais = {
    "IMAGENS": [".png", ".jpg", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".raw", ";eps", "psd", "ico", ".xcf"],
    "PLANILHAS": ["xlsx", ";xls", ".csv", ".ods",],
    "DOCUMENTO": [".pdf", ".doc", ".dot", ".docx", ".dotx", ".docm"],
    "csv": [".csv"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")