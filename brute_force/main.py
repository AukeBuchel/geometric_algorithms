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


def readInputFromFile():
    with open("testinputs/test02.txt", "r") as f:
        points = []
        squares = []
        
        # number of points
        inp = int(f.readline().split()[1].strip())
        for i in range(inp):
            points.append(tuple(map(float, f.readline().split())))
        inp = int(f.readline().split()[1].strip())
        for i in range(inp):
            squares.append(tuple(map(float, f.readline().split())))
            
        return points, squares


def main():
    # points, squares = readInput()
    points, squares = readInputFromFile()
    
    output = 0
    squares = [Polygon(square) for square in squares]
    
    for point in points:
        for poly in squares:
            if poly.contains(point):
               output += 1 
    
    print(output)


if __name__ == "__main__":
    main()