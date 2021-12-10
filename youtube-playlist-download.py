from pytube import Playlist
import shutil
import os

yt = Playlist(
	str(input("Url da Playlist \n>> ")))

pasta_downloads = '%s' % yt.title

if os.path.isdir(pasta_downloads):
  print('A pasta %s já existe, dando continuidade ao processo' %yt.title)
else:
  os.mkdir(pasta_downloads)
  print("Pasta criada com sucesso")


for video in yt.videos:

  video = video.streams.filter(only_audio=True).first()

  out_file = video.download(output_path=pasta_downloads)

  base, ext = os.path.splitext(out_file)
  new_file = base + '.mp3'
  os.rename(out_file, new_file)

  print(video.title + " has been successfully downloaded.")

shutil.make_archive(pasta_downloads, 'zip', './', pasta_downloads)




