from balancedtree.src.Tree import Tree
from geometry.Polygon import Polygon


class PlaneSweep():
    
    def __init__(self, points: tuple[float, float], squares: list[Polygon]):
        self.__output = 0 # updated whilst handling events
        self.__points = points
        self.__squares = squares
        print("TODO: implement PlaneSweep")
        
        
    def sweep(self):
        self.__getEvents()
        self.__handleEvent()
        return self.__output
        
        
    def __getEvents():
        pass
    
    
    def __handleEvent():
        pass
    
    
    def __findNewEvent():
        pass
    
    
    