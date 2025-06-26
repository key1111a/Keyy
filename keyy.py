from rich.console import Console
from rich.panel import Panel
import os

console = Console()

def menu():
    os.system("clear")
    console.print(Panel("[bold cyan]KEYY TOOLS - by kunci1111a[/bold cyan]\n[green]Tools serbaguna: Spam, Musik, TikTok[/green]"), justify="center")
    console.print("[1] Spam SMS / WA / Call", style="bold green")
    console.print("[2] Stel Musik", style="bold yellow")
    console.print("[3] Download Video TikTok Tanpa Watermark", style="bold blue")
    console.print("[4] Keluar", style="bold red")
    pilih = input("\n[?] Pilih menu > ")
    return pilih

while True:
    pilihan = menu()
    if pilihan == "1":
        os.system("python spam/spam.py")
    elif pilihan == "2":
        os.system("python musik/play.py")
    elif pilihan == "3":
        os.system("python tiktok/downloader.py")
    elif pilihan == "4":
        exit()
    else:
        print("Pilihan tidak valid!")
