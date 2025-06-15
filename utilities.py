import os 
from datetime import datetime
from rich.console import Console
import re

console = Console()

#Essa função valida se o usuario vai passar caracteres validos.

def is_valid_name(name: str ) -> bool:
    if ".." in name or "/" in name or "\\" in name:
        return False

#Passa somente os caracteres validos.
    pattern = r"^[\w\-.]+$"
    return bool(re.match(pattern, name))

#Função que salva a senha em um .txt.
def save_in_txt(password):

# Caso não exista a pasta, ela será criada com o nome "saves".
    if not os.path.exists("saves"):
        os.makedirs("saves")

#Input para o usuario decidir qual o nome do arquivo que ele deseja salvar.
    name = input("Enter a name to save your file: ").strip()

#Faz com que o arquivo termine com .txt.
    if not name.endswith(".txt"):
        name +=".txt"

#Se o nome não passar na validação, exibira no terminal Invalid filename.
    if not is_valid_name(name):
        console.print("[bold red]Invalid filename[/bold red]")
        return
    
#Divide o nome para poder adicionar o .txt ao final do arquivo.
    base_name, ext = os.path.splitext(name)

#Adiciona o timestamp de quando o arquivo foi criado.
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#F string para juntar todo o arquivo.
    filename = f'{base_name}_{timestamp}{ext}'
    path = os.path.join("saves", filename)
    with open (path, 'w') as arq:
        arq.write(f"Password: {password}\n")

    console.print(f"[bold green]Password saved successfully in {path}[/bold green]")

    





    
