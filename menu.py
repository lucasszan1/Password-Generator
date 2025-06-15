from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from password_generate import GeneratedPasword
from password_validation import check_password
from utilities import save_in_txt

generate_password= GeneratedPasword()
generated_password = generate_password.generate

console = Console()
class MainMenu():
    def main_menu():
        while True:
            console.print(Panel.fit('[bold magenta]PASSWORD GENERATOR[/bold magenta]', border_style="White"))
            console.print("[bold magenta][ 1 ][/bold magenta] Generate Password")
            console.print("[bold magenta][ 2 ][/bold magenta] Test Your Password")
            console.print("[bold magenta][ 0 ][/bold magenta] Exit ")
            choice = Prompt.ask("[bold magenta]>>>[/bold magenta]")
            return choice
        
#Função que inicia o teste da senha que o usuario mandar para a verificação.
    def start_test():
        unchecked_password = Prompt.ask("[bold magenta][ + ]Your password to test[/bold magenta]")
        check_password(unchecked_password)

#Inicia o gerador de senhas.
    def start_generator():
        size_str = Prompt.ask("[bold magenta][ + ][/bold magenta]Size of you password")
        size = int(size_str)

#Pergunta para o usuario o que ele vai querer na sua senha.
        use_symbols = Prompt.ask("[bold magenta][ + ][/bold magenta]Use symbols in your password ?",choices=["y", "n"]) == "y"
        use_numbers = Prompt.ask("[bold magenta][ + ][/bold magenta]Use numbers in your password ?",choices=["y", "n"]) == "y"
        use_upper = Prompt.ask("[bold magenta][ + ][/bold magenta]Use uppers in your password ?",choices=["y", "n"]) == "y"
        use_lowers = Prompt.ask("[bold magenta][ + ][/bold magenta]Use lowers in your password ?",choices=["y", "n"]) == "y"

#Recebe os valores que o usuario passou e gera a senha.
        get_password = generated_password(size, use_symbols, use_numbers, use_upper, use_lowers)
        if get_password:
            print()
            console.print(f"[bold green]{get_password}[bold green]")
            if Prompt.ask("Do you wana save the password ?", choices=["y", "n"]) == "y":
                save_in_txt(get_password)
            print()
        else:
            console.print("[bold red]Erro[/bold red]")

        
