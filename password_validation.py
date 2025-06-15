from zxcvbn import zxcvbn
from rich.console import Console

console = Console()

#Função que checa se a senha informada é fraca, mediana ou forte.
def check_password(password):
    result = zxcvbn(password)
    score = result["score"]
    
    feedback = result["feedback"]

    if score <= 1:
        level = "[bold red]WEAK!!![bold red]"
    elif score == 2:
        level = "[yellow]Reasonable[/yellow]"
    elif score == 3:
        level = "[bold cyan]Good[/bold cyan]"
    else:  
        level = "[bold green]Strong[/bold green]"

    console.print(level)

    if feedback["warning"]:
        console.print("[bold orange3]Warning:[/bold orange3]",feedback["warning"])
    if feedback["suggestions"]:
        console.print(feedback ["suggestions"])
