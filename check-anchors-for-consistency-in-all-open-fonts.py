################################################################################################
##################### Check anchors for consistency across all open fonts. #####################
################################################################################################

g = CurrentGlyph()

for font in AllFonts():
    for g in font:
        for anchor in g.anchors:
            # for each font in all open fonts
            for otherFont in AllFonts():
                if g.name in otherFont:
                    # make list of anchor names
                    anchorsInGlyph = []
                    # add anchor names to that list
                    for eachAnchor in otherFont[g.name].anchors:
                        anchorsInGlyph.append(eachAnchor.name)

                    # check that the current anchor name matches an anchor name in the list    
                    if anchor.name not in anchorsInGlyph:
                        print("anchor '" + anchor.name + "' from '" + font.info.styleName + "' in glyph '" + g.name + "'")
                        print("…is not present in '" + otherFont.info.styleName + "' in glyph '" + g.name + "'")
                        print("***************\n")
                    
## Check that no anchors are duplicates within the same glyph
for font in AllFonts():
    for glyph in font:
        if len(glyph.anchors) > 1:
            anchorsInGlyph = []
            for eachAnchor in glyph.anchors:
                    anchorsInGlyph.append(eachAnchor.name)
                    
            # check if there are duplicates in the list by checking the list against a set of the same items
            if len(anchorsInGlyph) != len(set(anchorsInGlyph)):            
                print(font.info.styleName + " |||| Glyph '" + glyph.name + "' contains duplicates in its anchors: \n" + str(anchorsInGlyph))
                print("✨🌟✴️ delete the duplicates to make your world a better place ✴️🌟✨")
                print("***************\n")
    
print("done")
