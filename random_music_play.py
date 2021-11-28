import random, os

music_dir = 'E:\\Music/tylor_swift'

songs = os.listdir(music_dir)
song = random.randint(0, len(songs))
print(songs[song])

os.startfile(os.path.join(music_dir, songs[0]))