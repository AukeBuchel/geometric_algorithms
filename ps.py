PK     �l�YS0�"�  �     __main__.pyfrom geometry.Polygon import Polygon
from planesweep import PlaneSweep

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
        
    for i in range(len(squares)):
        squares[i] = Polygon(squares[i], i)
    return points, squares

def readInputFromFile():
    with open("testinputs/test06.txt", "r") as f:
        points = []
        squares = []
        
        # number of points
        inp = int(f.readline().split()[1].strip())
        for i in range(inp):
            points.append(tuple(map(float, f.readline().split())))
        inp = int(f.readline().split()[1].strip())
        for i in range(inp):
            squares.append(tuple(map(float, f.readline().split())))
            
        for i in range(len(squares)):
            squares[i] = Polygon(squares[i], i)
        return points, squares


def main():
    try:
        points, squares = readInput()
        # points, squares = readInputFromFile()
        output = 0
        
        ps = PlaneSweep(points, squares)
        output = ps.sweep()
        print(output)
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    main()PK     j�Y               __pycache__/PK     &��Y_�:��  �  $   __pycache__/__main__.cpython-312.pyc�
    &\\g�  �                   �H   � d dl mZ d dlmZ d� Zd� Zd� Zedk(  r e�        yy)�    )�Polygon)�
PlaneSweepc            
      �h  � g } g }t        t        �       j                  �       d   j                  �       �      }t	        |�      D ]@  }| j                  t        t        t        t        �       j                  �       �      �      �       �B t        t        �       j                  �       d   j                  �       �      }t	        |�      D ]@  }|j                  t        t        t        t        �       j                  �       �      �      �       �B t	        t        |�      �      D ]  }t        ||   |�      ||<   � | |fS )N�   )�int�input�split�strip�range�append�tuple�map�float�lenr   )�points�squares�inp�is       ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\__main__.py�	readInputr      s�   � ��F��G� �e�g�m�m�o�a� �&�&�(�
)�C��3�Z�����e�C��u�w�}�}��7�8�9� � �e�g�m�m�o�a� �&�&�(�
)�C��3�Z�����u�S�������8�9�:� � �3�w�<� ���W�Q�Z��+���
� !��7�?��    c                  ��  � t        dd�      5 } g }g }t        | j                  �       j                  �       d   j	                  �       �      }t        |�      D ]F  }|j                  t        t        t        | j                  �       j                  �       �      �      �       �H t        | j                  �       j                  �       d   j	                  �       �      }t        |�      D ]F  }|j                  t        t        t        | j                  �       j                  �       �      �      �       �H t        t        |�      �      D ]  }t        ||   |�      ||<   � ||fcd d d �       S # 1 sw Y   y xY w)Nztestinputs/test09.txt�rr   )�openr   �readliner	   r
   r   r   r   r   r   r   r   )�fr   r   r   r   s        r   �readInputFromFiler      s  � �	�%�s�	+�q����� �!�*�*�,�$�$�&�q�)�/�/�1�2���s��A��M�M�%��E�1�:�:�<�+=�+=�+?� @�A�B� ��!�*�*�,�$�$�&�q�)�/�/�1�2���s��A��N�N�5��U�A�J�J�L�,>�,>�,@�!A�B�C� � �s�7�|�$�A� ����Q�/�G�A�J� %��w�� 
,�	+�	+�s   �EE"�"E+c                  �   � 	 t        �       \  } }d}t        | |�      }|j                  �       }t        |�       y # t        $ r}|�d }~ww xY w)Nr   )r   r   �sweep�print�	Exception)r   r   �output�ps�es        r   �mainr%   '   sK   � �	�+�-���������(��������f���� �����s   �69 �	A	�A�A	�__main__N)�geometry.Polygonr   �
planesweepr   r   r   r%   �__name__� r   r   �<module>r+      s.   �� $� !��"�$
� �z���F� r   PK     ֋�Y%;��L  L  &   __pycache__/planesweep.cpython-311.pyc�
    �>dg�  �                   �t   � d dl Z d dlmZmZ d dlmZmZ d dlmZ d dl	m
Z
 d dlZd dlmZ  G d� d�  �        ZdS )	�    N)�IntervalTree�Interval)�SegmentTree�sum_operation)�Polygon)�PriorityQueue)�PrioritizedItemc                   �   � e Zd Zdeeef         dee         fd�Zd� Zd� Z	de
fd�Z	 deeeeef         d	efd
�Zdeeef         fd�Zdefd�ZdS )�
PlaneSweep�points�squaresc                 �Z   � d| _         || _        || _        d | _        d | _        g | _        d S �Nr   )�_PlaneSweep__output�_PlaneSweep__points�_PlaneSweep__squares�x_compressed�_PlaneSweep__sweepState�_PlaneSweep__events)�selfr   r   s      ��C:\Users/abuch/OneDrive/Bureaublad/School/Courses/Geometric Algorithms/Programming assigment/geometric_algorithms/plane_sweep\planesweep.py�__init__zPlaneSweep.__init__   s2   � ������� ��� ��� ��������    c                 ��   � | �                     �   �          t          | j        �  �        dk    rIt          j        | j        �  �        }|�n-| �                    |�  �         t          | j        �  �        dk    �I| j        S r   )�_PlaneSweep__getEvents�lenr   �heapq�heappop�_PlaneSweep__handleEventr   �r   �events     r   �sweepzPlaneSweep.sweep   sw   � ��������$�-� � �1�$�$��M�$�-�0�0�E��}�����u�%�%�%� �$�-� � �1�$�$� �}�r   c                 �z  � t          �   �         }| j        D ]E}|�                    �   �         \  }}}}|�                    |�  �         |�                    |�  �         �F| j        D ]}|�                    |d         �  �         �d� t          t          |�  �        �  �        D �   �         }| j        D ]�}|�                    �   �         \  }}}}	t          |d||         ||         f|�  �        }
t          j	        | j
        |
�  �         t          |	d||         ||         f|�  �        }
t          j	        | j
        |
�  �         ��| j        D ]A}t          |d         d||d                  f|�  �        }
t          j	        | j
        |
�  �         �Bt          dgt          |�  �        z  t          g��  �        | _        || _        d S )Nr   c                 �   � i | ]\  }}||��	S � r%   )�.0�i�xs      r   �
<dictcomp>z*PlaneSweep.__getEvents.<locals>.<dictcomp>=   s   � �D�D�D���A��1�D�D�Dr   �   �   )�
operations)�setr   �	getLimits�addr   �	enumerate�sortedr	   r   �heappushr   r   r   r   r   r   )r   �x_cords�square�xmin�xmax�_�pointr   �ymin�ymaxr!   s              r   �__getEventszPlaneSweep.__getEvents$   s�  � � �%�%���n� 	� 	�F�  &�/�/�1�1��D�$��1��K�K������K�K������ �]� 	"� 	"�E��K�K��a��!�!�!�!� E�D��6�'�?�?�)C�)C�D�D�D�� �n� 	1� 	1�F�%+�%5�%5�%7�%7�"�D�$��d� $�T�1�l�4�.@�,�t�BT�$U�W]�^�^�E��N�4�=�%�0�0�0� $�T�1�l�4�.@�,�t�BT�$U�W]�^�^�E��N�4�=�%�0�0�0�0� �]� 	1� 	1�E�#�U�1�X�q�,�u�Q�x�2H�$I�5�Q�Q�E��N�4�=�%�0�0�0�0� (���c�,�.?�.?�(?�]�O�\�\�\���(����r   r!   c                 ��   � t          |j        �  �        t          k    r"| �                    |j        |j        �  �         d S | �                    |j        |j        �  �         d S �N)�type�itemr   �_PlaneSweep__handleSquareEvent�priority�_PlaneSweep__handlePointEventr    s     r   �__handleEventzPlaneSweep.__handleEvent]   sW   � ���
���w�&�&��$�$�U�^�U�Z�@�@�@�@�@��#�#�E�N�E�J�?�?�?�?�?r   rA   r4   c                 �   � |\  }}}}|dk    }|r#| j         �                    |||j        �  �         d S | j         �                    |||j        �  �         d S r   )r   �	associate�id�
dissociate)r   rA   r4   r7   �tagr5   r6   �isEntrys           r   �__handleSquareEventzPlaneSweep.__handleSquareEventg   sl   � �%���3��d� ��(��� 	@���'�'��d�F�I�>�>�>�>�>� ��(�(��t�V�Y�?�?�?�?�?r   r8   c                 �X   � |\  }}}| xj         | �                    |�  �        z  c_         d S r=   )r   �_PlaneSweep__countIntervals)r   rA   r8   r7   r(   s        r   �__handlePointEventzPlaneSweep.__handlePointEventw   s1   � � ���1�a�����.�.�q�1�1�1����r   �xValuec                 �:   � | j         �                    |�  �        }|S r=   )r   �pointQuery2)r   rN   �ress      r   �__countIntervalszPlaneSweep.__countIntervals~   s   � ���+�+�F�3�3���
r   N)�__name__�
__module__�__qualname__�tuple�float�listr   r   r"   r   r	   r   �intr@   rB   rL   r%   r   r   r   r      s�   � � � � � ��u�U�E�\�2� �T�'�]� � � � �� � �3)� 3)� 3)�r@�?� @� @� @� @��@�E�%��e�U�2J�,K� @�U\� @� @� @� @� 2�%��u��2E� 2� 2� 2� 2��u� � � � � � r   r   )�math�intervaltree.intervaltreer   r   �segmenttree.segmenttreer   r   �geometry.Polygonr   �queuer   r   �priorityqueue.PrioritizedItemr	   r   r%   r   r   �<module>r`      s�   �� ���� <� <� <� <� <� <� <� <� >� >� >� >� >� >� >� >� %� $� $� $� $� $� � � � � � � ���� 9� 9� 9� 9� 9� 9�s� s� s� s� s� s� s� s� s� sr   PK     j�Yݨ�*�  �  &   __pycache__/planesweep.cpython-312.pyc�
    _eg�  �                   �P   � d dl Z d dlmZmZ d dlmZ d dlZd dlmZ  G d� d�      Z	y)�    N)�SegmentTree�sum_operation)�Polygon)�PrioritizedItemc                   �   � e Zd Zdeeef   dee   fd�Zd� Zd� Z	de
fd�Z	 deeeeef   d	efd
�Zdeeef   fd�Zdefd�Zy)�
PlaneSweep�points�squaresc                 �X   � d| _         || _        || _        d | _        d | _        g | _        y �Nr   )�_PlaneSweep__output�_PlaneSweep__points�_PlaneSweep__squares�x_compressed�_PlaneSweep__sweepState�_PlaneSweep__events)�selfr	   r
   s      ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\planesweep.py�__init__zPlaneSweep.__init__   s.   � ������� ��� ��� ������    c                 �  � | j                  �        t        | j                  �      dkD  rXt        j                  | j                  �      }|�	 | j                  S | j                  |�       t        | j                  �      dkD  r�X| j                  S r   )�_PlaneSweep__getEvents�lenr   �heapq�heappop�_PlaneSweep__handleEventr   �r   �events     r   �sweepzPlaneSweep.sweep   st   � ������$�-�-� �1�$��M�M�$�-�-�0�E��}�� �}�}�� ���u�%� �$�-�-� �1�$� �}�}�r   c                 �X  � t        �       }| j                  D ]9  }|j                  �       \  }}}}|j                  |�       |j                  |�       �; | j                  D ]  }|j                  |d   �       � t        t        |�      �      D ��ci c]  \  }}||��
 }	}}| j                  D ]�  }|j                  �       \  }}}
}t        |
d|	|   |	|   f|�      }t        j                  | j                  |�       t        |d|	|   |	|   f|�      }t        j                  | j                  |�       �� | j                  D ]:  }t        |d   d|	|d      f|�      }t        j                  | j                  |�       �< t        dgt        |	�      z  t        g��      | _        |	| _        y c c}}w )Nr   �   �   )�
operations)�setr   �	getLimits�addr   �	enumerate�sortedr   r   �heappushr   r   r   r   r   r   )r   �x_cords�square�xmin�xmax�_�point�i�xr   �ymin�ymaxr   s                r   �__getEventszPlaneSweep.__getEvents!   s�  � � �%���n�n�F�  &�/�/�1��D�$��1��K�K����K�K��� %� �]�]�E��K�K��a��!� #� *3�6�'�?�)C�D�)C���A��1��)C��D� �n�n�F�%+�%5�%5�%7�"�D�$��d� $�T�1�l�4�.@�,�t�BT�$U�W]�^�E��N�N�4�=�=�%�0� $�T�1�l�4�.@�,�t�BT�$U�W]�^�E��N�N�4�=�=�%�0� %� �]�]�E�#�U�1�X�q�,�u�Q�x�2H�$I�5�Q�E��N�N�4�=�=�%�0� #� (���c�,�.?�(?�]�O�\���(����5 Es   �F&r   c                 ��   � t        |j                  �      t        k(  r'| j                  |j                  |j                  �       y | j                  |j                  |j                  �       y �N)�type�itemr   �_PlaneSweep__handleSquareEvent�priority�_PlaneSweep__handlePointEventr   s     r   �__handleEventzPlaneSweep.__handleEventZ   sC   � ���
�
��w�&��$�$�U�^�^�U�Z�Z�@��#�#�E�N�N�E�J�J�?r   r:   r+   c                 �   � |\  }}}}|dk(  }|r(| j                   j                  |||j                  �       y | j                   j                  |||j                  �       y r   )r   �	associate�id�
dissociate)r   r:   r+   r.   �tagr,   r-   �isEntrys           r   �__handleSquareEventzPlaneSweep.__handleSquareEventd   sX   � �%���3��d� ��(������'�'��d�F�I�I�>� ���(�(��t�V�Y�Y�?r   r/   c                 �X   � |\  }}}| xj                   | j                  |�      z  c_         y r6   )r   �_PlaneSweep__countIntervals)r   r:   r/   r.   r1   s        r   �__handlePointEventzPlaneSweep.__handlePointEventt   s(   � � ���1�a�����.�.�q�1�1�r   �xValuec                 �<   � | j                   j                  |�      }|S r6   )r   �pointQuery2)r   rG   �ress      r   �__countIntervalszPlaneSweep.__countIntervals{   s   � ����+�+�F�3���
r   N)�__name__�
__module__�__qualname__�tuple�float�listr   r   r   r   r   r   �intr9   r;   rE   � r   r   r   r   
   s�   � ��u�U�E�\�2� �T�'�]� ��3)�r@�?� @��@�E�%��e�U�2J�,K� @�U\� @� 2�%��u��2E� 2��u� r   r   )
�math�segmenttree.segmenttreer   r   �geometry.Polygonr   r   �priorityqueue.PrioritizedItemr   r   rS   r   r   �<module>rX      s    �� � >� $� � 9�s� sr   PK     zV�Y�p$tc  c  &   __pycache__/planesweep.cpython-313.pyc�
    ��ag   �                   �l   � S SK r S SKJrJr  S SKJrJr  S SKJr  S SK	J
r
  S SKrS SKJr   " S S5      rg)	�    N)�IntervalTree�Interval)�SegmentTree�sum_operation)�Polygon)�PriorityQueue)�PrioritizedItemc                   �   � \ rS rSrS\\\4   S\\   4S jrS r	S r
S\4S jr S	\\\\\4   S
\4S jrS\\\4   4S jrS rS\4S jrSrg)�
PlaneSweep�   �points�squaresc                 �T   � SU l         Xl        X l        S U l        S U l        / U l        g �Nr   )�_PlaneSweep__output�_PlaneSweep__points�_PlaneSweep__squares�x_compressed�_PlaneSweep__sweepState�_PlaneSweep__events)�selfr   r   s      �aC:\Users\abuch\Desktop\School\Geometric algorithms\geometric_algorithms\plane_sweep\planesweep.py�__init__�PlaneSweep.__init__   s*   � ������ �� ��� ������    c                 �$  � U R                  5         [        U R                  5      S:�  a\  [        R                  " U R                  5      nUc   U R                  $ U R                  U5        [        U R                  5      S:�  a  M\  U R                  $ r   )�_PlaneSweep__getEvents�lenr   �heapq�heappop�_PlaneSweep__handleEventr   �r   �events     r   �sweep�PlaneSweep.sweep   st   � ������$�-�-� �1�$��M�M�$�-�-�0�E��}�� �}�}�� ���u�%� �$�-�-� �1�$� �}�}�r   c                 �V  � [        5       nU R                   H9  nUR                  5       u  p4  nUR                  U5        UR                  U5        M;     U R                   H  nUR                  US   5        M     [        [        U5      5       VVs0 sH  u  pxX�_M	     n	nnU R                   H�  nUR                  5       u  p4p�[        U
SX�   X�   4U5      n[        R                  " U R                  U5        [        USX�   X�   4U5      n[        R                  " U R                  U5        M�     U R                   H;  n[        US   SX�S      4U5      n[        R                  " U R                  U5        M=     [        S/[        U	5      -  [        /S9U l        X�l        g s  snnf )Nr   �   �   )�
operations)�setr   �	getLimits�addr   �	enumerate�sortedr	   r   �heappushr   r   r   r   r   r   )r   �x_cords�square�xmin�xmax�_�point�i�xr   �ymin�ymaxr#   s                r   �__getEvents�PlaneSweep.__getEvents$   s{  � � �%���n�n�F�  &�/�/�1��D��1��K�K����K�K��� %� �]�]�E��K�K��a��!� #� *3�6�'�?�)C�D�)C�����)C��D� �n�n�F�%+�%5�%5�%7�"�D�� $�T�1�l�.@�,�BT�$U�W]�^�E��N�N�4�=�=�%�0� $�T�1�l�.@�,�BT�$U�W]�^�E��N�N�4�=�=�%�0� %� �]�]�E�#�U�1�X�q�,�Q�x�2H�$I�5�Q�E��N�N�4�=�=�%�0� #�
 (���c�,�.?�(?�]�O�\���(���) Es   �F%r#   c                 ��   � [        UR                  5      [        :X  a'  U R                  UR                  UR                  5        g U R                  UR                  UR                  5        g �N)�type�itemr   �_PlaneSweep__handleSquareEvent�priority�_PlaneSweep__handlePointEventr"   s     r   �__handleEvent�PlaneSweep.__handleEventU   sC   � ���
�
��w�&��$�$�U�^�^�U�Z�Z�@��#�#�E�N�N�E�J�J�?r   rA   r1   c                 ��   � Uu  p4pVUS:X  a  SOSnU(       a(  [        S5        U R                  R                  XVS5        g [        S5        U R                  R                  XVS5        g )Nr   TFzentry eventr(   z
exit event)�printr   �update_range)r   rA   r1   r4   �tagr2   r3   �isEntrys           r   �__handleSquareEvent�PlaneSweep.__handleSquareEvent_   sZ   � �%���� �!�8�$�%����-� ����*�*�4�q�9��,�����*�*�4�q�9r   r5   c                 �l   � [        S5        Uu    p4U =R                  U R                  U5      -  sl        g )Nzpoint event)rF   r   �_PlaneSweep__countIntervals)r   rA   r5   r4   r7   s        r   �__handlePointEvent�PlaneSweep.__handlePointEvento   s.   � � 	�m�����1�����.�.�q�1�1�r   c                 �   � g r=   � )r   s    r   �__findNewEvent�PlaneSweep.__findNewEventv   s   � �r   �xValuec                 �F   � U R                   R                  XS5      nUc  gU$ )N�sumr   )r   �query)r   rT   �ress      r   �__countIntervals�PlaneSweep.__countIntervals{   s)   � � ���%�%�f�e�<���;���
r   )�__events�__output�__points�	__squares�__sweepStater   N)�__name__�
__module__�__qualname__�__firstlineno__�tuple�float�listr   r   r$   r   r	   r!   �intr@   rB   �_PlaneSweep__findNewEventrM   �__static_attributes__rQ   r   r   r   r      s�   � ��u�U�E�\�2� �T�'�]� ��-)�b@�?� @��:�E�%��e�U�2J�,K� :�U\� :� 2�%��u��2E� 2��
�u� r   r   )�math�intervaltree.intervaltreer   r   �segmenttree.segmenttreer   r   �geometry.Polygonr   �queuer   r   �priorityqueue.PrioritizedItemr	   r   rQ   r   r   �<module>rp      s(   �� � <� >� %� � � 9�z� zr   PK     )h�Y            	   geometry/PK     ֋�Y               geometry/__pycache__/PK     ֋�Y��4�k  k  ,   geometry/__pycache__/Polygon.cpython-311.pyc�
    �Zagk  �                   �    �  G d � d�  �        Z dS )c                   �0   � e Zd Zdedefd�Zdefd�Zd� ZdS )�Polygon�args�idc                 �"   � || _         || _        d S �N)�limsr   )�selfr   r   s      ��C:\Users/abuch/OneDrive/Bureaublad/School/Courses/Geometric Algorithms/Programming assigment/geometric_algorithms/plane_sweep\geometry\Polygon.py�__init__zPolygon.__init__   s   � ���	������    �clockWiseIndexc                 �   � | j         \  }}}}|dk    r||fS |dk    r||fS |dk    r||fS |dk    r||fS t          d�  �        �)N�    �   �   �   z clockWiseIndex must be in [0, 3])r   �
ValueError)r	   r   �xmin�xmax�ymin�ymaxs         r
   �getPointzPolygon.getPoint   su   � �!%����d�D�$��Q����$�<���q� � ��$�<���q� � ��$�<���q� � ��$�<���?�@�@�@r   c                 �   � | j         S r   )r   )r	   s    r
   �	getLimitszPolygon.getLimits   s
   � ��y�r   N)�__name__�
__module__�__qualname__�list�intr   r   r   � r   r
   r   r      se   � � � � � ��T� �s� � � � �A�s� A� A� A� A�� � � � r   r   N)r   r    r   r
   �<module>r!      s7   ��� � � � � � � � � r   PK     �`�Y':�p�  �  ,   geometry/__pycache__/Polygon.cpython-312.pyc�
    �Zagk  �                   �   �  G d � d�      Z y)c                   �.   � e Zd Zdedefd�Zdefd�Zd� Zy)�Polygon�args�idc                 �    � || _         || _        y �N)�limsr   )�selfr   r   s      ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\geometry\Polygon.py�__init__zPolygon.__init__   s   � ���	����    �clockWiseIndexc                 �   � | j                   \  }}}}|dk(  r||fS |dk(  r||fS |dk(  r||fS |dk(  r||fS t        d�      �)N�    �   �   �   z clockWiseIndex must be in [0, 3])r   �
ValueError)r	   r   �xmin�xmax�ymin�ymaxs         r
   �getPointzPolygon.getPoint   sh   � �!%�����d�D�$��Q���$�<���q� ��$�<���q� ��$�<���q� ��$�<���?�@�@r   c                 �   � | j                   S r   )r   )r	   s    r
   �	getLimitszPolygon.getLimits   s   � ��y�y�r   N)�__name__�
__module__�__qualname__�list�intr   r   r   � r   r
   r   r      s(   � ��T� �s� �A�s� A�r   r   N)r   r    r   r
   �<module>r!      s   ��� r   PK     zV�Y��j�  �  ,   geometry/__pycache__/Polygon.cpython-313.pyc�
    �agk  �                   �   �  " S  S5      r g)c                   �:   � \ rS rSrS\S\4S jrS\4S jrS rSr	g	)
�Polygon�   �args�idc                 �   � Xl         X l        g �N)�limsr   )�selfr   r   s      �gC:\Users\abuch\Desktop\School\Geometric algorithms\geometric_algorithms\plane_sweep\geometry\Polygon.py�__init__�Polygon.__init__   s   � ��	���    �clockWiseIndexc                 �~   � U R                   u  p#pEUS:X  a  X$4$ US:X  a  X44$ US:X  a  X54$ US:X  a  X%4$ [        S5      e)N�    r   �   �   z clockWiseIndex must be in [0, 3])r	   �
ValueError)r
   r   �xmin�xmax�ymin�ymaxs         r   �getPoint�Polygon.getPoint   s\   � �!%�����D��Q���<���q� ��<���q� ��<���q� ��<���?�@�@r   c                 �   � U R                   $ r   )r	   )r
   s    r   �	getLimits�Polygon.getLimits   s   � ��y�y�r   )r   r	   N)
�__name__�
__module__�__qualname__�__firstlineno__�list�intr   r   r   �__static_attributes__� r   r   r   r      s(   � ��T� �s� �A�s� A�r   r   N)r   r%   r   r   �<module>r&      s   ��� r   PK     �`�YX�]k  k     geometry/Polygon.pyclass Polygon():
    def __init__(self, args: list, id: int):
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
        return self.limsPK     �i�Y�$?؅  �     planesweep.pyimport math

from segmenttree.segmenttree import SegmentTree, sum_operation

from geometry.Polygon import Polygon
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
            # event = PrioritizedItem((ymin, 0, xmin, xmax), square)
            heapq.heappush(self.__events, event)
            
            # exit boundary
            event = PrioritizedItem((ymax, 2, x_compressed[xmin], x_compressed[xmax]), square)
            # event = PrioritizedItem((ymax, 2, xmin, xmax), square)
            heapq.heappush(self.__events, event)
            
            
        for point in self.__points: 
            event = PrioritizedItem((point[1], 1, x_compressed[point[0]]), point)
            # event = PrioritizedItem((point[1], 1, point[0]), point)
            heapq.heappush(self.__events, event)
            
            
        # self.__sweepState = SegmentTree([0] * len(x_cords), operations=[sum_operation])
        self.__sweepState = SegmentTree([0] * len(x_compressed), operations=[sum_operation])           
        
        self.x_compressed = x_compressed
        
        # print(f"compressed cords: {x_compressed}")
    
    
    
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
        
        isEntry = tag == 0

        if isEntry:
            # print(f"entry event x:{xmin} - {xmax}, square {square.id}")
            self.__sweepState.associate(xmin, xmax, square.id)          
        else:
            # print(f"exit event x: {xmin} - {xmax}, square {square.id}")
            self.__sweepState.dissociate(xmin, xmax, square.id)  
    
    def __handlePointEvent(self, priority, point: tuple[float, float]):
        # check how many intervals of the sweep state this point is in
        # then update the output
        _, _, x = priority
        # print(f"point event x: {point}")
        self.__output += self.__countIntervals(x)
    
    def __countIntervals(self, xValue: float):
        res = self.__sweepState.pointQuery2(xValue)
        return res
        # print(f"for {xValue}: {res}")
        # res = self.__sweepState.pointQuery(xValue)
        # return len(res) if res is not None else None
PK     �j�Y               priorityqueue/PK     ֋�Y               priorityqueue/__pycache__/PK     ֋�Y[��  �  9   priorityqueue/__pycache__/PrioritizedItem.cpython-311.pyc�
    �F\g�   �                   �`   � d dl mZmZ d dlmZ  ed��  �         G d� d�  �        �   �         ZdS )�    )�	dataclass�field)�AnyT)�orderc                   �N   � e Zd ZU eeeef         ed<    ed��  �        Ze	ed<   dS )�PrioritizedItem�priorityF)�compare�itemN)
�__name__�
__module__�__qualname__�tuple�float�int�__annotations__r   r   r   � �    ��C:\Users/abuch/OneDrive/Bureaublad/School/Courses/Geometric Algorithms/Programming assigment/geometric_algorithms/plane_sweep\priorityqueue\PrioritizedItem.pyr   r      sG   � � � � � � ��E�5�#�%�&�&�&�&��e�E�"�"�"�D�#�"�"�"�"�"r   r   N)�dataclassesr   r   �typingr   r   r   r   r   �<module>r      sy   �� (� (� (� (� (� (� (� (� � � � � � �
������#� #� #� #� #� #� #� ��#� #� #r   PK     �|�Y[݁��  �  9   priorityqueue/__pycache__/PrioritizedItem.cpython-312.pyc�
    �F\g�   �                   �L   � d dl mZmZ d dlmZ  ed��       G d� d�      �       Zy)�    )�	dataclass�field)�AnyT)�orderc                   �@   � e Zd ZU eeeef   ed<    ed��      Ze	ed<   y)�PrioritizedItem�priorityF)�compare�itemN)
�__name__�
__module__�__qualname__�tuple�float�int�__annotations__r   r   r   � �    ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\priorityqueue\PrioritizedItem.pyr   r      s#   � ��E�5�#�%�&�&��E�"�D�#�"r   r   N)�dataclassesr   r   �typingr   r   r   r   r   �<module>r      s'   �� (� �
���#� #� �#r   PK     zV�Y��c��  �  9   priorityqueue/__pycache__/PrioritizedItem.cpython-313.pyc�
    �ag�   �                   �F   � S SK JrJr  S SKJr  \" SS9 " S S5      5       rg)�    )�	dataclass�field)�AnyT)�orderc                   �B   � \ rS rSr% \\\\4   \S'   \" SS9r	\
\S'   Srg)�PrioritizedItem�   �priorityF)�compare�item� N)�__name__�
__module__�__qualname__�__firstlineno__�tuple�float�int�__annotations__r   r   r   �__static_attributes__r   �    �tC:\Users\abuch\Desktop\School\Geometric algorithms\geometric_algorithms\plane_sweep\priorityqueue\PrioritizedItem.pyr   r      s#   � ��E�5�#�%�&�&��E�"�D�#�"r   r   N)�dataclassesr   r   �typingr   r   r   r   r   �<module>r      s'   �� (� �
���#� #� �#r   PK     �|�Yϸn�   �       priorityqueue/PrioritizedItem.pyfrom dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: tuple[float, float, int]
    item: Any=field(compare=False)
    
    
PK     =i�Y               segmenttree/PK     }l�Y               segmenttree/__pycache__/PK     ֋�Y�����7  �7  3   segmenttree/__pycache__/segmenttree.cpython-311.pyc�
    3@dg;'  �                   ��   �  G d � d�  �        Z d� Zd� Zd� Zd� Z e deed�  �        Z e deed�  �        Z e d	e	ed
�  �        Z
 e deed�  �        Z G d� d�  �        Z G d� d�  �        ZdS )c                   �   � e Zd Zdd�ZdS )�	Operation�    c                 �0   � || _         || _        || _        d S �N)�name�f�
f_on_equal)�selfr   �function�function_on_equal�neutral_values        ��C:\Users/abuch/OneDrive/Bureaublad/School/Courses/Geometric Algorithms/Programming assigment/geometric_algorithms/plane_sweep\segmenttree\segmenttree.py�__init__zOperation.__init__   s   � ���	����+�����    N)r   )�__name__�
__module__�__qualname__r   � r   r   r   r      s(   � � � � � �,� ,� ,� ,� ,� ,r   r   c                 �   � | |z  S r   r   ��x�counts     r   �add_multipler      s   � ��u�9�r   c                 �   � | S r   r   r   s     r   �min_multipler      �   � ��Hr   c                 �   � | S r   r   r   s     r   �max_multipler      r   r   c                 �&   � t          | �  �        |z  S r   )�lenr   s     r   �count_multipler!      s   � ��q�6�6�E�>�r   r   r   �sum�ming    e��A�maxg    e���c                   �j   � e Zd ZdZeeegfd�Zd� Zdd�Z	dd�Z
d� Z	 d	� Z	 dd
�Zdd�Zd� Zd� Zd� ZdS )�SegmentTreez
    SegmentTree class. Handles an underlying array as well as available
    operations and pointer to the root of a tree.
    c                 ��   � || _         t          |�  �        t          k    rt          d�  �        �i | _        |D ]}|| j        |j        <   �t          dt          |�  �        dz
  | �  �        | _        dS )z�
        Builds a segment tree based on the provided `array`. Supports operations
        of class Operation provided in the operations array.
        zoperations must be a listr   �   N)	�array�type�list�	TypeError�
operationsr   �SegmentTreeNoder    �root)r
   r)   r-   �ops       r   r   zSegmentTree.__init__$   su   � � ��
��
���t�#�#��7�8�8�8����� 	*� 	*�B�')�D�O�B�G�$�$�#�A�s�5�z�z�A�~�t�<�<��	�	�	r   c                 �   � | j         �                    |�  �        dk    rt          d�  �        �| j        �                    ||| j         |         �  �        S )z|
        Returns the result of the operation execution with `operation_name`
        on the range from [start, end]
        NzThis operation is not available)r-   �get�	Exceptionr/   �_query)r
   �start�end�operation_names       r   �queryzSegmentTree.query5   sO   � �
 �?���~�.�.�$�6�6��=�>�>�>��y����s�D�O�N�,K�L�L�Lr   Nc                 �  �� |�| j         }��t          �   �         �t          |j        �  �        dk    r�fd�|j        D �   �          |j        s|j        rw|j        rM|j        j        d         |cxk    r|j        j        d         k    r n n| �                    ||j        ��  �         n#|j        r| �                    ||j        ��  �         �S )Nr   c                 �:   �� g | ]}��                     |�  �        ��S r   )�add)�.0r   �ress     �r   �
<listcomp>z*SegmentTree.pointQuery.<locals>.<listcomp>F   s#   �� �5�5�5�A�S�W�W�Q�Z�Z�5�5�5r   r(   )r/   �setr    �true_intervals�left�right�range�
pointQuery)r
   �pointr/   r=   s      `r   rD   zSegmentTree.pointQuery?   s�   �� ��<��9�D��;��%�%�C��t�"�#�#�a�'�'�5�5�5�5��!4�5�5�5�5� �9� 	8��
� 	8��y� 8�T�Y�_�Q�/�5�N�N�N�N�D�I�O�A�<N�N�N�N�N�N�����t�y�#�6�6�6�6��� 8�����t�z�3�7�7�7��
r   r   c                 �P  � |�| j         }|t          |j        �  �        z  }|j        s|j        rw|j        rM|j        j        d         |cxk    r|j        j        d         k    r n n| �                    ||j        |�  �        }n#|j        r| �                    ||j        |�  �        }|S �Nr   r(   )r/   r    r@   rA   rB   rC   �pointQuery2)r
   rE   r/   �unique_counts       r   rH   zSegmentTree.pointQuery2Q   s�   � ��<��9�D� 	��D�/�0�0�0�� �9� 	Q��
� 	Q��y� Q�T�Y�_�Q�/�5�N�N�N�N�D�I�O�A�<N�N�N�N�N�N�#�/�/��t�y�,�O�O����� Q�#�/�/��t�z�<�P�P���r   c                 �   � | j         j        S )zS
        Prints the summary for the whole array (values in the root node).
        )r/   �values�r
   s    r   �summaryzSegmentTree.summaryd   s   � � �y��r   c                 �   � |\  }}|\  }}||k    r||k    s||k    r||k    rdS ||k    r||k    s||k    r||k    rdS dS )NTFr   )r
   �i1�i2�s1�e1�s2�e2s          r   �
__overlapszSegmentTree.__overlapst   se   � ����B����B��"�H�H��r���r�R�x�x�B�"�H�H��4��B�h�h�2��8�8��r���b�B�h�h��4��ur   c                 �  � |�| j         }|j        d         |k    r-|j        d         |k    r|j        �                    |�  �         d S |j        r?| �                    |j        j        ||f�  �        r| �                    ||||j        �  �         |j        rA| �                    |j        j        ||f�  �        r!| �                    ||||j        �  �         d S d S d S rG   )r/   rC   r@   r;   rA   �_SegmentTree__overlaps�	associaterB   �r
   r5   r6   �id�nodes        r   rX   zSegmentTree.associate�   s�   � ��<��9�D� �:�a�=�E�!�!�d�j��m�s�&:�&:���#�#�B�'�'�'�'�'� �y� :�T�_�_�T�Y�_�u�c�l�K�K� :����u�c�2�t�y�9�9�9��z� ;�d�o�o�d�j�.>����M�M� ;����u�c�2�t�z�:�:�:�:�:�;� ;� ;� ;r   c                 �  � |�| j         }|j        d         |k    r-|j        d         |k    r|j        �                    |�  �         d S |j        r?| �                    |j        j        ||f�  �        r| �                    ||||j        �  �         |j        rA| �                    |j        j        ||f�  �        r!| �                    ||||j        �  �         d S d S d S rG   )r/   rC   r@   �removerA   rW   �
dissociaterB   rY   s        r   r^   zSegmentTree.dissociate�   s�   � ��<��9�D��:�a�=�E�!�!�d�j��m�s�&:�&:���&�&�r�*�*�*�*�*� �y� ;�T�_�_�T�Y�_�u�c�l�K�K� ;�����s�B��	�:�:�:��z� <�d�o�o�d�j�.>����M�M� <�����s�B��
�;�;�;�;�;�<� <� <� <r   c                 �<   � | j         �                    ||�  �         dS )zF
        Updates an old value at `position` to a new `value`.
        N)r/   �_update�r
   �position�values      r   �updatezSegmentTree.update�   s"   � � 	�	���(�E�*�*�*�*�*r   c                 �>   � | j         �                    |||�  �         dS )z`
        Updates old values old in the range [start, end], inclusively, to a new value.
        N)r/   �_update_range�r
   r5   r6   rc   s       r   �update_rangezSegmentTree.update_range�   s$   � � 	�	����s�E�2�2�2�2�2r   c                 �4   � | j         �                    �   �         S r   )r/   �__repr__rL   s    r   rj   zSegmentTree.__repr__�   s   � ��y�!�!�#�#�#r   )NN)Nr   r   )r   r   r   �__doc__�sum_operation�min_operation�max_operationr   r8   rD   rH   rM   rW   rX   r^   rd   rh   rj   r   r   r   r&   r&      s�   � � � � � �� � +�M�=�I�=� =� =� =�"M� M� M�� � � �$� � � �& �  �  ��	� 	� 	��;� ;� ;� ;�<� <� <� <�+� +� +�3� 3� 3�$� $� $� $� $r   r&   c                   �<   � e Zd ZdZd� Zd� Zd� Zd� Zd� Zd� Z	d� Z
d	S )
r.   z�
    Internal SegmentTreeNode class represents a node of a segment tree. Each node
    stores the reference to the left and the right bound of a segment this
    node is responsible for.
    c                 �f  � ||f| _         || _        d | _        i | _        d | _        d | _        t          �   �         | _        ||k    r| �                    �   �          d S t          ||||z
  dz  z   |�  �        | _        t          |||z
  dz  z   dz   ||�  �        | _        | �                    �   �          d S )N�   r(   )
rC   �parent_tree�range_valuerK   rA   rB   r?   r@   �_syncr.   )r
   r5   r6   �segment_trees       r   r   zSegmentTreeNode.__init__�   s�   � ��S�\��
�'�����������	���
�!�e�e����C�<�<��J�J�L�L�L��F�#�E�5�C�%�K�A�3E�+E�$0�2� 2��	�$�U�c�E�k�a�-?�%?�!�%C�S�%1�3� 3��
��
�
�����r   c                 �  � || j         d         k     s|| j         d         k    rd S || j         d         k    r#| j         d         |k    r| j        |j                 S | �                    �   �          | j        r| j        �                    |||�  �        nd }| j        r| j        �                    |||�  �        nd }|�|S |�|S |�                    ||g�  �        S rG   )rC   rK   r   �_pushrA   r4   rB   r   )r
   r5   r6   �	operation�left_res�	right_ress         r   r4   zSegmentTreeNode._query�   s  � ����A����%�$�*�Q�-�"7�"7� �4��D�J�q�M�!�!�d�j��m�s�&:�&:� �;�y�~�.�.� 	�
�
����26�)�F�4�9�#�#�E�3�$-�/� /� /�AE� 	� 59�J�I�D�J�%�%�e�S�&/�1� 1� 1�DH� 	� �������O��{�{�H�i�0�1�1�1r   c                 �  � || j         d         k     s|| j         d         k    rd S || j         d         k    r6| j         d         |k    r%|| j        j        |<   | �                    �   �          d S | �                    �   �          | j        �                    ||�  �         | j        �                    ||�  �         | �                    �   �          d S rG   )rC   rr   r)   rt   rw   rA   r`   rB   ra   s      r   r`   zSegmentTreeNode._update�   s�   � ��d�j��m�#�#�x�$�*�Q�-�'?�'?��F��t�z�!�}�$�$���A��(�)B�)B�/4�D��"�8�,��J�J�L�L�L��F��
�
�����	���(�E�*�*�*��
���8�U�+�+�+��
�
�����r   c                 �  � || j         d         k     s|| j         d         k    rd S || j         d         k    r.| j         d         |k    r|| _        | �                    �   �          d S | �                    �   �          | j        �                    |||�  �         | j        �                    |||�  �         | �                    �   �          d S rG   )rC   rs   rt   rw   rA   rf   rB   rg   s       r   rf   zSegmentTreeNode._update_range�   s�   � ����A����%�$�*�Q�-�"7�"7��F��D�J�q�M�!�!�d�j��m�s�&:�&:�$�D���J�J�L�L�L��F��
�
�����	����s�E�2�2�2��
� � ���U�3�3�3��
�
�����r   c                 �  � | j         d         | j         d         k    rq| j        j        �                    �   �         D ]P}| j        j        | j         d                  }| j        �| j        }|�                    |g�  �        | j        |j        <   �Qd S | j        j        �                    �   �         D ]�}|�                    | j        j        |j                 | j	        j        |j                 g�  �        }| j        �9| j         d         | j         d         z
  dz   }|�
                    | j        |�  �        }|| j        |j        <   ��d S rG   )rC   rr   r-   rK   r)   rs   r   r   rA   rB   r	   )r
   r0   �current_value�result�bound_lengths        r   rt   zSegmentTreeNode._sync�   s7  � ��:�a�=�D�J�q�M�)�)��&�1�8�8�:�:� =� =�� $� 0� 6�t�z�!�}� E���#�/�$(�$4�M�')�t�t�]�O�'<�'<���B�G�$�$�	=� =� �&�1�8�8�:�:� .� .������Y�%�b�g�.��
�0A�"�'�0J�K�M� M���#�/�#'�:�a�=�4�:�a�=�#@�1�#D�L��]�]�4�+;�\�J�J�F�'-���B�G�$�$�.� .r   c                 ��   � | j         �d S | j        r]| j         | j        _         | j         | j        _         | j        �                    �   �          | j        �                    �   �          d | _         d S d S r   )rs   rA   rB   rt   rL   s    r   rw   zSegmentTreeNode._push	  sr   � ���#��F��9� 	$�$(�$4�D�I�!�%)�%5�D�J�"��I�O�O�����J������#�D����	$� 	$r   c                 �  � d�                     | j        d         | j        d         | j        | j        �  �        }| j        r|| j        �                    �   �         z  }| j        r|| j        �                    �   �         z  }|S )Nz({}, {}): {}, {}
r   r(   )�formatrC   rK   r@   rA   rj   rB   )r
   �anss     r   rj   zSegmentTreeNode.__repr__  s|   � �"�)�)�$�*�Q�-���A��&*�k�4�3F�H� H���9� 	(��4�9�%�%�'�'�'�C��:� 	)��4�:�&�&�(�(�(�C��
r   N)r   r   r   rk   r   r4   r`   rf   rt   rw   rj   r   r   r   r.   r.   �   s�   � � � � � �� �� � �&2� 2� 2�.
� 
� 
�
� 
� 
�.� .� .� $� $� $�� � � � r   r.   N)r   r   r   r   r!   r    �count_operationr"   rl   r#   rm   r$   rn   r&   r.   r   r   r   �<module>r�      s,  ��,� ,� ,� ,� ,� ,� ,� ,�� � �� � �� � �� � � �)�G�S�.�!�<�<���	�%��l�A�6�6���	�%��l�C�8�8���	�%��l�D�9�9��O$� O$� O$� O$� O$� O$� O$� O$�dj� j� j� j� j� j� j� j� j� jr   PK     }l�Y}ue�  �  3   segmenttree/__pycache__/segmenttree.cpython-312.pyc�
    �deg(  �                   �   �  G d � d�      Z d� Zd� Zd� Zd� Z e deed�      Z e deed�      Z e d	e	ed
�      Z
 e deed�      Z G d� d�      Z G d� d�      Zy)c                   �   � e Zd Zdd�Zy)�	Operationc                 �.   � || _         || _        || _        y �N)�name�f�
f_on_equal)�selfr   �function�function_on_equal�neutral_values        ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\segmenttree\segmenttree.py�__init__zOperation.__init__   s   � ���	����+���    N)�    )�__name__�
__module__�__qualname__r   � r   r   r   r      s   � �,r   r   c                 �   � | |z  S r   r   ��x�counts     r   �add_multipler      s   � ��u�9�r   c                 �   � | S r   r   r   s     r   �min_multipler      �   � ��Hr   c                 �   � | S r   r   r   s     r   �max_multipler      r   r   c                 �   � t        | �      |z  S r   )�lenr   s     r   �count_multipler!      s   � ��q�6�E�>�r   r   r   �sum�ming    e��A�maxg    e���c                   �V   � e Zd ZdZeeegfd�Zdd�Zdd�Z	d� Z
	 d� Z	 dd�Zdd	�Zd
� Zy)�SegmentTreez
    SegmentTree class. Handles an underlying array as well as available
    operations and pointer to the root of a tree.
    c                 �z   � t        |�      t        k7  rt        d�      �t        dt	        |�      dz
  | �      | _        y)z�
        Builds a segment tree based on the provided `array`. Supports operations
        of class Operation provided in the operations array.
        zoperations must be a listr   �   N)�type�list�	TypeError�SegmentTreeNoder    �root)r	   �array�
operationss      r   r   zSegmentTree.__init__$   s7   � � �
��t�#��7�8�8� $�A�s�5�z�A�~�t�<��	r   Nc                 �  � |�| j                   }|�
t        �       }t        |j                  �      dkD  r)|j                  D �cg c]  }|j	                  |�      �� c} |j
                  s|j                  r�|j
                  r[|j
                  j                  d   |cxk  r|j
                  j                  d   k  r"n n| j                  ||j
                  |�       |S |j                  r| j                  ||j                  |�       |S c c}w �Nr   r(   )	r-   �setr    �true_intervals�add�left�right�range�
pointQuery)r	   �pointr-   �resr   s        r   r8   zSegmentTree.pointQuery?   s�   � ��<��9�9�D��;��%�C��t�"�"�#�a�'�!%�!4�!4�5�!4�A�S�W�W�Q�Z�!4�5� �9�9��
�
��y�y�T�Y�Y�_�_�Q�/�5�N�D�I�I�O�O�A�<N�N�����t�y�y�#�6� �
� �������t�z�z�3�7��
�� 6s   �Dc                 �  � |�| j                   }|t        |j                  �      z  }|j                  s|j                  r�|j                  r[|j                  j
                  d   |cxk  r|j                  j
                  d   k  r"n n| j                  ||j                  |�      }|S |j                  r| j                  ||j                  |�      }|S r1   )r-   r    r3   r5   r6   r7   �pointQuery2)r	   r9   r-   �unique_counts       r   r<   zSegmentTree.pointQuery2Q   s�   � ��<��9�9�D� 	��D�/�/�0�0�� �9�9��
�
��y�y�T�Y�Y�_�_�Q�/�5�N�D�I�I�O�O�A�<N�N�#�/�/��t�y�y�,�O�� �� ���#�/�/��t�z�z�<�P���r   c                 �.   � | j                   j                  S )zS
        Prints the summary for the whole array (values in the root node).
        )r-   �values�r	   s    r   �summaryzSegmentTree.summaryd   s   � � �y�y���r   c                 �l   � |\  }}|\  }}||k  r||k\  s
||k  r||k\  ry||k  r||k\  s
||k  r||k\  ryy)NTFr   )r	   �i1�i2�s1�e1�s2�e2s          r   �
__overlapszSegmentTree.__overlapst   sO   � ����B����B��"�H��r��r�R�x�B�"�H���B�h�2��8��r��b�B�h��r   c                 ��  � |�| j                   }|j                  d   |k\  r.|j                  d   |k  r|j                  j                  |�       y |j                  rF| j                  |j                  j                  ||f�      r| j                  ||||j                  �       |j                  rH| j                  |j                  j                  ||f�      r| j                  ||||j                  �       y y y r1   )r-   r7   r3   r4   r5   �_SegmentTree__overlaps�	associater6   �r	   �start�end�id�nodes        r   rL   zSegmentTree.associate�   s�   � ��<��9�9�D� �:�:�a�=�E�!�d�j�j��m�s�&:����#�#�B�'� �y�y�T�_�_�T�Y�Y�_�_�u�c�l�K����u�c�2�t�y�y�9��z�z�d�o�o�d�j�j�.>�.>����M����u�c�2�t�z�z�:� N�zr   c                 ��  � |�| j                   }|j                  d   |k\  r.|j                  d   |k  r|j                  j                  |�       y |j                  rF| j                  |j                  j                  ||f�      r| j                  ||||j                  �       |j                  rH| j                  |j                  j                  ||f�      r| j                  ||||j                  �       y y y r1   )r-   r7   r3   �remover5   rK   �
dissociater6   rM   s        r   rT   zSegmentTree.dissociate�   s�   � ��<��9�9�D��:�:�a�=�E�!�d�j�j��m�s�&:����&�&�r�*� �y�y�T�_�_�T�Y�Y�_�_�u�c�l�K�����s�B��	�	�:��z�z�d�o�o�d�j�j�.>�.>����M�����s�B��
�
�;� N�zr   c                 �6   � | j                   j                  �       S r   )r-   �__repr__r@   s    r   rV   zSegmentTree.__repr__�   s   � ��y�y�!�!�#�#r   )NN)Nr   r   )r   r   r   �__doc__�sum_operation�min_operation�max_operationr   r8   r<   rA   rK   rL   rT   rV   r   r   r   r&   r&      sE   � �� +�M�=�I�=�6�$�& ��	��;�<�6$r   r&   c                   �   � e Zd ZdZd� Zy)r,   z�
    Internal SegmentTreeNode class represents a node of a segment tree. Each node
    stores the reference to the left and the right bound of a segment this
    node is responsible for.
    c                 ��   � ||f| _         || _        d | _        d | _        d | _        t        �       | _        ||k(  ry t        ||||z
  dz  z   |�      | _        t        |||z
  dz  z   dz   ||�      | _        y )N�   r(   )r7   �parent_tree�range_valuer5   r6   r2   r3   r,   )r	   rN   rO   �segment_trees       r   r   zSegmentTreeNode.__init__�   s�   � ��S�\��
�'��������	���
�!�e����C�<��#�E�5�C�%�K�A�3E�+E�$0�2��	�$�U�c�E�k�a�-?�%?�!�%C�S�%1�3��
r   N)r   r   r   rW   r   r   r   r   r,   r,   �   s   � ��3r   r,   N)r   r   r   r   r!   r    �count_operationr"   rX   r#   rY   r$   rZ   r&   r,   r   r   r   �<module>rb      s|   ��,� ,����� �G�S�.�!�<���%��l�A�6���%��l�C�8���%��l�D�9��O$� O$�d3� 3r   PK     zV�Y�p�r1&  1&  3   segmenttree/__pycache__/segmenttree.cpython-313.pyc�
    �ag�  �                   �   �  " S  S5      r S rS rS r\ " S\\S5      r\ " S\\S5      r\ " S	\\S
5      r	 " S S5      r
 " S S5      rg)c                   �   � \ rS rSrSS jrSrg)�	Operation�   c                 �(   � Xl         X l        X0l        g �N)�name�f�
f_on_equal)�selfr   �function�function_on_equal�neutral_values        �nC:\Users\abuch\Desktop\School\Geometric algorithms\geometric_algorithms\plane_sweep\segmenttree\segmenttree.py�__init__�Operation.__init__   s   � ��	���+��    )r   r	   r   N)�    )�__name__�
__module__�__qualname__�__firstlineno__r   �__static_attributes__� r   r   r   r      s   � �,r   r   c                 �
   � X-  $ r   r   ��x�counts     r   �add_multipler      s
   � ��9�r   c                 �   � U $ r   r   r   s     r   �min_multipler      �   � ��Hr   c                 �   � U $ r   r   r   s     r   �max_multipler"      r    r   �sumr   �ming    e��A�maxg    e���c                   �H   � \ rS rSrSr\\\/4S jrS r	S r
S rS rS rS	rg
)�SegmentTree�   zs
SegmentTree class. Handles an underlying array as well as available
operations and pointer to the root of a tree.
c                 ��   � Xl         [        U5      [        :w  a  [        S5      e0 U l        U H  nX0R                  UR
                  '   M     [        S[        U5      S-
  U 5      U l        g)z
Builds a segment tree based on the provided `array`. Supports operations
of class Operation provided in the operations array.
zoperations must be a listr   r   N)	�array�type�list�	TypeError�
operationsr   �SegmentTreeNode�len�root)r
   r*   r.   �ops       r   r   �SegmentTree.__init__   s[   � � �
��
��t�#��7�8�8�����B�')�O�O�B�G�G�$� �#�A�s�5�z�A�~�t�<��	r   c                 �   � U R                   R                  U5      S:X  a  [        S5      eU R                  R	                  XU R                   U   5      $ )zd
Returns the result of the operation execution with `operation_name`
on the range from [start, end]
NzThis operation is not available)r.   �get�	Exceptionr1   �_query)r
   �start�end�operation_names       r   �query�SegmentTree.query.   sG   � �
 �?�?���~�.�$�6��=�>�>��y�y����D�O�O�N�,K�L�Lr   c                 �.   � U R                   R                  $ )zC
Prints the summary for the whole array (values in the root node).
)r1   �values�r
   s    r   �summary�SegmentTree.summary7   s   � � �y�y���r   c                 �:   � U R                   R                  X5        g)z6
Updates an old value at `position` to a new `value`.
N)r1   �_update�r
   �position�values      r   �update�SegmentTree.update=   s   � � 	�	�	���(�*r   c                 �<   � U R                   R                  XU5        g)zP
Updates old values old in the range [start, end], inclusively, to a new value.
N)r1   �_update_range�r
   r8   r9   rF   s       r   �update_range�SegmentTree.update_rangeC   s   � � 	�	�	����E�2r   c                 �6   � U R                   R                  5       $ r   )r1   �__repr__r?   s    r   rO   �SegmentTree.__repr__I   s   � ��y�y�!�!�#�#r   )r*   r.   r1   N)r   r   r   r   �__doc__�sum_operation�min_operation�max_operationr   r;   r@   rG   rL   rO   r   r   r   r   r'   r'      s2   � �� +�M�=�I�=�M� �+�3�$r   r'   c                   �B   � \ rS rSrSrS rS rS rS rS r	S r
S	 rS
rg)r/   �M   z�
Internal SegmentTreeNode class represents a node of a segment tree. Each node
stores the reference to the left and the right bound of a segment this
node is responsible for.
c                 �  � X4U l         X0l        S U l        0 U l        S U l        S U l        X:X  a  U R                  5         g [        XX!-
  S-  -   U5      U l        [        XU-
  S-  -   S-   UU5      U l        U R                  5         g )N�   r   )�range�parent_tree�range_valuer>   �left�right�_syncr/   )r
   r8   r9   �segment_trees       r   r   �SegmentTreeNode.__init__T   s�   � ��\��
�'����������	���
��<��J�J�L��#�E�C�K�A�3E�+E�$0�2��	�$�U�E�k�a�-?�%?�!�%C�S�%1�3��
��
�
�r   c                 �6  � X R                   S   :  d  XR                   S   :�  a.  [        X4 SU R                   S   U R                   S   4 35        g XR                   S   ::  a,  U R                   S   U::  a  U R                  UR                     $ U R	                  5         U R
                  (       a  U R
                  R                  XU5      OS nU R                  (       a  U R                  R                  XU5      OS nUc  U$ Uc  U$ UR                  XE/5      $ )Nr   r   z out of range )	rY   �printr>   r   �_pushr\   r7   r]   r   )r
   r8   r9   �	operation�left_res�	right_ress         r   r7   �SegmentTreeNode._queryd   s�   � ����A���%�*�*�Q�-�"7��U�Z�L��t�z�z�!�}�d�j�j��m�/K�.L�M�N���J�J�q�M�!�d�j�j��m�s�&:��;�;�y�~�~�.�.��
�
��26�)�)� �9�9�#�#�E�$-�/�AE� 	� 59�J�J� �J�J�%�%�e�&/�1�DH� 	��������O��{�{�H�0�1�1r   c                 �  � XR                   S   :  d  XR                   S   :�  a  g XR                   S   :X  a<  U R                   S   U:X  a)  X R                  R                  U'   U R                  5         g U R	                  5         U R
                  R                  X5        U R                  R                  X5        U R                  5         g �Nr   r   )rY   rZ   r*   r^   rc   r\   rC   r]   rD   s      r   rC   �SegmentTreeNode._updateu   s�   � ��j�j��m�#�x�*�*�Q�-�'?���z�z�!�}�$����A��(�)B�/4���"�"�8�,��J�J�L���
�
���	�	���(�*��
�
���8�+��
�
�r   c                 �v  � X R                   S   :  d  XR                   S   :�  a  g XR                   S   ::  a*  U R                   S   U::  a  X0l        U R                  5         g U R                  5         U R                  R                  XU5        U R                  R                  XU5        U R                  5         g ri   )rY   r[   r^   rc   r\   rJ   r]   rK   s       r   rJ   �SegmentTreeNode._update_range�   s�   � ����A���%�*�*�Q�-�"7���J�J�q�M�!�d�j�j��m�s�&:�$���J�J�L���
�
���	�	����E�2��
�
� � ��U�3��
�
�r   c                 �2  � U R                   S   U R                   S   :X  a�  U R                  R                  R                  5        Hk  nU R                  R                  U R                   S      nU R
                  b  U R
                  nUR                  U/5      U R                  UR                  '   Mm     g U R                  R                  R                  5        H�  nUR                  U R                  R                  UR                     U R                  R                  UR                     /5      nU R
                  b>  U R                   S   U R                   S   -
  S-   nUR                  U R
                  U5      nX0R                  UR                  '   M�     g ri   )rY   rZ   r.   r>   r*   r[   r   r   r\   r]   r	   )r
   r2   �current_value�result�bound_lengths        r   r^   �SegmentTreeNode._sync�   s:  � ��:�:�a�=�D�J�J�q�M�)��&�&�1�1�8�8�:�� $� 0� 0� 6� 6�t�z�z�!�}� E���#�#�/�$(�$4�$4�M�')�t�t�]�O�'<����B�G�G�$�	 ;� �&�&�1�1�8�8�:������Y�Y�%�%�b�g�g�.��
�
�0A�0A�"�'�'�0J�K�M���#�#�/�#'�:�:�a�=�4�:�:�a�=�#@�1�#D�L��]�]�4�+;�+;�\�J�F�'-���B�G�G�$� ;r   c                 �&  � U R                   c  g U R                  (       ar  U R                   U R                  l         U R                   U R                  l         U R                  R                  5         U R                  R                  5         S U l         g g r   )r[   r\   r]   r^   r?   s    r   rc   �SegmentTreeNode._push�   sg   � ����#���9�9�$(�$4�$4�D�I�I�!�%)�%5�%5�D�J�J�"��I�I�O�O���J�J����#�D�� r   c                 �(  � SR                  U R                  S   U R                  S   U R                  5      nU R                  (       a  XR                  R	                  5       -  nU R
                  (       a  XR
                  R	                  5       -  nU$ )Nz({}, {}): {}
r   r   )�formatrY   r>   r\   rO   r]   )r
   �anss     r   rO   �SegmentTreeNode.__repr__�   sj   � ��%�%�d�j�j��m�T�Z�Z��]�&*�k�k�3���9�9��9�9�%�%�'�'�C��:�:��:�:�&�&�(�(�C��
r   )r\   rZ   rY   r[   r]   r>   N)r   r   r   r   rQ   r   r7   rC   rJ   r^   rc   rO   r   r   r   r   r/   r/   M   s*   � ��� 2�"
�
�.� $�r   r/   N)r   r   r   r"   r#   rR   r$   rS   r%   rT   r'   r/   r   r   r   �<module>rx      sg   ��,� ,���� �%��l�A�6���%��l�C�8���%��l�D�9��1$� 1$�ha� ar   PK     Ȃ�Y킩�B  B     segmenttree/license.txtMIT License

Copyright (c) 2017 Evgeny Yurtaev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.PK     �l�YT�m�  �     segmenttree/segmenttree.pyclass Operation:
    def __init__(self, name, function, function_on_equal, neutral_value=0):
        self.name = name
        self.f = function
        self.f_on_equal = function_on_equal


def add_multiple(x, count):
    return x * count


def min_multiple(x, count):
    return x


def max_multiple(x, count):
    return x


def count_multiple(x, count):
    return len(x) * count


count_operation = Operation("count", len, count_multiple, 0)
sum_operation = Operation("sum", sum, add_multiple, 0)
min_operation = Operation("min", min, min_multiple, 1e9)
max_operation = Operation("max", max, max_multiple, -1e9)


class SegmentTree:
    """
    SegmentTree class. Handles an underlying array as well as available
    operations and pointer to the root of a tree.
    """

    def __init__(self,
                 array,
                 operations=[sum_operation, min_operation, max_operation]):
        """
        Builds a segment tree based on the provided `array`. Supports operations
        of class Operation provided in the operations array.
        """
        
        
        # self.array = array
        if type(operations) != list:
            raise TypeError("operations must be a list")
        self.root = SegmentTreeNode(0, len(array) - 1, self)

    
    def pointQuery(self, point, root=None, res=None):
        if root is None:
            root = self.root
        if res is None: 
            res = set()
        
        if len(root.true_intervals) > 0:
            [res.add(x) for x in root.true_intervals]

        # not a leaf node
        if root.left or root.right:
            if root.left and root.left.range[0] <= point <= root.left.range[1]:
                self.pointQuery(point, root.left, res)
            elif root.right :
                self.pointQuery(point, root.right, res)
                
        return res
    
    def pointQuery2(self, point, root=None, unique_count=0):
        # apply some operation that counts the number of unique true intervals at a subtree 
        if root is None:
            root = self.root

        # Count the number of true_intervals at this node
        unique_count += len(root.true_intervals)

        # Traverse left or right based on the query point
        if root.left or root.right:  # If it's not a leaf node
            if root.left and root.left.range[0] <= point <= root.left.range[1]:
                unique_count = self.pointQuery2(point, root.left, unique_count)
            elif root.right:
                unique_count = self.pointQuery2(point, root.right, unique_count)

        return unique_count

        

    def summary(self):
        """
        Prints the summary for the whole array (values in the root node).
        """
        return self.root.values
    
    
    """Does interval S1 overlap S2?
    |---S1---|
        |---S2---|
    
    or 
    
        |---S1---|
    |---S2---|    
    """
    def __overlaps(self, i1, i2):
        s1, e1 = i1
        s2, e2 = i2
        
        if (s1 <= e2 and s1 >= s2) or (e1 <= e2 and e1 >= s2):
            return True
        elif (s2 <= e1 and s2 >= s1) or (e2 <= e1 and e2 >= s1):
            return True
        
        return False    
    
    """
    Associate a primitive interval with a true interval. This should only happen if the true interval is fully contained in the primitive interval.
    """
    def associate(self, start, end, id, node=None):
        if node is None:
            node = self.root
            
        # if Int(v) sub [start, end]:
        if node.range[0] >= start and node.range[1] <= end:
            node.true_intervals.add(id)
            # print(f"associated node {node.range} with {start} - {end}")            
        else:
            # if left node interval intersects with [start, end]
            if node.left and self.__overlaps(node.left.range, (start, end)):
                self.associate(start, end, id, node.left)
            if node.right and self.__overlaps(node.right.range, (start, end)):
                self.associate(start, end, id, node.right)
                
    def dissociate(self, start, end, id, node=None):
        if node is None:
            node = self.root

        if node.range[0] >= start and node.range[1] <= end:
            node.true_intervals.remove(id)
            # print(f"dissociated node {node.range} with {start} - {end}")            
        else:
            # if left node interval intersects with [start, end]
            if node.left and self.__overlaps(node.left.range, (start, end)):
                self.dissociate(start, end, id, node.left)
            if node.right and self.__overlaps(node.right.range, (start, end)):
                self.dissociate(start, end, id, node.right)

    def __repr__(self):
        return self.root.__repr__()


class SegmentTreeNode:
    """
    Internal SegmentTreeNode class represents a node of a segment tree. Each node
    stores the reference to the left and the right bound of a segment this
    node is responsible for.
    """

    def __init__(self, start, end, segment_tree):
        self.range = (start, end)
        self.parent_tree = segment_tree
        self.range_value = None
        # self.values = {}
        self.left = None
        self.right = None
        
        self.true_intervals = set()
        
        if start == end:
            # self._sync()
            return
        self.left = SegmentTreeNode(start, start + (end - start) // 2,
                                    segment_tree)
        self.right = SegmentTreeNode(start + (end - start) // 2 + 1, end,
                                     segment_tree)
        # self._sync()
PK     ˀ�Y               tree/PK     ˀ�Y               tree/__pycache__/PK      �l�YS0�"�  �             ��    __main__.pyPK      j�Y                      �A�  __pycache__/PK      &��Y_�:��  �  $           ��  __pycache__/__main__.cpython-312.pycPK      ֋�Y%;��L  L  &           ��K  __pycache__/planesweep.cpython-311.pycPK      j�Yݨ�*�  �  &           ���(  __pycache__/planesweep.cpython-312.pycPK      zV�Y�p$tc  c  &           ���<  __pycache__/planesweep.cpython-313.pycPK      )h�Y            	          �A^R  geometry/PK      ֋�Y                      �A�R  geometry/__pycache__/PK      ֋�Y��4�k  k  ,           ���R  geometry/__pycache__/Polygon.cpython-311.pycPK      �`�Y':�p�  �  ,           ��mX  geometry/__pycache__/Polygon.cpython-312.pycPK      zV�Y��j�  �  ,           ���]  geometry/__pycache__/Polygon.cpython-313.pycPK      �`�YX�]k  k             ���b  geometry/Polygon.pyPK      �i�Y�$?؅  �             ��~e  planesweep.pyPK      �j�Y                      �A.z  priorityqueue/PK      ֋�Y                      �AZz  priorityqueue/__pycache__/PK      ֋�Y[��  �  9           ���z  priorityqueue/__pycache__/PrioritizedItem.cpython-311.pycPK      �|�Y[݁��  �  9           ��l~  priorityqueue/__pycache__/PrioritizedItem.cpython-312.pycPK      zV�Y��c��  �  9           ����  priorityqueue/__pycache__/PrioritizedItem.cpython-313.pycPK      �|�Yϸn�   �               ���  priorityqueue/PrioritizedItem.pyPK      =i�Y                      �A��  segmenttree/PK      }l�Y                      �A(�  segmenttree/__pycache__/PK      ֋�Y�����7  �7  3           ��^�  segmenttree/__pycache__/segmenttree.cpython-311.pycPK      }l�Y}ue�  �  3           ����  segmenttree/__pycache__/segmenttree.cpython-312.pycPK      zV�Y�p�r1&  1&  3           ����  segmenttree/__pycache__/segmenttree.cpython-313.pycPK      Ȃ�Y킩�B  B             ��	 segmenttree/license.txtPK      �l�YT�m�  �             ��� segmenttree/segmenttree.pyPK      ˀ�Y                      �Av tree/PK      ˀ�Y                      �A� tree/__pycache__/PK      n  �   