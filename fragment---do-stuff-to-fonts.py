inputFonts = getFile("select UFOs", allowsMultipleSelection=True, fileTypes=["ufo"])

for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)
    
    # do stuff to the font, e.g. sort, check anchors, add fea code, etc
    
    f.save()
    f.close()