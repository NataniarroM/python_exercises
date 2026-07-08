def make_album(name, title, tracks=""):
    if tracks:
        album = {"artist_name":name, "album_title":title, "number_of_tracks":tracks}
    else:
        album = {"artist_name":name, "album_title":title}
    return album

while True:
    choice = input("Deseja adicionar um álbum('n' para sair)? ").lower()
    if choice == "n":
        break

    artist = input("Digite o nome do artista/banda: ").lower()
    title = input("Digite o nome do álbum: ").lower()
    album = make_album(artist, title)

    print(album)
