import os
import yt_dlp
from rich import print
from log import console,get_progress,get_ydl_opts
from rich.console import Console
video_path="/storage/emulated/0/videos"
audio_path="/storage/emulated/0/Download/musica"
console=Console()

def limpiar():
    console.clear()


def obtener_cookies():
    if os.path.exists("cookies.txt"):
        return "cookies.txt"

    return None

def guardar_video():
    limpiar()
    os.makedirs(video_path, exist_ok=True)
    while True:
        print("[bold cyan]1.[/bold cyan] [bold blue]ingresar link[/bold blue]")
        print("[bold cyan]2.[/bold cyan][bold blue] salir[/bold blue]")
        opcion=input("> ")
        if opcion=="1":
            url = console.input("[bold green]ingresar link: [/bold green]")
        elif opcion=="2":
            break


    progress, hook = get_progress()
    opts = get_ydl_opts(video_path, hook)

    yt_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": f"{video_path}/%(title)s.%(id)s.%(ext)s",
    }

    cookies = obtener_cookies()
    if cookies:
        yt_opts["cookiefile"] = cookies

    final_opts = {**opts, **yt_opts}
    final_opts["progress_hooks"] = [hook]

    with progress:
        with yt_dlp.YoutubeDL(final_opts) as ydl:
            ydl.download([url])


def guardar_audio():
    limpiar()
    os.makedirs(audio_path,exist_ok=True)
    while True:
        print("[bold cyan]1.[/bold cyan] [bold blue]ingresar link[/bold blue]")
        print("[bold cyan]2.[/bold cyan] [bold blue]salir[/bold blue]")
        opcion=input("> ")
        if opcion=="1":
            url = console.input("[bold green]ingresar link: [/bold green]")
        elif opcion=="2":
            break
    progress,hook=get_progress()
    opts= get_ydl_opts(audio_path,hook)


    yt_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{audio_path}/%(title)s.%(id)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "0"
        }]
    }

    cookies = obtener_cookies()

    if cookies:
        yt_opts["cookiefile"] = cookies
    final_opts= {**opts,**yt_opts}
    final_opts["progress_hooks"] = [hook]

    with progress:
        with yt_dlp.YoutubeDL(final_opts) as ydl:
            ydl.download([url])


def guardar_tiktok():
    limpiar()
    os.makedirs(video_path, exist_ok=True)
    while True:
        print("[bold cyan]1.[/bold cyan][bold blue]ingresar link[/bold blue]")
        print("[bold cyan]2.[/bold cyan][bold blue]salir[/bold blue]")
        opcion=input("> ")
        if opcion=="1":
            url = console.input("[bold green]link de tiktok: [/bold green]")
        elif opcion=="2":
            break

    progress,hook= get_progress()
    opts=get_ydl_opts(video_path,hook)

    yt_opts = {
        "format": "best",
        "outtmpl": f"{video_path}/%(title)s.%(id)s.%(ext)s",
    }

    cookies = obtener_cookies()

    if cookies:
        yt_opts["cookiefile"] = cookies
    final_opts={**opts,**yt_opts}
    final_opts["progress_hooks"] = [hook]
    with progress:
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.download([url])
