from typing import Tuple

class Polygon():
    def __init__(self, args: list, id: int):
        if len(args) == 2:
            assert all([type(x) == Tuple for x in args])
            xmin = min([x[0] for x in args])
            xmax = max([x[0] for x in args])
            ymin = min([x[1] for x in args])
            ymax = max([x[1] for x in args])
            self.lims = (xmin, xmax, ymin, ymax)
        elif len(args) == 4:
            assert all([type(x) == float for x in args])
            a, b, c, d = args
            
            
            xmin = min(a, b)
            xmax = max(a, b)
            ymin = min(c, d)
            ymax = max(c, d)
            self.lims = xmin, xmax, ymin, ymax
            
        self.id = id
    
    def contains(self, point: tuple[float, float]):
        x, y = point
        xmin, xmax, ymin, ymax = self.lims
        return (xmin <= x <= xmax) and (ymin <= y <= ymax)