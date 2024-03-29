from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# artist_repository.delete_all()
# album_repository.delete_all()

# create aritsts
artist1 = Artist("Madonna")
artist_repository.create(artist1)
artist2 = Artist("Prince")
artist_repository.create(artist2)


# update artists
# artist2.name = "The artist formerly known as Prince"
# artist_repository.update(artist2)

# create albums
album1 = Album("The Immaculate Collection", "Pop", artist1)
album_repository.create(album1)
album2 = Album("Purple Rain", "Pop", artist2)
album_repository.create(album2)
album3 = Album("Vogue", "PoP", artist1)
album_repository.create(album3)

# Delete artist
# artist_repository.delete_artist(2)

# print function results
# print(artist_repository.select(1).name)
# print(album_repository.select(1).title)

for artist in artist_repository.select_all():
    print(artist.name)

for album in album_repository.select_all():
    print(album.title)

# album_repository.delete_album(3)

for album_from_artist in album_repository.albums_by_artist(artist1):
    print(album_from_artist.title)