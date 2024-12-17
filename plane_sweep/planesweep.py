import math

from intervaltree.intervaltree import IntervalTree, Interval
from segmenttree.segmenttree import SegmentTree, sum_operation


from geometry.Polygon import Polygon
from queue import PriorityQueue
import heapq
from priorityqueue.PrioritizedItem import PrioritizedItem


class PlaneSweep():
    
    def __init__(self, points: tuple[float, float], squares: list[Polygon]):
        self.__output = 0 # updated whilst handling events
        self.__points = points
        self.__squares = squares
        
        self.x_compressed = None
        self.__sweepState = None
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
        
        
        x_cords = set()
        # compress the x coordinates of the squares
        for square in self.__squares:            
            
            # compress the x coordinates
            xmin, xmax, _, _ = square.getLimits()
            x_cords.add(xmin)
            x_cords.add(xmax)
            
        # compress the x coordinates of the points
        for point in self.__points:
            x_cords.add(point[0])
            
        # compress the x coordinates
        x_compressed = {x: i for i, x in enumerate(sorted(x_cords))}
    
        # prepare the event queue
        for square in self.__squares:
            xmin, xmax, ymin, ymax = square.getLimits()
            
            # entry boundary
            event = PrioritizedItem((ymin, 0, x_compressed[xmin], x_compressed[xmax]), square)
            heapq.heappush(self.__events, event)
            
            # exit boundary
            event = PrioritizedItem((ymax, 2, x_compressed[xmin], x_compressed[xmax]), square)
            heapq.heappush(self.__events, event)
            
        for point in self.__points: 
            event = PrioritizedItem((point[1], 1, x_compressed[point[0]]), point)
            heapq.heappush(self.__events, event)
            
            
        self.__sweepState = SegmentTree([0] * len(x_compressed), operations=[sum_operation])
        self.x_compressed = x_compressed
    
    
    
    def __handleEvent(self, event: PrioritizedItem):
        # is this a point or a square?
        if type(event.item) == Polygon:
            self.__handleSquareEvent(event.priority, event.item)
        else: 
            self.__handlePointEvent(event.priority, event.item)    
    
    """
    Method for handling square events: the bottom boundary of the square. Handle these with 
    """
    def __handleSquareEvent(self, priority: tuple[float, int, float, float], square: Polygon):
        _, tag, xmin, xmax = priority
        
        
        # add this square's interval to the sweep state
        # is this a square start or end event?
        
        isEntry = True if (tag == 0) else False

        if isEntry:
            print("entry event")
            self.__sweepState.update_range(xmin, xmax, 1)            
        else:
            print("exit event")
            self.__sweepState.update_range(xmin, xmax, 0)    
    
    def __handlePointEvent(self, priority, point: tuple[float, float]):
        # check how many intervals of the sweep state this point is in
        # then update the output
        print("point event")
        _, _, x = priority
        self.__output += self.__countIntervals(x)
    
    def __findNewEvent(self):
        # not used, as all events are known in advance
        pass

    
    def __countIntervals(self, xValue: float):
        # x = self.__sweepState[xValue]
        # for i in x:
        #     print(f"Point {xValue} is in square {i.data}")
            
        # print(f"point {xValue} checked in tree") 
        # self.__sweepState.print_structure()            
        res = self.__sweepState.query(xValue, xValue, "sum")
        
        if res is None:
            return 0
        
        return res
