# Purpose: place a grid of guides on the current glyph, following the italic angle if there is one
# Run once to add a grid of guides; run again to remove the guides. Hook it up to a keyboard shortcut for easy toggling!
# Note: overrides other guidelines on the glyph
# TODO: start grid at baseline, then add horizontal guides below and above

## Helpful extra note: if you're drawing italics, set your italic angle and italic offset:
## http://robofont.com/documentation/how-tos/working-with-italic-slant/

from mojo.UI import setDefault

f = CurrentFont()
g = CurrentGlyph()
UPM = f.info.unitsPerEm

## Set grid size or number of divisions in UPM
# gridSize = 25                         ### uncomment this to use units for grid size (and comment-out the two lines below)
divisions = 20                          ### uncomment this to use divisions of UPM for grid size (and comment-out the line above)
gridSize = int(round(UPM / divisions))  ### uncomment this to use divisions of UPM for grid size


if f.info.italicAngle:
    italicAngle = f.info.italicAngle
else:
    italicAngle = 0

# clear existing guides in glyph
def clearGuides():
    for guide in g.guidelines:
        g.removeGuideline(guide)

# if the glyph already has a bunch of guides clear them and set default guides to be unlocked; otherwise, add them
if len(g.guidelines) > 10:
    print("🤖 There are more than 10 guidelines. Now clearing guides.")
    clearGuides()
    setDefault("glyphViewLockGuides", False) # set to False to unlock guidelines
    
else: 
    print("🤖 Applying a grid of guidelines with a size of " + str(gridSize))
    print("🤖 You have a leftover of " + str(UPM%divisions) + " units.")
    clearGuides()
    setDefault("glyphViewLockGuides", True)
  
    italicOffset = f.lib["com.typemytype.robofont.italicSlantOffset"]
    # add vertical guides
    for x in range(0, g.width+gridSize, gridSize):
        
        if italicOffset:
            xPos = italicOffset
        else:
            xPos = 0
        xPos += x
        g.appendGuideline((xPos, 0), 90+italicAngle)
    
    # add horizontal guides
    for y in range(0, int(UPM), gridSize):
        startAt = f.info.descender
        startAt += y
        g.appendGuideline((italicOffset, startAt),0)
    
    # make guides magnetic, if you want to (It may disrupt drawing, though ¯\_(ツ)_/¯)
    for guide in g.guidelines:
        # control level of "magnetism" for vertical and horizontal
        if guide.angle == 90:
            guide.magnetic = 0
        else:
            guide.magnetic = 0
            
    # make guides magnetic
    for guide in g.guidelines:
        guide.locked = True
    
    
    
    