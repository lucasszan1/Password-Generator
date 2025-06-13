from menu import MainMenu
from rich.console import Console

console = Console()

def main():
 
    menu = MainMenu

    while True:
        opcao = menu.main_menu()
        if opcao == "0":
            console.print("[bold red] Quit [/bold red]")
            break
        elif opcao == "1":
            menu.start_generator()
        elif opcao == "2":
            menu.start_test()
            continue

if __name__ == "__main__":
    main()