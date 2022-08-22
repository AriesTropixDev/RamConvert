from __future__ import unicode_literals
import youtube_dl
from termcolor import cprint
from pyfiglet import figlet_format
from time import sleep
import os
import datetime

now = datetime.datetime.now()

def progress_hook(response):
    if response["status"] == "finished":
        file_name = response["filename"]
        x = open("log.txt", 'a')
        print("Downloaded " + file_name)
        x.close()
    if response["status"] == "finished":
      file_name = response["filename"]
      print("Downloaded " + file_name)
    if response["status"] == 'downloading':
        x = open("log.txt", 'a')
        print("Date: ", now.strftime('%m-%d-%Y') ,"Filename:" ,response['filename'], "Progress:" ,response['_percent_str'], "ETA:" ,response['_eta_str'])
        x.close()
    if response["status"] == 'downloading':
      print("Date: ", now.strftime('%m-%d-%Y') ,"Filename:" ,response['filename'], "Progress:" ,response['_percent_str'], "ETA:" ,response['_eta_str'])


clear = lambda: os.system('clear')

clear()
cprint(figlet_format("RamConvert.", font="big"), 'blue', attrs=["bold"])
cprint("Welcome To RamConvert!", "blue", attrs=["bold"])
print('')
print(
    "RamConvert is a YouTube MP3 Audio Downloader that only Requires a YouTube Video URL. RamConvert is powered by Youtube_dl.")
print('')
cprint('References:', 'blue', attrs=['bold'])
print('')
print('• To See Change History - Go to Changelog.md')
print('• To See Privacy Policy - Go to Privacy_Policy.txt')
print('')
cprint('Announcements', 'blue', attrs=['bold'])
cprint('RamConvert Will Receive An Update on 02/02/2022', 'red')
print('')
sleep(4)
cprint("Insert the YouTube Video URL", "blue", attrs=['bold'])
link = input("")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '360',
    }],
    'quiet': True,
    'progress_hooks': [progress_hook],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
