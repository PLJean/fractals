import rhinoscriptsyntax as rs
import math

#define breakpoint
smallestCurve = 0.0125

#Find the y value of the third point using the pythagorean theorem
height = math.sqrt(9 - math.pow(1.5, 2))
print(height)

#define points of triangle
points1 = (0, 0, 0)
points2 = (3, 0, 0)
points3 = (1.5, height, 0)

#define base triangle
line1 = rs.AddLine(points1, points2)
line2 = rs.AddLine(points2, points3)
line3 = rs.AddLine(points3, points1)

def drawTriangle(line):
    #make an array to store the lines
    angle = [0, 0]
    
    #split the input line in two
    split = splitLine(line)
    
    #reconnect the two lines with angle[0]
    angle[0] = rs.AddLine(rs.CurveEndPoint(split[0]), rs.CurveStartPoint(split[1]))
    #rotate angle[0] -60 degrees
    angle[0] = rs.RotateObject(angle[0], rs.CurveEndPoint(split[0]), -60)
    #connect it with the other split line
    angle[1] = rs.AddLine(rs.CurveEndPoint(angle[0]), rs.CurveStartPoint(split[1]))

    if rs.CurveLength(angle[1]) < smallestCurve:
        return
    else:
        #return
        drawTriangle(split[0])
        drawTriangle(split[1])
        drawTriangle(angle[0])
        drawTriangle(angle[1])
        
def splitLine(line):
    #obtain the curve (line) minimum and maximum (domain)
    lineDomain = rs.CurveDomain(line)
    
    min = lineDomain[0]
    max = lineDomain[1]
    OneThird = (max - min)/3
    TwoThird = (max - min) * 2/3
    
    StartLine = rs.TrimCurve(line, (min, min + OneThird), False)
    EndLine = rs.TrimCurve(line, (min + TwoThird, max))
    SplitLine = (StartLine, EndLine)
    
    #return the array of two lines
    return SplitLine
    
drawTriangle(line1)
drawTriangle(line2)
drawTriangle(line3)
