import os
import re
from pytube import Playlist

playlist = Playlist('https://www.youtube.com/watch?v=VsreClRvTyQ&list=PL6gXJiXPDzu28WS3FJd7Yjk49eTrrpqLs')

DOWNLOAD_DIR = 'E:\\'

pasta = DOWNLOAD_DIR + '\\%s' % playlist.title

if os.path.isdir(pasta): # vemos de este diretorio ja existe
    print ('Ja existe uma pasta com esse nome!')
else:
    os.mkdir(DOWNLOAD_DIR + '\\%s' % playlist.title) # aqui criamos a pasta caso nao exista
    print ('Pasta criada com sucesso!')

for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video = video.streams.get_by_itag(251)
    downloaded_file = video.download(pasta)
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
