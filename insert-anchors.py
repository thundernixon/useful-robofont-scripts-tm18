from fontParts import *

# f= CurrentFont()
g = CurrentGlyph()


# help(g)
# help(g.appendAnchor)

xHeightGlyphsWithTopAnchor = [
    "a",
    "ae",
    "c",
    "e",
    "flatg", # flat-top form
    "dotlessi",
    "dotlessj",
    "n",
    "o",
    "oslash",
    "r",
    "s",
    "u",
    "w",
    "y",
    "z"
]

ascHeightGlyphsWithTopAnchor = [
    "h",
    "l"
    ]
    
capHeightGlyphsWithTopAnchor = [
    "A",
    "AE",
    "C",
    "D",
    "E",
    "G",
    "H",
    "I",
    "J",
    "L",
    "N",
    "O",
    "Oslash",
    "R",
    "S",
    "T",
    "U",
    "W",
    "Y",
    "Z"    
    ]

glyphsWithBottomAnchor = [
    "a",
    "c",
    "e",
    "i",
    "k",
    "l",
    "n",
    "o",
    "r",
    "s",
    "t",
    "u",
    
    "A",
    "C",
    "E",
    "G",
    "I",
    "K",
    "L",
    "O",
    "N",
    "R",
    "S",
    "T",
    "U"
    ]

glyphsWithOgonekAnchor= [
    "a",
    "e",
    "i",
    "o",
    "u",
    "A",
    "E",
    "I",
    "O",
    "U"
    ]
    
glyphsWithCaronslovakAnchor = [
    "d",
    "l",
    "n", # very debatable, but worth it for now
    "t",
    "L"
    ]

glyphsWithMiddleDotAnchor = [
    "l",
    "L"
    ]
    
glyphsWithRingAnchor = [
    "A",
    "U"
    ]
    
# glyphsWithApostropheAnchor = [
#     "n"
#     ]
    
    
# make this a dictionary
# glyphDict = {
#     xHeightGlyphsWithTopAnchor: "top",
#     ascHeightGlyphsWithTopAnchor: "top",
#     glyphsWithBottomAnchor:"bottom",
#     glyphsWithOgonekAnchor: "ogonek",
#     glyphsWithCaronslovakAnchor: "caronslovak"
#     }

glyphWithAnchorLists = [
    (xHeightGlyphsWithTopAnchor, "top", "xHeight"),
    (ascHeightGlyphsWithTopAnchor, "top", "ascHeight"),
    (capHeightGlyphsWithTopAnchor, "top", "capHeight"),
    (glyphsWithBottomAnchor, "bottom", "baseline"),
    (glyphsWithOgonekAnchor, "ogonek", "baseline"),
    (glyphsWithMiddleDotAnchor, "dot", "middle"),
    (glyphsWithCaronslovakAnchor, "caronslovak", "capHeight"),
    (glyphsWithRingAnchor, "ring","capHeight"),
    # (glyphsWithRingAnchor, "apostrophe","xHeight")
]
    
def addAnchors(f):
    for glyphWithAnchorList in glyphWithAnchorLists:
        print(glyphWithAnchorList[1])
    
        if glyphWithAnchorList[2] == "xHeight":
            anchorHeight = f.info.xHeight + 11
        elif glyphWithAnchorList[2] == "ascHeight": 
            anchorHeight = f.info.ascender - 20
        elif glyphWithAnchorList[2] == "capHeight": 
            anchorHeight = f.info.capHeight + 11
        elif glyphWithAnchorList[2] == "baseline": 
            anchorHeight = -1
        elif glyphWithAnchorList[2] == "middle":
            anchorHeight = f.info.capHeight/2 + 50
    
        for glyphName in glyphWithAnchorList[0]:
        
            print("==================================================")
            print(glyphName)
        
            print("---")
        
        
            if glyphName in f:
                realGlyphWidth = f[glyphName].width - f[glyphName].leftMargin - f[glyphName].rightMargin 
                glyphCenter = (realGlyphWidth/2) + f[glyphName].leftMargin
        
                if glyphWithAnchorList[1] == "caronslovak" or glyphWithAnchorList[1] == "dot":
                    glyphCenter += 150
            
                if glyphWithAnchorList[1] == "ogonek":
                    glyphCenter += 150
                    
                # if glyphWithAnchorList[1] == "apostrophe":
                #     glyphCenter -= 150
            
                if glyphName == "h":
                    glyphCenter -= 160
        
                glyphAnchors = []
        
        
                for anchor in f[glyphName].anchors:
                    print(anchor.name)
                    glyphAnchors.append(anchor.name)
        
                print(glyphAnchors)
        
        
            
                if glyphWithAnchorList[1] not in glyphAnchors:
            
                    print("adding anchor '" + glyphWithAnchorList[1] + "' at " + str(int(glyphCenter)), str(int(anchorHeight)))
            
                    f[glyphName].appendAnchor(glyphWithAnchorList[1], (int(glyphCenter), int(anchorHeight)))

for f in AllFonts():
    addAnchors(f)