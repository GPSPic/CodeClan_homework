from db.run_sql import run_sql
import pdb

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def create(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values =[id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        album = Album(result['title'], result['genre'], result['artist_id'], result['id'])
    return album

def select_all():
    # set up empty list to be returned
    albums = []
    # create s string of sql
    sql = "SELECT * FROM albums"
    # send SQL string to run_sql 
    results = run_sql(sql)

    # pdb.set_trace()
    # translate the dictionaries into objects
    for row in results:
        # create new album object with artist_id as an artist object 
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    # return the list
    return albums

def albums_by_artist(artist):
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    albums = []
    for row in results:
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def delete_album(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id)) = (%s, %s, %s) where id = %s"
    values = [album.title, album.genre, album.artist_id]
    run_sql(sql, values)