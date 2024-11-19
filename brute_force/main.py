from geometry.Polygon import Polygon


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
        
    return points, squares



def main():
    points, squares = readInput()
    polygons = []
    
    output = 0
    for square in squares: 
        polygons.append(Polygon(square))
    
    for point in points:
        for poly in polygons:
            if poly.contains(point):
               output += 1 
    
    print(output)


if __name__ == "__main__":
    main()