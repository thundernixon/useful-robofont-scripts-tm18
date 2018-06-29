from vanilla.dialogs import *
import os
import math
from mojo.UI import AskYesNoCancel

files =  getFile("Select files to print family name", allowsMultipleSelection=True, fileTypes=["ufo"])

separator = "---------------------------------------------------------------"

print(separator)

# def checkIfOkay(masterToSendToName):
#     proceedWithSloping = AskYesNoCancel("This will overwrite italic info and skew all chars in " + masterToSendToName+"." +" Proceed?")
  
#     print(proceedWithSloping)
#     return proceedWithSloping



# checkIfOkay()

for file in files:
    font = OpenFont(file)
    print("file name: \t \t '" + os.path.split(file)[1] + "'")
    print("family name: \t \t '" + font.info.familyName + "'")
    print("style name: \t \t '" + font.info.styleName + "'")
    font.info.italicAngle = -14.04
    print("italic angle: \t \t '" + str(font.info.italicAngle) + "'")        
    italicSlantOffset = math.tan(font.info.italicAngle * math.pi / 180) * (font.info.xHeight * 0.5)
    print("italic offset should be: \t \t '" + str(round(italicSlantOffset)) + "'")  
    font.lib['com.typemytype.robofont.italicSlantOffset'] = round(italicSlantOffset)
    print(separator)
    
    
    
    for g in font:
        
        font[g.name].decompose()

    for g in font:
        # g.decompose()
     
        font[g.name].skewBy(-font.info.italicAngle) 
        font[g.name].moveBy((italicSlantOffset, 0))
        

# italicSlantOffset = math.tan(f.info.italicAngle * math.pi / 180) * (f.info.xHeight * 0.5)

# # set the italic slant offset in font
# font.lib['com.typemytype.robofont.italicSlantOffset'] = round(italicSlantOffset)