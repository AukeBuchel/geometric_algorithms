from balancedtree.src.Tree import Tree
from balancedtree.src.Node import Node
from geometry.Polygon import Polygon


from queue import PriorityQueue
from priorityqueue.PrioritizedItem import PrioritizedItem
import math


class PlaneSweep():
    
    def __init__(self, points: tuple[float, float], squares: list[Polygon]):
        self.__output = 0 # updated whilst handling events
        self.__points = points
        self.__squares = squares
        
        self.__sweepState = None
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
        
        squareEventIntervalStart = Node(xmin, square.id)
        squareEventIntervalEnd = Node(xmax, square.id)
        
        if math.isclose(yValue, ymin):
            # on-the-fly initialization of the sweep state
            if self.__sweepState is None:
                self.__sweepState = Tree([squareEventIntervalStart, squareEventIntervalEnd])
            else:
                self.__sweepState.insert(xmin, square.id)
                self.__sweepState.insert(xmax, square.id)
        else:
            # square exit event
            self.__sweepState.delete(xmin)
            self.__sweepState.delete(xmax)
    
    
    def __handlePointEvent(self, point: tuple[float, float]):
        # check how many intervals of the sweep state this point is in
        # then update the output
        self.__output += self.__countIntervals(point[0])
    
    def __findNewEvent(self):
        # not used, as all events are known in advance
        pass

    
    def __countIntervals(self, xValue: float):
        # search the balanced tree for xValue. This is likely going to fail, 
        assert self.__sweepState is not None
        
        node: Node = self.__sweepState.root
        visitedIntervals = []
        
        while node is not None:
            [visitedIntervals.append(x) for x in node.value]
            if math.isclose(node.key, xValue):
                return len(set(visitedIntervals))
            elif node.key < xValue:
                node = node.right
            else:
                node = node.left
                
        # we probably don't find the exact xValue, since we only store interval start and end points.
        # thus, at this point we should have the interval that contains xValue
        # we can simply return the number of unique values in the visitedIntervals list
        return len(set(visitedIntervals))