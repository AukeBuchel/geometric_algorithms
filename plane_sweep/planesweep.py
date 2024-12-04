import math

from intervaltree.intervaltree import IntervalTree, Interval

from geometry.Polygon import Polygon
from queue import PriorityQueue
from priorityqueue.PrioritizedItem import PrioritizedItem


class PlaneSweep():
    
    def __init__(self, points: tuple[float, float], squares: list[Polygon]):
        self.__output = 0 # updated whilst handling events
        self.__points = points
        self.__squares = squares
        
        self.__sweepState = IntervalTree()       
        self.__events = PriorityQueue(2 * len(squares) + len(self.__points)) # 2n + points events max
        
        
    def sweep(self):
        self.__getEvents()
        while self.__events.empty() is False:
            event = self.__events.get(block=False) # don't block, only one thread
            if event is None:
                break
            
            self.__handleEvent(event)
        return self.__output
        
        
    def __getEvents(self):
        # all static events are the start and end points of the squares, as the top-left and bottom-left corners of the squares. Handle event priority ordering automatically based on y, then x coordinates
        for square in self.__squares:
            p = square.getPoint(0) # point is (x, y), but we want to sort by y, then x
            event = PrioritizedItem((p[1], p[0]), square)
            self.__events.put(event)
            
            p = square.getPoint(3) # point is (x, y), but we want to sort by y, then x
            event = PrioritizedItem((p[1], p[0]), square)
            self.__events.put(event)
            
        # points themselves are also events, at these events check which squares they are in
        for point in self.__points:
            event = PrioritizedItem((point[1], point[0]), point)
            self.__events.put(event)
    
    
    def __handleEvent(self, event: PrioritizedItem):
        # is this a point or a square?
        if type(event.item) == Polygon:
            self.__handleSquareEvent(event.priority[0], event.item)
        else: 
            self.__handlePointEvent(event.item)
    
    
    """
    Method for handling square events. Will insert into the sweep line state the start and end of the square interval, as a projection of the square onto the x-axis.
    For each square, we thus get 2 entries in the sweep line state. In order to be able to associate these entries with the square, we will use the square's id as the value of the node.
    The tree ordering is kept based only on the x-coordinate of the square's interval.
    """
    def __handleSquareEvent(self, yValue: float, square: Polygon):
        # add this square's interval to the sweep state
        # is this a square start or end event?
        xmin, xmax, ymin, _ = square.getLimits()
        interval = Interval(xmin, xmax, square.id)
    
        
        if math.isclose(yValue, ymin):
            # square entry event
            self.__sweepState.add(interval)
        else:
            # square exit event
            self.__sweepState.remove(interval)
    
    
    def __handlePointEvent(self, point: tuple[float, float]):
        # check how many intervals of the sweep state this point is in
        # then update the output
        self.__output += self.__countIntervals(point[0])
    
    def __findNewEvent(self):
        # not used, as all events are known in advance
        pass

    
    def __countIntervals(self, xValue: float):
        return len(self.__sweepState[xValue])