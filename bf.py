PK     �p�Y ��J       __main__.pyfrom geometry.Polygon import Polygon


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
    points, squares = readInput()
    # points, squares = readInputFromFile()
    
    output = 0
    squares = [Polygon(square) for square in squares]
    
    for point in points:
        for poly in squares:
            if poly.contains(point):
               output += 1 
    
    print(output)


if __name__ == "__main__":
    main()PK     IH�Y            	   geometry/PK     "{�Y               geometry/__pycache__/PK     "{�Y��@�x  x  ,   geometry/__pycache__/Polygon.cpython-312.pyc�
    
^Qg�  �                   �$   � d dl mZ  G d� d�      Zy)�    )�Tuplec                   �.   � e Zd Zdefd�Zdeeef   fd�Zy)�Polygon�argsc                 �  � t        |�      dk(  r�t        |D �cg c]  }t        |�      t        k(  �� c}�      sJ �t	        |D �cg c]  }|d   ��	 c}�      }t        |D �cg c]  }|d   ��	 c}�      }t	        |D �cg c]  }|d   ��	 c}�      }t        |D �cg c]  }|d   ��	 c}�      }||||f| _        y t        |�      dk(  rzt        |D �cg c]  }t        |�      t        k(  �� c}�      sJ �|\  }}}	}
||k7  r|	|
k7  sJ �t	        ||�      }t        ||�      }t	        |	|
�      }t        |	|
�      }||||f| _        y y c c}w c c}w c c}w c c}w c c}w c c}w )N�   r   �   �   )�len�all�typer   �min�max�lims�float)�selfr   �x�xmin�xmax�ymin�ymax�a�b�c�ds              ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\brute_force\geometry\Polygon.py�__init__zPolygon.__init__   s_  � ��t�9��>��$�7�$�Q��Q��5�(�$�7�8�8�8��d�+�d���!��d�+�,�D��d�+�d���!��d�+�,�D��d�+�d���!��d�+�,�D��d�+�d���!��d�+�,�D��t�T�4�0�D�I���Y�!�^��$�7�$�Q��Q��5�(�$�7�8�8�8��J�A�q�!�Q���F�q�A�v�&�%��q�!�9�D��q�!�9�D��q�!�9�D��q�!�9�D��d�D�$�.�D�I� �� 8��+��+��+��+�� 8s#   �D?�E�E	�;E�E�E�pointc                 �r   � |\  }}| j                   \  }}}}||cxk  xr |k  nc xr ||cxk  xr |k  S c S )N)r   )r   r   r   �yr   r   r   r   s           r   �containszPolygon.contains   sB   � ����1�!%�����d�D�$���!�T�!�:���(9�T�(9�:�(9�:�    N)�__name__�
__module__�__qualname__�listr   �tupler   r!   � r"   r   r   r      s#   � �/�T� /�(;�e�E�5�L�1� ;r"   r   N)�typingr   r   r(   r"   r   �<module>r*      s   �� �;� ;r"   PK     IH�YD��  �  ,   geometry/__pycache__/Polygon.cpython-313.pyc�
    WzPg�  �                   �$   � S SK Jr   " S S5      rg)�    )�Tuplec                   �:   � \ rS rSrS\4S jrS\\\4   4S jrSr	g)�Polygon�   �argsc                 ��  � [        U5      S:X  a�  [        U Vs/ sH  n[        U5      [        :H  PM     sn5      (       d   e[	        U Vs/ sH  o"S   PM	     sn5      n[        U Vs/ sH  o"S   PM	     sn5      n[	        U Vs/ sH  o"S   PM	     sn5      n[        U Vs/ sH  o"S   PM	     sn5      nX4XV4U l        g [        U5      S:X  ay  [        U Vs/ sH  n[        U5      [        :H  PM     sn5      (       d   eUu  pxp�Xx:w  a  X�:w  d   e[	        Xx5      n[        Xx5      n[	        X�5      n[        X�5      nX4XV4U l        g g s  snf s  snf s  snf s  snf s  snf s  snf )N�   r   �   �   )�len�all�typer   �min�max�lims�float)�selfr   �x�xmin�xmax�ymin�ymax�a�b�c�ds              �gC:\Users\abuch\Desktop\School\Geometric algorithms\geometric_algorithms\brute_force\geometry\Polygon.py�__init__�Polygon.__init__   sE  � ��t�9��>��$�7�$�Q��Q��5�(�$�7�8�8�8�8��d�+�d��!��d�+�,�D��d�+�d��!��d�+�,�D��d�+�d��!��d�+�,�D��d�+�d��!��d�+�,�D��T�0�D�I���Y�!�^��$�7�$�Q��Q��5�(�$�7�8�8�8�8��J�A�!��F�q�v�&�%��q�9�D��q�9�D��q�9�D��q�9�D��D�.�D�I� �� 8��+��+��+��+�� 8s#   �E	�E�(E�E�"E�E"�pointc                 �   � Uu  p#U R                   u  pEpgXBs=:*  =(       a    U:*  Os  =(       a    Xcs=:*  =(       a    U:*  $ s  $ )N�r   )r   r    r   �yr   r   r   r   s           r   �contains�Polygon.contains   s>   � ����!%�����D��!�!�T�!�:��(9�(9�T�(9�:�(9�:�    r"   N)
�__name__�
__module__�__qualname__�__firstlineno__�listr   �tupler   r$   �__static_attributes__� r&   r   r   r      s#   � �/�T� /�(;�e�E�5�L�1� ;r&   r   N)�typingr   r   r.   r&   r   �<module>r0      s   �� �;� ;r&   PK     IH�Y�����  �     geometry/Polygon.pyfrom typing import Tuple

class Polygon():
    def __init__(self, args: list):
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
            
            assert (a != b and c != d) # dimensions of square must be non-zero
            
            xmin = min(a, b)
            xmax = max(a, b)
            ymin = min(c, d)
            ymax = max(c, d)
            self.lims = xmin, xmax, ymin, ymax
    
    def contains(self, point: tuple[float, float]):
        x, y = point
        xmin, xmax, ymin, ymax = self.lims
        return (xmin <= x <= xmax) and (ymin <= y <= ymax)PK      �p�Y ��J               ��    __main__.pyPK      IH�Y            	          �AF  geometry/PK      "{�Y                      �Am  geometry/__pycache__/PK      "{�Y��@�x  x  ,           ���  geometry/__pycache__/Polygon.cpython-312.pycPK      IH�YD��  �  ,           ��b  geometry/__pycache__/Polygon.cpython-313.pycPK      IH�Y�����  �             ��B  geometry/Polygon.pyPK      �  H    