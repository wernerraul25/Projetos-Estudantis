from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

titulo = yt.title
views = yt.views
autor = yt.author

print("Título do vídeo: " , titulo)
print("Views: " , views)
print("Autor: ", autor)

yd = yt.streams.get_audio_only()  #audio
yd = yt.streams.get_highest_resolution()  #vídeo

try:
    yd.download('/Users/Geral/Downloads') #download video
    print('Download de', '"'+titulo+'"', 'concluído!')
except:
    print("Erro no download!")