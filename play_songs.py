import pygame
import time
import load_data

pygame.init()

playlist = load_data.obj_list

pygame.mixer.init()

for mp3_file in playlist:
    print()
    print('*' * 56)
    print(f'Singer: {mp3_file.singer}\nSong: {mp3_file.song}')
    pygame.mixer.music.load(mp3_file.path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)


pygame.quit()
