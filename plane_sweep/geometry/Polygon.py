class Polygon():
    def __init__(self, args: list, id: int):
        # a, b, c, d = args
        # xmin = min(a, b)
        # xmax = max(a, b)
        # ymin = min(c, d)
        # ymax = max(c, d)
        # self.lims = xmin, xmax, ymin, ymax
        self.lims = args
        self.id = id
    
    def getPoint(self, clockWiseIndex: int):
        xmin, xmax, ymin, ymax = self.lims
        if clockWiseIndex == 0:
            return (xmin, ymin)
        elif clockWiseIndex == 1:
            return (xmax, ymin)
        elif clockWiseIndex == 2:
            return (xmax, ymax)
        elif clockWiseIndex == 3:
            return (xmin, ymax)
        else:
            raise ValueError("clockWiseIndex must be in [0, 3]")
        
    def getLimits(self):
        return self.lims