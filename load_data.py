import psycopg2
import pygame


class Song:
    def __init__(self, song, singer, path):
        self.song = song
        self.singer = singer
        self.path = path


con = psycopg2.connect(
    host='localhost',
    database='my_music',
    user='postgres-user',
    password='password'
)

cur = con.cursor()
pygame.init()

query = 'SELECT * FROM music'

cur.execute(query)
data = cur.fetchall()

obj_list = []
for row in data:
    for col in row:
        print(col)
    obj_list.append(Song(row[2], row[1], row[3]))

con.close()
