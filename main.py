from menu import MainMenu
from rich.console import Console

console = Console()

#Função principal que executa todo o projeto.
def main():

    menu = MainMenu

    while True:
        user_option = menu.main_menu()
        if user_option == "0":
            console.print("[bold red] Quit [/bold red]")
            break
        elif user_option == "1":
            menu.start_generator()
        elif user_option == "2":
            menu.start_test()
            continue

if __name__ == "__main__":
    main()