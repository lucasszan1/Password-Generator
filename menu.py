from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from passwords import GeneratedPasword
from passwordtest import check_password
from utilities import save_in_txt

Gpw= GeneratedPasword()
Gpassword = Gpw.generate

console = Console()

class MainMenu():
    def main_menu():
        while True:
            console.print(Panel.fit('[bold magenta]PASSWORD GENERATOR[/bold magenta]', border_style="White"))
            console.print("[bold magenta][ 1 ][/bold magenta] Generate Password")
            console.print("[bold magenta][ 2 ][/bold magenta] Test Your password")
            console.print("[bold magenta][ 0 ][/bold magenta] Exit ")

            choice = Prompt.ask("[bold magenta]>>>[/bold magenta]")
            return choice
        
    def start_test():
        unchecked_password = Prompt.ask("[bold magenta][ + ]Your password to test[/bold magenta]")
        check_password(unchecked_password)


    def start_generator():
        size_str = Prompt.ask("[bold magenta][ + ][/bold magenta]Size of you password")
        size = int(size_str)
        use_symbols = Prompt.ask("[bold magenta][ + ][/bold magenta]Use symbols in your password ?",choices=["y", "n"]) == "y"
        use_numbers = Prompt.ask("[bold magenta][ + ][/bold magenta]Use number in your password ?",choices=["y", "n"]) == "y"
        use_upper = Prompt.ask("[bold magenta][ + ][/bold magenta]Use uppers in your password ?",choices=["y", "n"]) == "y"
        use_lowers = Prompt.ask("[bold magenta][ + ][/bold magenta]Use lowers in your password ?",choices=["y", "n"]) == "y"

        get_password = Gpassword(size, use_symbols, use_numbers, use_upper, use_lowers)
        if get_password:
            print()
            console.print(f"[bold green]{get_password}[bold green]")
            if Prompt.ask("Do you wana save the password ?", choices=["y", "n"]) == "y":
                save_in_txt(get_password)
            print()
        else:
            console.print("[bold red]Erro[/bold red]")

        
