import os 
from datetime import datetime
from rich.console import Console
import re

console = Console()


def is_valid_name(name: str ) -> bool:
    if ".." in name or "/" in name or "\\" in name:
        return False

    pattern = r"^[\w\-.]+$"
    return bool(re.match(pattern, name))


def save_in_txt(password):

    if not os.path.exists("saves"):
        os.makedirs("saves")

    name = input("Enter a name to save your file: ").strip()
    if not name.endswith(".txt"):
        name +=".txt"

    if not is_valid_name(name):
        console.print("[bold red]Invalid filename[/bold red]")
        return
    
    base_name, ext = os.path.splitext(name)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'{base_name}_{timestamp}{ext}'
    path = os.path.join("saves", filename)

    with open (path, 'w') as arq:
        arq.write(f"Password: {password}\n")

    console.print(f"[bold green]Password saved successfully in {path}[/bold green]")

    





    
