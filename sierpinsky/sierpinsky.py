import rhinoscriptsyntax as rs

#define breakpoint
smallestCurve = 0.0125

#define points of triangle
#One can create any size equilateral triangle
point1 = [0, 0, 0]
point2 = [2, 0, 0]
point3 = [0.99999999999999989, 1.7320508075655772, 0]

#define first triangle
line1 = rs.AddLine(point1, point2)
line2 = rs.AddLine(point2, point3)
line3 = rs.AddLine(point3, point1)

def Sierpinsky_triangle(triangle):
    if rs.CurveLength(triangle[0]) < smallestCurve:
        return
    else:
        #make left triangle 
        line1 = rs.AddLine(rs.CurveStartPoint(triangle[0]), rs.CurveMidPoint(triangle[0]))
        line2 = rs.AddLine(rs.CurveMidPoint(triangle[0]), rs.CurveMidPoint(triangle[2]))
        line3 = rs.AddLine(rs.CurveMidPoint(triangle[2]), rs.CurveStartPoint(triangle[0]))
        
        #make right triangle
        line4 = rs.AddLine(rs.CurveMidPoint(triangle[0]), rs.CurveEndPoint(triangle[0]))
        line5 = rs.AddLine(rs.CurveEndPoint(triangle[0]), rs.CurveMidPoint(triangle[1]))
        line6 = rs.AddLine(rs.CurveMidPoint(triangle[1]), rs.CurveMidPoint(triangle[0]))
        
        #make top triangle
        line7 = rs.AddLine(rs.CurveMidPoint(triangle[2]), rs.CurveMidPoint(triangle[1]))
        line8 = rs.AddLine(rs.CurveMidPoint(triangle[1]), rs.CurveEndPoint(triangle[1]))
        line9 = rs.AddLine(rs.CurveStartPoint(triangle[2]), rs.CurveMidPoint(triangle[2]))
        
        #recurse
        Sierpinsky_triangle([line1, line2, line3])
        Sierpinsky_triangle([line4, line5, line6])
        Sierpinsky_triangle([line7, line8, line9])

Sierpinsky_triangle([line1, line2, line3])