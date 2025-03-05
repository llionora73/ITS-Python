def make_album(artist: str, title: str, number_song: int = None) -> dict:
    album = {"artist": artist, "title": title}
    if number_song is not None:
        album["number_of_songs"] = number_song
    return album 

Album1 = make_album("The Beatles", "Abbey Road") 
Album2 = make_album("Vasco Rossi", "Gli spari sopra", number_song=12)
Album3 = make_album("Renato Zero", "Zerofobia")

print(Album1)
print(Album2)
print(Album3)
