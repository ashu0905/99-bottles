song = ""
song1 = ""
song2 = ""
song3 = ""
songs = ""
song = "{} bottles of beer on the wall, {} bottles of beer.\n Take 1 down & pass it around, {} bottles of beer on the wall.\n"
song1 = "{} bottle of beer on the wall, {} bottle of beer.\n Take 1 down & pass it around, {} bottle of beer on the wall.\n"
song2 = "No more bottles of beer on the wall, no more bottles of beer.\n Go to the store and buy some more, {} bottles of beer on th    e wall.\n"
song3 = "{} bottles of beer on the wall, {} bottles of beer.\n Take 1 down & pass it around, {} bottle of beer on the wall.\n"
def lyrics(songs, i):
    if songs == "song":
        print((song).format(i, i, i-1))
    elif songs == "song3":
        print((song3).format(i, i, i-1))
    elif songs == "song1":
        print((song1).format(i, i, i-1))
    else:
        print((song2).format(i))
