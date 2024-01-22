import os

# caminho = r"C:\Users\dedlo\Documents\GitHub\moveFiles"
lista_arquivos = os.listdir("Mover")

for arquivo in lista_arquivos:
    if ".xlsx" in arquivo:
        if "Jan" in arquivo:
            # jogar pra pasta Jan
            os.rename(f"Mover/{arquivo}", f"Mover/Jan/{arquivo}")
        if "Fev" in arquivo:
            # jogar pra pasta Fev
            os.rename(f"Mover/{arquivo}", f"Mover/Fev/{arquivo}")
        if "Mar" in arquivo:
            # jogar pra pasta Mar
            os.rename(f"Mover/{arquivo}", f"Mover/Mar/{arquivo}")
