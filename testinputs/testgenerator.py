import random

nPoints = int(input("number of points: ").strip())
nSquares = int(input("number of points: ").strip())
testId = int(input("test id: ").strip())

points = []
squares = []

for i in range(nPoints):
    x = int(random.uniform(0, 1000))
    y = int(random.uniform(0, 1000))
    points.append((x, y))
    
for i in range(nSquares):
    xmin = int(random.uniform(0, 1000))
    ymin = int(random.uniform(0, 1000))
    xmax = int(random.uniform(xmin, 1000))
    ymax = int(random.uniform(ymin, 1000))
    
    if xmin == xmax:
        xmax += int(random.uniform(2, 200))
    if ymin == ymax:
        ymax += int(random.uniform(2, 200))
        
    xmin = min(xmin, xmax)
    xmax = max(xmin, xmax)
    ymin = min(ymin, ymax)
    ymax = max(ymin, ymax)
    
    squares.append((xmin, xmax, ymin, ymax))
    
    
with open(f"testinputs/test0{testId}.txt", "x") as f:
    f.write(f"points: {nPoints}\n")
    for point in points:
        f.write(f"{point[0]} {point[1]}\n")
    f.write(f"squares: {nSquares}\n")
    for square in squares:
        f.write(f"{square[0]} {square[1]} {square[2]} {square[3]}\n")