# pip install rich requests

import sys
import json
import time
import requests
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.live import Live
from rich.spinner import Spinner
from rich.table import Table

console = Console()

API_URL = "https://roommate.theushen.me"

CONFIG_DIR = Path(__file__).parent.parent / "config"
PASSWORD_FILE = CONFIG_DIR / "api_password.txt"
headers = {"Content-Type": "application/json"}

if PASSWORD_FILE.exists():
    password = PASSWORD_FILE.read_text().strip()
    headers["Authorization"] = f"Bearer {password}"
    console.print("[dim]Local server detected — unlimited access[/]")
else:
    console.print("[dim]Connected to public server — test mode (3 messages)[/]")

BANNER = """
[bold magenta]╔══════════════════════════════════════════════════╗
║                                                  ║
║    [bold cyan]██████╗  █████╗  ██████╗ ███╗   ███╗[/]    ║
║    [bold cyan]██╔══██╗██╔══██╗██╔═══██╗████╗ ████║[/]    ║
║    [bold cyan]██████╔╝██║  ██║██║   ██║██╔████╔██║[/]    ║
║    [bold cyan]██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║[/]    ║
║    [bold cyan]██║  ██║╚█████╔╝╚██████╔╝██║ ╚═╝ ██║[/]    ║
║    [bold cyan]╚═╝  ╚═╝ ╚════╝  ╚═════╝ ╚═╝     ╚═╝[/]    ║
║                                                  ║
║        [bold white]Your Personal AI Roommate[/]               ║
╚══════════════════════════════════════════════════╝[/]
""".strip()

def typewriter_print(text: str, delay: float = 0.018):
    for char in text:
        console.print(char, end="", flush=True)
        if char in ".,!?;:":
            time.sleep(delay * 3)
        elif char == " ":
            time.sleep(delay * 0.7)
        else:
            time.sleep(delay)
    console.print()

class StreamingResponse:
    def __init__(self):
        self.text = ""
        self.started = False

    def render(self):
        table = Table.grid(expand=True)
        table.add_column()

        if not self.started:
            table.add_row(Spinner("dots12", text="Roommate is thinking...", style="cyan"))
        else:
            table.add_row("Roommate", style="bold green")

        panel = Panel(
            Markdown(self.text if self.text else "[dim]Awaiting response...[/]"),
            title="Response",
            border_style="bright_blue" if not self.started else "green",
            padding=(1, 2),
        )
        table.add_row(panel)
        return table

def check_server() -> bool:
    try:
        ping_url = API_URL.replace("/chat", "/ping")
        requests.get(ping_url, timeout=8)
        return True
    except:
        return False

def stream_chat(prompt: str):
    streamer = StreamingResponse()
    full_response = ""

    with Live(streamer.render(), refresh_per_second=12, console=console) as live:
        try:
            with requests.post(
                API_URL,
                json={"prompt": prompt},
                headers=headers,
                stream=True,
                timeout=3600
            ) as r:
                r.raise_for_status()
                buffer = ""

                for chunk in r.iter_lines(decode_unicode=True):
                    if not chunk:
                        continue
                    buffer += chunk + "\n"
                    lines = buffer.split("\n")
                    buffer = lines.pop()

                    for line in lines:
                        if line.strip():
                            try:
                                data = json.loads(line)
                                content = data.get("message", {}).get("content", "") or data.get("response", "")
                                if content:
                                    full_response += content
                                    streamer.text = full_response
                                    streamer.started = True
                                    live.update(streamer.render())
                            except json.JSONDecodeError:
                                continue

                if buffer.strip():
                    try:
                        data = json.loads(buffer)
                        content = data.get("message", {}).get("content", "") or data.get("response", "")
                        if content:
                            full_response += content
                    except:
                        pass

        except requests.exceptions.RequestException as e:
            console.print(f"\n[red]Connection error: {e}[/]")
            return
        except KeyboardInterrupt:
            console.print("\n[yellow]Cancelled[/]")
            return

    # Final typewriter effect
    console.print("\n" + "━" * 60)
    console.print(Panel.fit("[bold green]Final Response[/]", style="green"))
    console.print()
    typewriter_print(full_response, delay=0.018)
    console.print("━" * 60 + "\n")

def main():
    console.clear()
    console.print(BANNER)
    console.print("[dim]Type 'exit' or press Ctrl+C to quit\n")

    if not check_server():
        console.print("[red]Cannot connect to the Roommate server[/]")
        console.print("[dim]→ Make sure your server is running or the public instance is online[/]")
        sys.exit(1)

    while True:
        try:
            prompt = console.input("\n[bold blue]You:[/] ")

            if not prompt.strip():
                continue
            if prompt.lower().strip() in {"exit", "quit", ":q", "bye", "sair"}:
                console.print(Panel(
                    "[bold green]See you later! Your Roommate is always here ",
                    title="Goodbye!",
                    style="green"
                ))
                break

            console.print(Panel(Markdown(prompt), title="You", border_style="bold blue", padding=(1, 2)))
            stream_chat(prompt)

        except KeyboardInterrupt:
            console.print("\n[yellow]Press Ctrl+C again to exit, or continue chatting![/]")
        except EOFError:
            console.print("\n[bold green]Bye![/]")
            break

if __name__ == "__main__":
    main()
