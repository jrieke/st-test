import streamlit as st
from rich.console import Console

console = Console(force_terminal=True)

# try:
#     a = {}
#     a["key"]
# except KeyError as e:
#     console.print_exception()
#     #console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

console.print("[yellow][09:26:03][/yellow] 🚥 Connecting...")
console.print(
    """
    
[red][09:26:03][/red] 🚥 Connecting...
[red][09:26:04][/red] 🚀 Starting up...
              - owner:        [cyan]streamlit[/cyan]
              - repository:   [cyan]app-frontpage[/cyan]
              - branch:       [cyan]main[/cyan]
              - main module:  [cyan]streamlit_app.py[/cyan]
[red][09:26:09][/red] 🐙 Cloning repository...
[red][09:26:10][/red]    Cloning into [white]'app-frontpage'[/white]...
[red][09:26:55][/red]    Cloned repository!                    
[red][09:27:00][/red] 📦 Processing dependencies...
              - tool:  [cyan]pipenv[/cyan]
              - file:  [cyan]/app/app-frontpage/Pipfile[/cyan]
    """
)
st.write("Hello")