import time
def main():
    playlist = ["Boston","Dracula","I Knew It, I knew You","hate that i made you love me","risk it all"]

    playlist.append("Be by you")

    playlist.insert(0,"Bohemian rhapsody")

    playlist.pop(4)
    print(playlist)
    print(playlist.index('risk it all'))
    print("Number of songs in playlist:",len(playlist))
    playlist.reverse()
    print(playlist)
    playlist.sort()
    print(playlist)

    repeat = len(playlist)
    while repeat > 0:
        print(playlist)
        song = playlist[0]
        playlist.pop(0)
        playlist.append(song)
        repeat -= 1
        time.sleep(3)


if __name__== "__main__":
    main()
