### copy sidebearings from one font to another
### a script to fix spacing in corrected italics, which were started on before "italic offset" was in place

# easy: just copying the left sidebearing (probably too simplistic)

# medium: giving the same "average" sidebearing
    # example: R upright is 80 on left and 40 on right, but italic form is slightly wider ... So it could be 70 on left, and 35 on right
    # BUT because my italic tries to be just a slanted roman, this is probably not very necessary
    # I'll test the simplistic version first, and fix if necessary
    

from vanilla.dialogs import *
from mojo.UI import AskYesNoCancel
import math

def srcUFO():
    
    print("getting source font")
    ## let user select masterToCopyFrom
    masterToCopyFromPath =  getFile("Please pick a master to copy anchor x positions from")
    # print(masterToCopyFromPath)

    srcUFO = OpenFont(masterToCopyFromPath)[0]
    
    srcUFOName = srcUFO.info.familyName + " " + srcUFO.info.styleName
    
    return srcUFO, srcUFOName

def destUFO():
    print("getting destination font")
    ## let user select masterToSendTo
    destUFOPath =  getFile("Please pick a master to overwrite anchor x positions into")
    # print(masterToSendToPath)
    destUFO = OpenFont(destUFOPath)[0]
    
    destUFOName = destUFO.info.familyName + " " + destUFO.info.styleName
    
    return destUFO, destUFOName

def checkIfOkay(srcUFOName, destUFOName):
    proceedWithCopy = AskYesNoCancel("This will overwrite anchor x positions from " + srcUFOName + " into " + destUFOName+"." +" Proceed?")
    return proceedWithCopy
    
    
def calculateItalicAnchorPos(destUFO, desiredX, desiredY):
    italicAngle = destUFO.info.italicAngle
    anteItalicAngle = 90 - abs(italicAngle)
    
    addX = desiredY * math.sin(math.radians(abs(italicAngle))) / math.sin(math.radians(abs(anteItalicAngle)))
    
    return addX
    

def copyAnchorXPos(srcUFO, srcUFOName, destUFO, destUFOName):
    # destUFO, destUFOName = destUFO()[0], destUFO()[1]
    # srcUFO, srcUFOName = srcUFO()[0], srcUFO()[1]
    
    # print(checkIfOkay(srcUFOName, destUFOName))
    print("copying from " + srcUFOName + " into " + destUFOName)    
    
    italicOffset = destUFO.lib["com.typemytype.robofont.italicSlantOffset"]
    print("italicOffset is " + str(italicOffset))
    if checkIfOkay(srcUFOName, destUFOName) == 1:
        for g in destUFO:
            
            destGlyphAnchorsDict = {}
            for anchor in g.anchors:
                destGlyphAnchorsDict[anchor.name] = (anchor.x, anchor.y)
                
            srcGlyphAnchorsDict = {}
            for anchor in srcUFO[g.name].anchors:
                srcGlyphAnchorsDict[anchor.name] = (anchor.x, anchor.y)
            
            print(g.name + str(srcGlyphAnchorsDict))
                
            for anchor in g.anchors:
                
                addX = calculateItalicAnchorPos(destUFO, srcGlyphAnchorsDict[anchor.name][0],srcGlyphAnchorsDict[anchor.name][1])
                
                newX = srcGlyphAnchorsDict[anchor.name][0] + addX - abs(italicOffset)
                print("srcX is " + str(srcGlyphAnchorsDict[anchor.name][0]) + " so newX should be " + str(newX))
                anchor.x = newX
                print("'" + g.name + "', anchor '" +  anchor.name + "' moved from " + str(destGlyphAnchorsDict[anchor.name][0]) + " to " + str(newX))
            
            g.changed()
                

            
            print("--------------------")

# srcUFO, srcUFOName = srcUFO()[0], srcUFO()[1]
# destUFO, destUFOName = destUFO()[0], destUFO()[1]

srcUFO, srcUFOName = srcUFO()
destUFO, destUFOName = destUFO()

copyAnchorXPos(srcUFO, srcUFOName, destUFO, destUFOName)