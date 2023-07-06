from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

print("Título do vídeo: " , yt.title)
print("Views: " , yt.views)
print("Autor: ", yt.author)

'''yd = yt.streams.get_audio_only()  #audio
yd = yt.streams.get_highest_resolution()  #vídeo

yd.download('/Users/Geral/Desktop/Projetospython/Projetos-Estudantis/yt_downloader')'''
#*******   erro no DOWNLOAD   ******