import n9b_header_files
i = int
for i in range(99, -1, -1):
    if i == 0:
        n9b_header_files.lyrics("song2", i+99)
    elif i == 2:
        n9b_header_files.lyrics("song3", i)
    elif i == 1:
        n9b_header_files.lyrics("song1", i)
    else:
        n9b_header_files.lyrics("song", i)
