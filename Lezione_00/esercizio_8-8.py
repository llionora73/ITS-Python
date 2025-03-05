def make_album(artist: str, title: str) -> dict:
    return {"artist": artist, "title": title}

while True:
    print("\nEnter album details (or type 'quit' to stop):")
    
    artist = input("Artist: ")
    if artist == 'quit':
        break

    title = input("Album Title: ")
    if title == 'quit':
        break

    album = make_album(artist, title)
    print("\nAlbum created:", album)