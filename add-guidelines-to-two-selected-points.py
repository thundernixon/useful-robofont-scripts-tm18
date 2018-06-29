import math

g = CurrentGlyph()

pointsSelected = []

for contour in g:
    for seg in contour:
        for point in seg:
            if point.selected:
                print(point.x, point.y)
                pointsSelected.append((point.x, point.y))          

pointRadians = math.atan2(pointsSelected[1][1]-pointsSelected[0][1], pointsSelected[1][0]-pointsSelected[0][0])

pointDegrees = math.degrees(pointRadians)

guidelineCoordinates = (pointsSelected[0][0], pointsSelected[0][1])

g.appendGuideline(guidelineCoordinates, pointDegrees)