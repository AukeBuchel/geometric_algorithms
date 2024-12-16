import math

from intervaltree.intervaltree import IntervalTree, Interval

from geometry.Polygon import Polygon
from queue import PriorityQueue
import heapq
from priorityqueue.PrioritizedItem import PrioritizedItem


class PlaneSweep():
    
    def __init__(self, points: tuple[float, float], squares: list[Polygon]):
        self.__output = 0 # updated whilst handling events
        self.__points = points
        self.__squares = squares
        
        self.__sweepState = IntervalTree()       
        self.__events = []
        
        
    def sweep(self):
        self.__getEvents()
        while len(self.__events) > 0:
            event = heapq.heappop(self.__events) # don't block, only one thread
            if event is None:
                break
            
            self.__handleEvent(event)
        return self.__output
        
        
    def __getEvents(self):
        # all static events are the start and end points of the squares, as the top-right and bottom-right corners of the squares. 
        # Handle event priority ordering automatically based on y, then x coordinates
        # it is important that we choose the right-most points, because if a point has the same y-coordinate as the top or bottom boundary,
        # we want to handle the point first. Tuples provide this ordering automatically, so long as the x coordinate of the square is the right boundary
        # moreover, to handle points before squares in cases where the point lies on the right boundary AND top or bottom boundary, we add a third element
        # to the priority tuple, which is set so that 
        # - square bottom boundaries (entry) are handled before points
        # - square top boundaries (exit) are handled after points
        for square in self.__squares:
            
            # bottom boundary
            p = square.getPoint(0) # point is (x, y), but we want to sort by y, then x
            event = PrioritizedItem((p[1], p[0], 0), square)
            heapq.heappush(self.__events, event)
            
            # top boundary
            p = square.getPoint(2) # point is (x, y), but we want to sort by y, then x
            event = PrioritizedItem((p[1], p[0], 2), square)
            heapq.heappush(self.__events, event)
            
        # points themselves are also events, at these events check which squares they are in
        for point in self.__points:
            event = PrioritizedItem((point[1], point[0], 1), point)
            heapq.heappush(self.__events, event)
    
    
    def __handleEvent(self, event: PrioritizedItem):
        # is this a point or a square?
        if type(event.item) == Polygon:
            self.__handleSquareEvent(event.priority[0], event.item)
        else: 
            self.__handlePointEvent(event.item)    
    
    """
    Method for handling square events: the bottom boundary of the square. Handle these with 
    """
    def __handleSquareEvent(self, yValue: float, square: Polygon):
        # add this square's interval to the sweep state
        # is this a square start or end event?
        xmin, xmax, ymin, _ = square.getLimits()
        interval = Interval(xmin, xmax, square.id)
            
        if yValue == ymin:
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
        # x = self.__sweepState[xValue]
        # for i in x:
            # print(f"Point {xValue} is in square {i.data}")
            
        # print(f"point {xValue} checked in tree") 
        # self.__sweepState.print_structure()            
    
        return self.__sweepState.countPointOverlaps3(xValue)
