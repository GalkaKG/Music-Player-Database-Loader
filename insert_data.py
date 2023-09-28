import pathlib
import psycopg2

files = pathlib.Path('C:/Music')
filtered_data = list(files.rglob('*.mp3'))


con = psycopg2.connect(
    host='localhost',
    database='my_music',
    user='postgres-user',
    password='password'
)

cur = con.cursor()

for f in filtered_data:
    singer = f.parts[2].split(' - ')[0]
    song = f.parts[2].split(' - ')[1]
    file_path = str(f)

    query = '''INSERT INTO music(singer, song, file_path)
    VALUES
        (%s, %s, %s)
    '''

    cur.execute(query, (singer, song, file_path))

con.commit()
