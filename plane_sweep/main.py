from geometry.Polygon import Polygon
from planesweep import PlaneSweep

def readInput():
    points = []
    squares = []
    
    # number of points
    inp = int(input().split()[1].strip())
    for i in range(inp):
        points.append(tuple(map(float, input().split())))
        
    inp = int(input().split()[1].strip())
    for i in range(inp):
        squares.append(tuple(map(float, input().split())))
        
    for i in range(len(squares)):
        squares[i] = Polygon(squares[i], i)
    return points, squares



def main():
    points, squares = readInput()
    output = 0
    
    ps = PlaneSweep(points, squares)
    output = ps.sweep()
    print(output)
    
    
if __name__ == "__main__":
    main()