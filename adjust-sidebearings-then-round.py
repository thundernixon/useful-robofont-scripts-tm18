### add sidebearings to selected glyphs

f = CurrentFont()

sidebearing = 40

roundingUnit = 50

def roundToNearestUnit(x, base):
    return int(base * round(float(x)/base))

for g in f.selection:
    f[g].leftMargin = sidebearing # avg margin for fonts
    f[g].rightMargin = sidebearing # avg margin for fonts
    print(f[g].leftMargin, f[g].rightMargin, f[g].width)
    
    
    roundedWidth = roundToNearestUnit(f[g].width, roundingUnit)
    
    f[g].width = roundedWidth
    
    totalNewMargin = f[g].leftMargin + f[g].rightMargin
    
    print(totalNewMargin)
    
    f[g].leftMargin = totalNewMargin/2
    f[g].rightMargin = totalNewMargin/2
    
    print(f[g].leftMargin, f[g].rightMargin, f[g].width)


