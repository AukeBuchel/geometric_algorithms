from balancedtree.src.Tree import Tree
from geometry.Polygon import Polygon
from queue import PriorityQueue
from priorityqueue.PrioritizedItem import PrioritizedItem



class PlaneSweep():
    
    def __init__(self, points: tuple[float, float], squares: list[Polygon]):
        self.__output = 0 # updated whilst handling events
        self.__points = points
        self.__squares = squares
        
        self.__events = PriorityQueue(2 * len(squares) + len(self.__points)) # 2n + points events max
        self.__sweepState = Tree() # *balanced* binary search tree, which python does not have by default
        print("TODO: implement PlaneSweep")
        
        
    def sweep(self):
        self.__getEvents()
        while len(self.__events) > 0:
            event = self.__events.get()
            self.__handleEvent(event)
        return self.__output
        
        
    def __getEvents(self):
        # all static events are the start and end points of the squares, as the top-left and bottom-left corners of the squares. Handle event priority ordering automatically based on y, then x coordinates
        for square in self.__squares:
            p = square.getPoint(0) # point is (x, y), but we want to sort by y, then x
            event = PrioritizedItem((p[1], p[0]), square)
            self.__events.put(event)
            
            p = square.getPoint(2) # point is (x, y), but we want to sort by y, then x
            event = PrioritizedItem((p[1], p[0]), square)
            self.__events.put(event)
            
        # points themselves are also events, at these events check which squares they are in
        for point in self.__points:
            event = PrioritizedItem((point[1], point[0]), point)
            self.__events.put(event)
    
    
    def __handleEvent(self, event: PrioritizedItem):
        # is this a point or a square?
        if type(event.item) == Polygon:
            self.__handleSquareEvent(event.item)
        else: 
            self.__handlePointEvent(event.item)
    
    
    def __handleSquareEvent(self, square: Polygon):
        # add this square's interval to the sweep state
        pass
    
    
    def __handlePointEvent(self, point: tuple[float, float]):
        # check how many intervals of the sweep state this point is in
        # then update the output
        pass
    
    def __findNewEvent(self):
        # not used, as all events are known in advance
        pass

    
    