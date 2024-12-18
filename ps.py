PK      ��YS0�"�  �     __main__.pyfrom geometry.Polygon import Polygon
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
    main()PK     ���Y               __pycache__/PK     &��Y_�:��  �  $   __pycache__/__main__.cpython-312.pyc�
    &\\g�  �                   �H   � d dl mZ d dlmZ d� Zd� Zd� Zedk(  r e�        yy)�    )�Polygon)�
PlaneSweepc            
      �h  � g } g }t        t        �       j                  �       d   j                  �       �      }t	        |�      D ]@  }| j                  t        t        t        t        �       j                  �       �      �      �       �B t        t        �       j                  �       d   j                  �       �      }t	        |�      D ]@  }|j                  t        t        t        t        �       j                  �       �      �      �       �B t	        t        |�      �      D ]  }t        ||   |�      ||<   � | |fS )N�   )�int�input�split�strip�range�append�tuple�map�float�lenr   )�points�squares�inp�is       ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\__main__.py�	readInputr      s�   � ��F��G� �e�g�m�m�o�a� �&�&�(�
)�C��3�Z�����e�C��u�w�}�}��7�8�9� � �e�g�m�m�o�a� �&�&�(�
)�C��3�Z�����u�S�������8�9�:� � �3�w�<� ���W�Q�Z��+���
� !��7�?��    c                  ��  � t        dd�      5 } g }g }t        | j                  �       j                  �       d   j	                  �       �      }t        |�      D ]F  }|j                  t        t        t        | j                  �       j                  �       �      �      �       �H t        | j                  �       j                  �       d   j	                  �       �      }t        |�      D ]F  }|j                  t        t        t        | j                  �       j                  �       �      �      �       �H t        t        |�      �      D ]  }t        ||   |�      ||<   � ||fcd d d �       S # 1 sw Y   y xY w)Nztestinputs/test09.txt�rr   )�openr   �readliner	   r
   r   r   r   r   r   r   r   )�fr   r   r   r   s        r   �readInputFromFiler      s  � �	�%�s�	+�q����� �!�*�*�,�$�$�&�q�)�/�/�1�2���s��A��M�M�%��E�1�:�:�<�+=�+=�+?� @�A�B� ��!�*�*�,�$�$�&�q�)�/�/�1�2���s��A��N�N�5��U�A�J�J�L�,>�,>�,@�!A�B�C� � �s�7�|�$�A� ����Q�/�G�A�J� %��w�� 
,�	+�	+�s   �EE"�"E+c                  �   � 	 t        �       \  } }d}t        | |�      }|j                  �       }t        |�       y # t        $ r}|�d }~ww xY w)Nr   )r   r   �sweep�print�	Exception)r   r   �output�ps�es        r   �mainr%   '   sK   � �	�+�-���������(��������f���� �����s   �69 �	A	�A�A	�__main__N)�geometry.Polygonr   �
planesweepr   r   r   r%   �__name__� r   r   �<module>r+      s.   �� $� !��"�$
� �z���F� r   PK     ���Y�%�E  E  &   __pycache__/planesweep.cpython-312.pyc�
    C`ga  �                   �\   � d dl Z d dlmZmZ d dlmZ d dlmZ d dlZd dl	m
Z
  G d� d�      Zy)�    N)�IntervalTree�Interval)�Polygon)�PriorityQueue)�PrioritizedItemc                   �~   � e Zd Zdeeef   dee   fd�Zd� Zd� Z	de
fd�Z	 ded	efd
�Zdeeef   fd�Zd� Zdefd�Zy)�
PlaneSweep�points�squaresc                 �Z   � d| _         || _        || _        t        �       | _        g | _        y �Nr   )�_PlaneSweep__output�_PlaneSweep__points�_PlaneSweep__squaresr   �_PlaneSweep__sweepState�_PlaneSweep__events)�selfr
   r   s      ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\planesweep.py�__init__zPlaneSweep.__init__   s(   � ������� ���(�N������    c                 �  � | j                  �        t        | j                  �      dkD  rXt        j                  | j                  �      }|�	 | j                  S | j                  |�       t        | j                  �      dkD  r�X| j                  S r   )�_PlaneSweep__getEvents�lenr   �heapq�heappop�_PlaneSweep__handleEventr   �r   �events     r   �sweepzPlaneSweep.sweep   st   � ������$�-�-� �1�$��M�M�$�-�-�0�E��}�� �}�}�� ���u�%� �$�-�-� �1�$� �}�}�r   c                 ��  � | j                   D ]�  }|j                  d�      }t        |d   |d   df|�      }t        j                  | j
                  |�       |j                  d�      }t        |d   |d   df|�      }t        j                  | j
                  |�       �� | j                  D ]7  }t        |d   |d   df|�      }t        j                  | j
                  |�       �9 y )Nr   �   �   )r   �getPointr   r   �heappushr   r   )r   �square�pr   �points        r   �__getEventszPlaneSweep.__getEvents!   s�   � � �n�n�F�����"�A�#�Q�q�T�1�Q�4��O�V�<�E��N�N�4�=�=�%�0� ����"�A�#�Q�q�T�1�Q�4��O�V�<�E��N�N�4�=�=�%�0� %� �]�]�E�#�U�1�X�u�Q�x��$;�U�C�E��N�N�4�=�=�%�0� #r   r   c                 ��   � t        |j                  �      t        k(  r*| j                  |j                  d   |j                  �       y | j                  |j                  �       y r   )�type�itemr   �_PlaneSweep__handleSquareEvent�priority�_PlaneSweep__handlePointEventr   s     r   �__handleEventzPlaneSweep.__handleEvent;   sB   � ���
�
��w�&��$�$�U�^�^�A�%6��
�
�C��#�#�E�J�J�/r   �yValuer%   c                 ��   � |j                  �       \  }}}}t        |||j                  �      }||k(  r| j                  j	                  |�       y | j                  j                  |�       y �N)�	getLimitsr   �idr   �add�remove)r   r0   r%   �xmin�xmax�ymin�_�intervals           r   �__handleSquareEventzPlaneSweep.__handleSquareEventE   s^   � � %�.�.�0���d�D�!��D�$��	�	�2���T�>����!�!�(�+� ���$�$�X�.r   r'   c                 �R   � | xj                   | j                  |d   �      z  c_         y r   )r   �_PlaneSweep__countIntervals)r   r'   s     r   �__handlePointEventzPlaneSweep.__handlePointEventS   s!   � � 	����.�.�u�Q�x�8�8�r   c                  �   � y r2   � )r   s    r   �__findNewEventzPlaneSweep.__findNewEventX   s   � �r   �xValuec                 �8   � | j                   j                  |�      S r2   )r   �countPointOverlaps3)r   rC   s     r   �__countIntervalszPlaneSweep.__countIntervals]   s   � � � � �4�4�V�<�<r   N)�__name__�
__module__�__qualname__�tuple�float�listr   r   r   r   r   r   r,   r.   �_PlaneSweep__findNewEventr>   rA   r   r   r	   r	      sv   � ��u�U�E�\�2� �T�'�]� ��1�40�?� 0��/�%� /�� /�9��e�U�l�(;� 9�
�
=�u� =r   r	   )�math�intervaltree.intervaltreer   r   �geometry.Polygonr   �queuer   r   �priorityqueue.PrioritizedItemr   r	   rA   r   r   �<module>rS      s#   �� � <� $� � � 9�Z=� Z=r   PK     )h�Y            	   geometry/PK     4��Y               geometry/__pycache__/PK     4��Y)���  �  ,   geometry/__pycache__/Polygon.cpython-312.pyc�
    1L\g&  �                   �   �  G d � d�      Z y)c                   �.   � e Zd Zdedefd�Zdefd�Zd� Zy)�Polygon�args�idc                 �    � || _         || _        y �N)�limsr   )�selfr   r   s      ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\geometry\Polygon.py�__init__zPolygon.__init__   s   � � ��	����    �clockWiseIndexc                 �   � | j                   \  }}}}|dk(  r||fS |dk(  r||fS |dk(  r||fS |dk(  r||fS t        d�      �)N�    �   �   �   z clockWiseIndex must be in [0, 3])r   �
ValueError)r	   r   �xmin�xmax�ymin�ymaxs         r
   �getPointzPolygon.getPoint   sh   � �!%�����d�D�$��Q���$�<���q� ��$�<���q� ��$�<���q� ��$�<���?�@�@r   c                 �   � | j                   S r   )r   )r	   s    r
   �	getLimitszPolygon.getLimits   s   � ��y�y�r   N)�__name__�
__module__�__qualname__�list�intr   r   r   � r   r
   r   r      s(   � ��T� �s� �A�s� A�r   r   N)r   r    r   r
   �<module>r!      s   ��� r   PK     "��Y	��I&  &     geometry/Polygon.pyclass Polygon():
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
        return self.limsPK     ˀ�Y               intervaltree/PK     ˀ�Yq�m;g  g     intervaltree/__init__.py#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Root package.

Copyright 2013-2018 Chaim Leib Halbert

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from .interval import Interval
from .intervaltree import IntervalTree
PK     ���Y               intervaltree/__pycache__/PK     ���YQ�_@  @  1   intervaltree/__pycache__/__init__.cpython-312.pyc�
    �A`gg  �                   �    � d Z ddlmZ ddlmZ y)a�  
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Root package.

Copyright 2013-2018 Chaim Leib Halbert

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
�   )�Interval)�IntervalTreeN)�__doc__�intervalr   �intervaltreer   � �    ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\intervaltree\__init__.py�<module>r      s   ���( � &r	   PK     ���Y�mB4  4  1   intervaltree/__pycache__/interval.cpython-312.pyc�
    �C`g>)  �            	       �H   � d Z ddlmZ ddlmZ  G d� d edg d��      �      Zy)	a  
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Interval class

Copyright 2013-2018 Chaim Leib Halbert
Modifications copyright 2014 Konstantin Tretyakov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
�    )�Number)�
namedtuplec                   �   � � e Zd ZdZd� fd�	Zdd�Zdd�Zd� Zd� Zd� Z	d� Z
d	� Zd
� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� ZeZd� Zd� Z� xZS )�Interval� c                 �0   �� t         t        | �  | |||�      S �N)�superr   �__new__)�cls�begin�end�data�	__class__s       ���C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\intervaltree\interval.pyr   zInterval.__new__!   s   �� ��X�s�+�C���T�B�B�    c                 ��   � |� || j                   k  xr || j                  kD  S 	 | j                  |j                  |j                   �      S #  | j                  |�      cY S xY w)a$  
        Whether the interval overlaps the given point, range or Interval.
        :param begin: beginning point of the range, or the point, or an Interval
        :param end: end point of the range. Optional if not testing ranges.
        :return: True or False
        :rtype: bool
        )r   r   �overlaps�contains_point)�selfr   r   s      r   r   zInterval.overlaps$   s^   � � �?� �4�8�8�#�8��d�j�j�(8�8�	.��=�=����e�i�i�8�8��	.��&�&�u�-�-�s   �%A
 �
Ac                 �  � | j                  ||�      }|sy|�1t        | j                  |�      }t        | j                  |�      }||z
  S t        | j                  |j                  �      }t        | j                  |j                  �      }||z
  S )a�  
        Return the overlap size between two intervals or a point
        :param begin: beginning point of the range, or the point, or an Interval
        :param end: end point of the range. Optional if not testing ranges.
        :return: Return the overlap size, None if not overlap is found
        :rtype: depends on the given input (e.g., int will be returned for int interval and timedelta for
        datetime intervals)
        r   )r   �maxr   �minr   )r   r   r   r   �i0�i1s         r   �overlap_sizezInterval.overlap_size8   sy   � � �=�=���,�����?��T�Z�Z��'�B��T�X�X�s�#�B���7�N�����U�[�[�)������5�9�9�%���B�w�r   c                 �J   � | j                   |cxk  xr | j                  k  S c S )z�
        Whether the Interval contains p.
        :param p: a point
        :return: True or False
        :rtype: bool
        �r   r   )r   �ps     r   r   zInterval.contains_pointO   s"   � � �z�z�Q�*�$�(�(�*�*�*�*r   c                 �j   � | j                   |j                   k(  xr | j                  |j                  k(  S )z�
        Whether the begins equal and the ends equal. Compare __eq__().
        :param other: Interval
        :return: True or False
        :rtype: bool
        r   �r   �others     r   �range_matcheszInterval.range_matchesX   �.   � � �J�J�%�+�+�%� "��H�H��	�	�!�	
r   c                 �j   � | j                   |j                   k  xr | j                  |j                  k\  S )z�
        Whether other is contained in this Interval.
        :param other: Interval
        :return: True or False
        :rtype: bool
        r   r!   s     r   �contains_intervalzInterval.contains_intervald   r$   r   c                 �*  � | j                  |�      ry	 | j                  |j                  k  r|j                  | j                  z
  S | j                  |j                  z
  S #  | j                  |k  r|| j                  z
  cY S | j                  |z
  cY S xY w)z�
        Returns the size of the gap between intervals, or 0 
        if they touch or overlap.
        :param other: Interval or point
        :return: distance
        :rtype: Number
        r   )r   r   r   r!   s     r   �distance_tozInterval.distance_top   s   � � �=�=����		*��z�z�E�K�K�'��{�{�T�X�X�-�-��z�z�E�I�I�-�-��	*��x�x�5� ��t�x�x�'�'��z�z�E�)�)�s   �1A �A � B�Bc                 �4   � | j                   | j                  kD  S )z~
        Whether this equals the null interval.
        :return: True if end <= begin else False
        :rtype: bool
        r   �r   s    r   �is_nullzInterval.is_null�   s   � � �z�z�D�H�H�$�$r   c                 �V   � | j                  �       ry| j                  | j                  z
  S )zf
        The distance covered by this Interval.
        :return: length
        :type: Number
        r   )r+   r   r   r*   s    r   �lengthzInterval.length�   s#   � � �<�<�>���x�x�$�*�*�$�$r   c                 �D   � t        | j                  | j                  f�      S )z]
        Depends on begin and end only.
        :return: hash
        :rtype: Number
        )�hashr   r   r*   s    r   �__hash__zInterval.__hash__�   s   � � �T�Z�Z����*�+�+r   c                 �   � | j                   |j                   k(  xr4 | j                  |j                  k(  xr | j                  |j                  k(  S )z�
        Whether the begins equal, the ends equal, and the data fields
        equal. Compare range_matches().
        :param other: Interval
        :return: True or False
        :rtype: bool
        �r   r   r   r!   s     r   �__eq__zInterval.__eq__�   sC   � � �J�J�%�+�+�%� $��H�H��	�	�!�$��I�I����#�	
r   c                 �v  � | dd }	 |dd }||k7  r	||k  rdS dS 	 | j                   |j                   k(  ry| j                   |j                   k  rdS dS #  |f}Y �MxY w# t        $ rS t        | j                   �      j                  }t        |j                   �      j                  }||k(  rY y||k  rdcY S dcY S w xY w)a^  
        Tells whether other sorts before, after or equal to this
        Interval.

        Sorting is by begins, then by ends, then by data fields.

        If data fields are not both sortable types, data fields are
        compared alphabetically by type name.
        :param other: Interval
        :return: -1, 0, 1
        :rtype: int
        r   �   ������   )r   �	TypeError�type�__name__)r   r"   �s�os       r   �__cmp__zInterval.__cmp__�   s�   � � ��1�I��	��a��
�A� ��6��Q��2�%�A�%�		&��y�y�E�J�J�&�����U�Z�Z�/�2�6�Q�6��	���A�� � 	&��T�Y�Y��(�(�A��U�Z�Z� �)�)�A��A�v���Q��2�%�A�%�	&�s4   �A �A �A �A �A�AB8�*B8�3B8�7B8c                 �*   � | j                  |�      dk  S )z�
        Less than operator. Parrots __cmp__()
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        r   �r=   r!   s     r   �__lt__zInterval.__lt__�   �   � � �|�|�E�"�Q�&�&r   c                 �*   � | j                  |�      dkD  S )z�
        Greater than operator. Parrots __cmp__()
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        r   r?   r!   s     r   �__gt__zInterval.__gt__�   rA   r   c                 �   � | j                  �       rt        d�      �t        |d�      r|j                  �       rt        d�      �yy)zP
        :raises ValueError: if either self or other is a null Interval
        zCannot compare null Intervals!r+   N)r+   �
ValueError�hasattrr!   s     r   �_raise_if_nullzInterval._raise_if_null�   s?   � � �<�<�>��=�>�>��5�)�$������=�>�>� *9�$r   c                 �X   � | j                  |�       | j                  t        |d|�      k  S )a  
        Strictly less than. Returns True if no part of this Interval
        extends higher than or into other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        r   �rG   r   �getattrr!   s     r   �ltzInterval.lt�   s*   � � 	���E�"��x�x�7�5�'�5�9�9�9r   c                 �X   � | j                  |�       | j                  t        |d|�      k  S )a  
        Less than or overlaps. Returns True if no part of this Interval
        extends higher than other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        r   rI   r!   s     r   �lezInterval.le�   s*   � � 	���E�"��x�x�7�5�%��7�7�7r   c                 �   � | j                  |�       t        |d�      r| j                  |j                  k\  S | j                  |kD  S )a  
        Strictly greater than. Returns True if no part of this Interval
        extends lower than or into other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        r   )rG   rF   r   r   r!   s     r   �gtzInterval.gt�   s>   � � 	���E�"��5�%� ��:�:����*�*��:�:��%�%r   c                 �X   � | j                  |�       | j                  t        |d|�      k\  S )a  
        Greater than or overlaps. Returns True if no part of this Interval
        extends lower than other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        r   )rG   r   rJ   r!   s     r   �gezInterval.ge  s*   � � 	���E�"��z�z�W�U�G�U�;�;�;r   c                 �   � | j                   �#| j                  | j                  | j                   fS | j                  | j                  fS )z�
        Used by str, unicode, repr and __reduce__.

        Returns only the fields necessary to reconstruct the Interval.
        :return: reconstruction info
        :rtype: tuple
        )r   r   r   r*   s    r   �_get_fieldszInterval._get_fields  s:   � � �9�9� ��:�:�t�x�x����2�2��:�:�t�x�x�'�'r   c                 �h  � t        | j                  t        �      r+t        | j                  �      }t        | j                  �      }n*t        | j                  �      }t        | j                  �      }| j                  �dj                  ||�      S dj                  ||t        | j                  �      �      S )z
        Executable string representation of this Interval.
        :return: string representation
        :rtype: str
        zInterval({0}, {1})zInterval({0}, {1}, {2}))�
isinstancer   r   �strr   �reprr   �format)r   �s_begin�s_ends      r   �__repr__zInterval.__repr__'  s�   � � �d�j�j�&�)��$�*�*�o�G�����M�E��4�:�:�&�G�����N�E��9�9��'�.�.�w��>�>�,�3�3�G�U�D����O�T�Tr   c                 �X   � t        | j                  | j                  | j                  �      S )zV
        Shallow copy.
        :return: copy of self
        :rtype: Interval
        )r   r   r   r   r*   s    r   �copyzInterval.copy:  s   � � ��
�
�D�H�H�d�i�i�8�8r   c                 �.   � t         | j                  �       fS )zT
        For pickle-ing.
        :return: pickle data
        :rtype: tuple
        )r   rS   r*   s    r   �
__reduce__zInterval.__reduce__B  s   � � ��)�)�+�+�+r   r	   )r:   �
__module__�__qualname__�	__slots__r   r   r   r   r#   r&   r(   r+   r-   r0   r3   r=   r@   rC   rG   rK   rM   rO   rQ   rS   r[   �__str__r]   r_   �__classcell__)r   s   @r   r   r      s�   �� ��I�C�.�(�.+�

�

�*�*%�%�,�
�&�>'�'�?�
:�
8�&�
<�(�U�" �G�9�,r   r   �IntervalBaser2   N)�__doc__�numbersr   �collectionsr   r   r   r   r   �<module>ri      s(   ���* � "�j,�z�.�*B�C� j,r   PK     ���Y	��  �  5   intervaltree/__pycache__/intervaltree.cpython-312.pyc�
    �A`gū  �                   �   � d Z ddlmZ ddlmZ ddlmZ ddlmZ ddl	m	Z	 ddl
mZ 	 dd	lmZ 	 e  G d
� de�      Zy# e$ r	 dd	lmZ Y �w xY w# e$ r eZY �&w xY w)a  
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Core logic.

Copyright 2013-2018 Chaim Leib Halbert
Modifications Copyright 2014 Konstantin Tretyakov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
�   ��Interval)�Node�    )�Number)�
SortedDict��copy)�warn)�
MutableSetc                   ��  � e Zd ZdZed� �       Zd>d�Zd� Zd� Zd� Z	d� Z
e
Zd>d	�ZeZd
� Zd� Zd>d�Zd� Zd>d�Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd>d�Zd� Zd>d�Zd>d�Zd� Zd� Zd>d�Z d� Z!d� Z"d� Z#d?d �Z$d@d!�Z%	 	 	 	 dAd"�Z&d#� Z'd$� Z(d%� Z)d&e*d'e*fd(�Z+d&e*d'e*fd)�Z,d&e*d'e*fd*�Z-d>d+�Z.d>d,�Z/d-� Z0d.� Z1d/� Z2d0� Z3dBd1�Z4d2� Z5dBd3�Z6d4� Z7d5� Z8d6� Z9d7� Z:d>d8�Z;d9� Z<e<Z=d:� Z>d;� Z?d<� Z@e@ZAd=� ZBy)C�IntervalTreea�  
    A binary lookup tree of intervals.
    The intervals contained in the tree are represented using ``Interval(a, b, data)`` objects.
    Each such object represents a half-open interval ``[a, b)`` with optional data.

    Examples:
    ---------

    Initialize a blank tree::

        >>> tree = IntervalTree()
        >>> tree
        IntervalTree()

    Initialize a tree from an iterable set of Intervals in O(n * log n)::

        >>> tree = IntervalTree([Interval(-10, 10), Interval(-20.0, -10.0)])
        >>> tree
        IntervalTree([Interval(-20.0, -10.0), Interval(-10, 10)])
        >>> len(tree)
        2

    Note that this is a set, i.e. repeated intervals are ignored. However,
    Intervals with different data fields are regarded as different::

        >>> tree = IntervalTree([Interval(-10, 10), Interval(-10, 10), Interval(-10, 10, "x")])
        >>> tree
        IntervalTree([Interval(-10, 10), Interval(-10, 10, 'x')])
        >>> len(tree)
        2

    Insertions::
        >>> tree = IntervalTree()
        >>> tree[0:1] = "data"
        >>> tree.add(Interval(10, 20))
        >>> tree.addi(19.9, 20)
        >>> tree
        IntervalTree([Interval(0, 1, 'data'), Interval(10, 20), Interval(19.9, 20)])
        >>> tree.update([Interval(19.9, 20.1), Interval(20.1, 30)])
        >>> len(tree)
        5

        Inserting the same Interval twice does nothing::
            >>> tree = IntervalTree()
            >>> tree[-10:20] = "arbitrary data"
            >>> tree[-10:20] = None  # Note that this is also an insertion
            >>> tree
            IntervalTree([Interval(-10, 20), Interval(-10, 20, 'arbitrary data')])
            >>> tree[-10:20] = None  # This won't change anything
            >>> tree[-10:20] = "arbitrary data" # Neither will this
            >>> len(tree)
            2

    Deletions::
        >>> tree = IntervalTree(Interval(b, e) for b, e in [(-10, 10), (-20, -10), (10, 20)])
        >>> tree
        IntervalTree([Interval(-20, -10), Interval(-10, 10), Interval(10, 20)])
        >>> tree.remove(Interval(-10, 10))
        >>> tree
        IntervalTree([Interval(-20, -10), Interval(10, 20)])
        >>> tree.remove(Interval(-10, 10))
        Traceback (most recent call last):
        ...
        ValueError
        >>> tree.discard(Interval(-10, 10))  # Same as remove, but no exception on failure
        >>> tree
        IntervalTree([Interval(-20, -10), Interval(10, 20)])

    Delete intervals, overlapping a given point::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.1)
        >>> tree
        IntervalTree([Interval(-1.1, 1.1)])

    Delete intervals, overlapping an interval::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> tree.remove_overlap(0, 0.5)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.7, 1.8)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.6, 1.6)  # Null interval does nothing
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.6, 1.5)  # Ditto
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])

    Delete intervals, enveloped in the range::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> tree.remove_envelop(-1.0, 1.5)
        >>> tree
        IntervalTree([Interval(-1.1, 1.1), Interval(0.5, 1.7)])
        >>> tree.remove_envelop(-1.1, 1.5)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_envelop(0.5, 1.5)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_envelop(0.5, 1.7)
        >>> tree
        IntervalTree()

    Point queries::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree[-1.1]   == set([Interval(-1.1, 1.1)])
        >>> assert tree.at(1.1) == set([Interval(-0.5, 1.5), Interval(0.5, 1.7)])   # Same as tree[1.1]
        >>> assert tree.at(1.5) == set([Interval(0.5, 1.7)])                        # Same as tree[1.5]

    Interval overlap queries

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree.overlap(1.7, 1.8) == set()
        >>> assert tree.overlap(1.5, 1.8) == set([Interval(0.5, 1.7)])
        >>> assert tree[1.5:1.8] == set([Interval(0.5, 1.7)])                       # same as previous
        >>> assert tree.overlap(1.1, 1.8) == set([Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree[1.1:1.8] == set([Interval(-0.5, 1.5), Interval(0.5, 1.7)])  # same as previous

    Interval envelop queries::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree.envelop(-0.5, 0.5) == set()
        >>> assert tree.envelop(-0.5, 1.5) == set([Interval(-0.5, 1.5)])

    Membership queries::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> Interval(-0.5, 0.5) in tree
        False
        >>> Interval(-1.1, 1.1) in tree
        True
        >>> Interval(-1.1, 1.1, "x") in tree
        False
        >>> tree.overlaps(-1.1)
        True
        >>> tree.overlaps(1.7)
        False
        >>> tree.overlaps(1.7, 1.8)
        False
        >>> tree.overlaps(-1.2, -1.1)
        False
        >>> tree.overlaps(-1.2, -1.0)
        True

    Sizing::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> len(tree)
        3
        >>> tree.is_empty()
        False
        >>> IntervalTree().is_empty()
        True
        >>> not tree
        False
        >>> not IntervalTree()
        True
        >>> print(tree.begin())    # using print() because of floats in Python 2.6
        -1.1
        >>> print(tree.end())      # ditto
        1.7

    Iteration::

        >>> tree = IntervalTree([Interval(-11, 11), Interval(-5, 15), Interval(5, 17)])
        >>> [iv.begin for iv in sorted(tree)]
        [-11, -5, 5]
        >>> assert tree.items() == set([Interval(-5, 15), Interval(-11, 11), Interval(5, 17)])

    Copy- and typecasting, pickling::

        >>> tree0 = IntervalTree([Interval(0, 1, "x"), Interval(1, 2, ["x"])])
        >>> tree1 = IntervalTree(tree0)  # Shares Interval objects
        >>> tree2 = tree0.copy()         # Shallow copy (same as above, as Intervals are singletons)
        >>> import pickle
        >>> tree3 = pickle.loads(pickle.dumps(tree0))  # Deep copy
        >>> list(tree0[1])[0].data[0] = "y"  # affects shallow copies, but not deep copies
        >>> tree0
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['y'])])
        >>> tree1
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['y'])])
        >>> tree2
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['y'])])
        >>> tree3
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['x'])])

    Equality testing::

        >>> IntervalTree([Interval(0, 1)]) == IntervalTree([Interval(0, 1)])
        True
        >>> IntervalTree([Interval(0, 1)]) == IntervalTree([Interval(0, 1, "x")])
        False
    c                 �L   � |D �cg c]
  }t        |� �� }}t        |�      S c c}w )z�
        Create a new IntervalTree from an iterable of 2- or 3-tuples,
         where the tuple lists begin, end, and optionally data.
        )r   r   )�cls�tups�t�ivss       ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\intervaltree\intervaltree.py�from_tupleszIntervalTree.from_tuples�   s,   � � &*�*�T��x��|�T��*��C� � �� +s   �!Nc                 �L  � |�t        |�      n	t        �       }|D ],  }|j                  �       s�t        dj                  |�      �      � || _        t        j                  | j                  �      | _        t        �       | _	        | j                  D ]  }| j                  |�       � y)z�
        Set up a tree. If intervals is provided, add all the intervals
        to the tree.

        Completes in O(n*log n) time.
        N�DIntervalTree: Null Interval objects not allowed in IntervalTree: {0})�set�is_null�
ValueError�format�all_intervalsr   �from_intervals�top_noder   �boundary_table�_add_boundaries��self�	intervals�ivs      r   �__init__zIntervalTree.__init__�   s�   � � '0�&;�C�	�N���	��B��z�z�|� ��!�6�"�:�� � � '����+�+�D�,>�,>�?���(�l����$�$�B�� � ��$� %�    c                 �&   � t        d� | D �       �      S )z�
        Construct a new IntervalTree using shallow copies of the
        intervals in the source tree.

        Completes in O(n*log n) time.
        :rtype: IntervalTree
        c              3   �<   K  � | ]  }|j                  �       �� � y �w�Nr	   )�.0r$   s     r   �	<genexpr>z$IntervalTree.copy.<locals>.<genexpr>  s   � �� �5��"�B�G�G�I��s   �)r   �r"   s    r   r
   zIntervalTree.copy  s   � � �5��5�5�5r&   c                 �  � |j                   }|j                  }|| j                  v r| j                  |xx   dz  cc<   nd| j                  |<   || j                  v r| j                  |xx   dz  cc<   yd| j                  |<   y)zO
        Records the boundaries of the interval in the boundary table.
        r   N��begin�endr   �r"   �intervalr/   r0   s       r   r    zIntervalTree._add_boundaries  s~   � � �����l�l���D�'�'�'�����&�!�+�&�)*�D����&��$�%�%�%�����$��)�$�'(�D����$r&   c                 �  � |j                   }|j                  }| j                  |   dk(  r| j                  |= n| j                  |xx   dz  cc<   | j                  |   dk(  r| j                  |= y| j                  |xx   dz  cc<   y)zQ
        Removes the boundaries of the interval from the boundary table.
        r   Nr.   r1   s       r   �_remove_boundarieszIntervalTree._remove_boundaries)  s�   � � �����l�l�����u�%��*��#�#�E�*�����&�!�+�&����s�#�q�(��#�#�C�(�����$��)�$r&   c                 �H  � || v ry|j                  �       rt        dj                  |�      �      �| j                  st	        j
                  |�      | _        n | j                  j                  |�      | _        | j                  j                  |�       | j                  |�       y)zl
        Adds an interval to the tree, if not already present.

        Completes in O(log n) time.
        Nr   )	r   r   r   r   r   �from_interval�addr   r    �r"   r2   s     r   r7   zIntervalTree.add9  s�   � � �t����������v�h�'�� �
 �}�}� �.�.�x�8�D�M� �M�M�-�-�h�7�D�M������x�(����X�&r&   c                 �:   � | j                  t        |||�      �      S )zd
        Shortcut for add(Interval(begin, end, data)).

        Completes in O(log n) time.
        )r7   r   �r"   r/   r0   �datas       r   �addizIntervalTree.addiP  s   � � �x�x����T�2�3�3r&   c                 �4   � |D ]  }| j                  |�       � y)z�
        Given an iterable of intervals, add them to the tree.

        Completes in O(m*log(n+m), where m = number of intervals to
        add.
        N)r7   r!   s      r   �updatezIntervalTree.updateY  s   � � �B��H�H�R�L� r&   c                 �   � || vrt         �| j                  j                  |�      | _        | j                  j                  |�       | j	                  |�       y)z�
        Removes an interval from the tree, if present. If not, raises
        ValueError.

        Completes in O(log n) time.
        N)r   r   �remover   r4   r8   s     r   r@   zIntervalTree.removec  sJ   � � �4�������,�,�X�6������!�!�(�+�����)r&   c                 �:   � | j                  t        |||�      �      S )zg
        Shortcut for remove(Interval(begin, end, data)).

        Completes in O(log n) time.
        )r@   r   r:   s       r   �removeizIntervalTree.removeis  s   � � �{�{�8�E�3��5�6�6r&   c                 �   � || vry| j                   j                  |�       | j                  j                  |�      | _        | j                  |�       y)z�
        Removes an interval from the tree, if present. If not, does
        nothing.

        Completes in O(log n) time.
        N)r   �discardr   r4   r8   s     r   rD   zIntervalTree.discard{  sG   � � �4������"�"�8�,����-�-�h�7�������)r&   c                 �:   � | j                  t        |||�      �      S )zh
        Shortcut for discard(Interval(begin, end, data)).

        Completes in O(log n) time.
        )rD   r   r:   s       r   �discardizIntervalTree.discardi�  s   � � �|�|�H�U�C��6�7�7r&   c                 �f   � t        �       }| D ]  }||vs�|j                  |�       � t        |�      S )z`
        Returns a new tree, comprising all intervals in self but not
        in other.
        )r   r7   r   �r"   �otherr   r$   s       r   �
differencezIntervalTree.difference�  s4   � �
 �e���B��������� � �C� � r&   c                 �4   � |D ]  }| j                  |�       � y)z;
        Removes all intervals in other from self.
        N)rD   )r"   rI   r$   s      r   �difference_updatezIntervalTree.difference_update�  s   � � �B��L�L��� r&   c                 �H   � t        t        | �      j                  |�      �      S )z[
        Returns a new tree, comprising all intervals from self
        and other.
        )r   r   �union�r"   rI   s     r   rN   zIntervalTree.union�  s   � �
 �C��I�O�O�E�2�3�3r&   c                 �   � t        �       }t        | |gt        ��      \  }}|D ]  }||v s�|j                  |�       � t	        |�      S )z\
        Returns a new tree of all intervals common to both self and
        other.
        )�key)r   �sorted�lenr7   r   )r"   rI   r   �shorter�longerr$   s         r   �intersectionzIntervalTree.intersection�  sH   � �
 �e�� �$���C�8�����B��V�|������ � �C� � r&   c                 �T   � t        | �      }|D ]  }||vs�| j                  |�       � y)zN
        Removes intervals from self unless they also exist in other.
        N)�listr@   rH   s       r   �intersection_updatez IntervalTree.intersection_update�  s)   � � �4�j���B�������B�� r&   c                 ��   � t        |t        �      st        |�      }t        | �      }|j                  |�      j                  |j                  |�      �      }t	        |�      S )zY
        Return a tree with elements only in self or other but not
        both.
        )�
isinstancer   rJ   rN   r   )r"   rI   �mer   s       r   �symmetric_differencez!IntervalTree.symmetric_difference�  sN   � �
 �%��%�s�5�z�u���Y���m�m�E�"�(�(��)9�)9�"�)=�>���C� � r&   c                 �   � t        |�      }t        | �      }|D ])  }||v s�| j                  |�       |j                  |�       �+ | j                  |�       y)z`
        Throws out all intervals except those only in self or other,
        not both.
        N)r   rX   r@   r>   rH   s       r   �symmetric_difference_updatez(IntervalTree.symmetric_difference_update�  sL   � �
 �E�
���4�j���B��U�{����B�����R� � � 	���E�r&   c                 �~   � |�| j                  |�      n| j                  ||�      }|D ]  }| j                  |�       � y)a  
        Removes all intervals overlapping the given point or range.

        Completes in O((r+m)*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * r = size of the search range (this is 1 for a point)
        N)�at�overlapr@   �r"   r/   r0   �hitlistr$   s        r   �remove_overlapzIntervalTree.remove_overlap�  s7   � � %(�K�$�'�'�%�.�T�\�\�%��5M���B��K�K��O� r&   c                 �X   � | j                  ||�      }|D ]  }| j                  |�       � y)z�
        Removes all intervals completely enveloped in the given range.

        Completes in O((r+m)*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * r = size of the search range
        N)�envelopr@   rc   s        r   �remove_envelopzIntervalTree.remove_envelop�  s)   � � �,�,�u�c�*���B��K�K��O� r&   c                 �   � t        �       }| j                  |�      D �cg c]  }|j                  |k  s�|�� }}| j                  |�      D �cg c]  }|j                  |kD  s�|�� }}|ri|D ]/  }|j	                  t        |j                  | ||d�      �      �       �1 |D ]/  }|j	                  t        ||j                   ||d�      �      �       �1 nn|D ]2  }|j	                  t        |j                  ||j                  �      �       �4 |D ]2  }|j	                  t        ||j                  |j                  �      �       �4 | j                  ||�       | j                  |�       | j                  |�       | j                  |�       yc c}w c c}w )z�
        Like remove_envelop(), but trims back Intervals hanging into
        the chopped area so that nothing overlaps.
        TFN)
r   ra   r/   r0   r7   r   r;   rh   rL   r>   )r"   r/   r0   �datafunc�
insertionsr$   �
begin_hits�end_hitss           r   �chopzIntervalTree.chop�  sB  � �
 �U�
�#'�7�7�5�>�F�>�R�R�X�X��5E�b�>�
�F�!%�����>��2����#��B���>�� �����x����%��"�d�9K�L�M� !������x��R�V�V�X�b�%�5H�I�J� � !�����x����%����A�B� !������x��R�V�V�R�W�W�=�>� � 	���E�3�'����z�*����x�(����J���# G��>s   �F�F�F�!Fc                 �:  �� t        �fd�| j                  ��      D �       �      }t        �       }|rb|D ]\  }|j                  t        |j                  � ||d�      �      �       |j                  t        �|j
                   ||d�      �      �       �^ ng|D ]b  }|j                  t        |j                  �|j                  �      �       |j                  t        �|j
                  |j                  �      �       �d | j                  |�       | j                  |�       y)aX  
        Split Intervals that overlap point into two new Intervals. if
        specified, uses datafunc(interval, islower=True/False) to
        set the data field of the new Intervals.
        :param point: where to slice
        :param datafunc(interval, isupper): callable returning a new
        value for the interval's data field
        c              3   �B   �K  � | ]  }|j                   �k  s�|�� � y �wr)   )r/   )r*   r$   �points     �r   r+   z%IntervalTree.slice.<locals>.<genexpr>  s   �� �� �F�>�R�R�X�X��5E�b�>�s   ��TFN)	r   ra   r7   r   r/   r0   r;   rL   r>   )r"   rq   rj   rd   rk   r$   s    `    r   �slicezIntervalTree.slice  s�   �� � �F�4�7�7�5�>�F�F���U�
�������x����%��"�d�9K�L�M����x��r�v�v�x��E�7J�K�L� � �����x����%����A�B����x��r�v�v�r�w�w�?�@� � 	���w�'����J�r&   c                 �$   � | j                  �        y)zD
        Empties the tree.

        Completes in O(1) tine.
        N)r%   r,   s    r   �clearzIntervalTree.clear  s   � � 	���r&   c                 �   ���� i ����fd�}t        | j                  t        j                  d��      }t	        |�      D ]  \  }�||dz   d D ]	  � |�        � � �S )z�
        Returns a dictionary mapping parent intervals to sets of
        intervals overlapped by and contained in the parent.

        Completes in O(n^2) time.
        :rtype: dict of [Interval, set of Interval]
        c                  �t   �� �j                  � �      r&��vrt        �       ��<   ��   j                  � �       y y r)   )�contains_intervalr   r7   )�child�parent�results   ���r   �add_if_nestedz/IntervalTree.find_nested.<locals>.add_if_nested0  s;   �� ��'�'��.���'�%(�U�F�6�N��v��"�"�5�)� /r&   T)rQ   �reverser   N)rR   r   r   �length�	enumerate)r"   r{   �long_ivs�irx   ry   rz   s       @@@r   �find_nestedzIntervalTree.find_nested&  s]   �� � ��	*� �$�,�,�(�/�/�4�P��"�8�,�I�A�v�!�!�a�%�&�)���� *� -� �r&   c                 �   � |�| j                  ||�      S t        |t        �      r| j                  |�      S | j                  |j                  |j
                  �      S )z�
        Returns whether some interval in the tree overlaps the given
        point or range.

        Completes in O(r*log n) time, where r is the size of the
        search range.
        :rtype: bool
        )�overlaps_ranger[   r   �overlaps_pointr/   r0   �r"   r/   r0   s      r   �overlapszIntervalTree.overlaps<  sR   � � �?��&�&�u�c�2�2���v�&��&�&�u�-�-��&�&�u�{�{�E�I�I�>�>r&   c                 �l   � | j                  �       ryt        | j                  j                  |�      �      S )z�
        Returns whether some interval in the tree overlaps p.

        Completes in O(log n) time.
        :rtype: bool
        F)�is_empty�boolr   �contains_point)r"   �ps     r   r�   zIntervalTree.overlaps_pointL  s*   � � �=�=�?���D�M�M�0�0��3�4�4r&   c                 �   � ��� � j                  �       ry��k\  ry� j                  ��      ryt        ��� fd�� j                  D �       �      S )a  
        Returns whether some interval in the tree overlaps the given
        range. Returns False if given a null interval over which to
        test.

        Completes in O(r*log n) time, where r is the range length and n
        is the table size.
        :rtype: bool
        FTc              3   �\   �K  � | ]#  }�|cxk  r�k  rn n�j                  |�      �� �% y �wr)   )r�   )r*   �boundr/   r0   r"   s     ���r   r+   z.IntervalTree.overlaps_range.<locals>.<genexpr>h  s1   �� �� � 
�,���u�"�s�"� ����&�,�s   �),)r�   r�   �anyr   r�   s   ```r   r�   zIntervalTree.overlaps_rangeX  sL   �� � �=�=�?���c�\��� � ��'��� 
��,�,�
� 
� 	
r&   c           	      �0  � | syt        | j                  �      dk(  ryt        | j                  �      }t        �       }t	        |dd |dd �      D ]5  \  }}| |   D ](  }|j                  t        |||j                  �      �       �* �7 | j                  |�       y)a2  
        Finds all intervals with overlapping ranges and splits them
        along the range boundaries.

        Completes in worst-case O(n^2*log n) time (many interval
        boundaries are inside many intervals), best-case O(n*log n)
        time (small number of overlaps << n per interval).
        N�   �����r   )	rS   r   rR   r   �zipr7   r   r;   r%   )r"   �bounds�new_ivs�lbound�uboundr$   s         r   �split_overlapszIntervalTree.split_overlapsn  s�   � � ���t�"�"�#�q�(����+�+�,���%��!�&��"�+�v�a�b�z�:�N�F�F��6�l�����H�V�V�R�W�W�=�>� #� ;� 	���g�r&   c                 ��  ����	�
� | syt        | j                  �      }g �
dg�d�	����	�
fd�}|D ]�  �	�
r��
d   }�	j                  |j                  k  s|sx�	j                  |j                  k(  r_t	        |j                  �	j                  �      }�� ��d   �	j
                  �      �d<   nd�d<   t        |j                  |�d   �      �
d<   �� |�        �� |�        �� | j                  �
�       y)a�  
        Finds all intervals with overlapping ranges and merges them
        into a single interval. If provided, uses data_reducer and
        data_initializer with similar semantics to Python's built-in
        reduce(reducer_func[, initializer]), as follows:

        If data_reducer is set to a function, combines the data
        fields of the Intervals with
            current_reduced_data = data_reducer(current_reduced_data, new_data)
        If data_reducer is None, the merged Interval's data
        field will be set to None, ignoring all the data fields
        of the merged Intervals.

        On encountering the first Interval to merge, if
        data_initializer is None (default), uses the first
        Interval's data field as the first value for
        current_reduced_data. If data_initializer is not None,
        current_reduced_data is set to a shallow copy of
        data_initializer created with copy.copy(data_initializer).

        If strict is True (default), intervals are only merged if
        their ranges actually overlap; adjacent, touching intervals
        will not be merged. If strict is False, intervals are merged
        even if they are only end-to-end adjacent.

        Completes in O(n*logn) time.
        Nc                  �   �� ��!�j                   � d<   �j                  ��       y t        ��      � d<    �� d   �j                   �      � d<   �j                  t        �j                  �j
                  � d   �      �       y �Nr   �r;   �appendr
   r   r/   r0   ��current_reduced�data_initializer�data_reducer�higher�mergeds   �����r   �
new_seriesz/IntervalTree.merge_overlaps.<locals>.new_series�  �s   �� ��'�%+�[�[���"����f�%��%)�*:�%;���"�%1�/�!�2D�f�k�k�%R���"����h�v�|�|�V�Z�Z��QR�AS�T�Ur&   r�   r   �rR   r   r/   r0   �maxr;   r   r%   )r"   r�   r�   �strict�sorted_intervalsr�   �lower�upper_boundr�   r�   r�   s    ``     @@@r   �merge_overlapszIntervalTree.merge_overlaps�  s�   �� �8 ��!�$�"4�"4�5�����&����	V� 	V� '�F���r�
���L�L�5�9�9�,��6�<�<�5�9�9�#<�"%�e�i�i����"<�K�#�/�-9�/�!�:L�f�k�k�-Z���*�-1���*�!)�%�+�+�{�O�TU�DV�!W�F�2�J��L��� '�  	���f�r&   c                 �  �����	� | syt        | j                  �      }g �	dg�d������	fd�}|D ]�  ��	r}�	d   }�j                  |�      r_t        |j                  �j                  �      }�� ��d   �j
                  �      �d<   nd�d<   t        |j                  |�d   �      �	d<   �z |�        �� |�        �� | j                  �	�       y)a�  
        Finds all intervals with equal ranges and merges them
        into a single interval. If provided, uses data_reducer and
        data_initializer with similar semantics to Python's built-in
        reduce(reducer_func[, initializer]), as follows:

        If data_reducer is set to a function, combines the data
        fields of the Intervals with
            current_reduced_data = data_reducer(current_reduced_data, new_data)
        If data_reducer is None, the merged Interval's data
        field will be set to None, ignoring all the data fields
        of the merged Intervals.

        On encountering the first Interval to merge, if
        data_initializer is None (default), uses the first
        Interval's data field as the first value for
        current_reduced_data. If data_initializer is not None,
        current_reduced_data is set to a shallow copy of
        data_initiazer created with
            copy.copy(data_initializer).

        Completes in O(n*logn) time.
        Nc                  �   �� ��!�j                   � d<   �j                  ��       y t        ��      � d<    �� d   �j                   �      � d<   �j                  t        �j                  �j
                  � d   �      �       y r�   r�   r�   s   �����r   r�   z-IntervalTree.merge_equals.<locals>.new_series�  r�   r&   r�   r   )	rR   r   �range_matchesr�   r0   r;   r   r/   r%   )
r"   r�   r�   r�   r�   r�   r�   r�   r�   r�   s
    ``    @@@r   �merge_equalszIntervalTree.merge_equals�  s�   �� �0 ��!�$�"4�"4�5�����&����	V� 	V� '�F���r�
���'�'��.�"%�e�i�i����"<�K�#�/�-9�/�!�:L�f�k�k�-Z���*�-1���*�!)�%�+�+�{�O�TU�DV�!W�F�2�J��L��� '� 	���f�r&   c                 ��  ���
��� | syt        | j                  �      }g �dg�
d��
����fd�}|D ]�  ��r��d   }�j                  |j                  z
  }||k  rn|r|dk  r |�        �7t	        |j                  �j                  �      }	�� ��
d   �j
                  �      �
d<   nd�
d<   t        |j                  |	�
d   �      �d<   �� |�        �� |�        �� | j                  ��       y)a'  
        Finds all adjacent intervals with range terminals less than or equal to
        the given distance and merges them into a single interval. If provided,
        uses data_reducer and data_initializer with similar semantics to
        Python's built-in reduce(reducer_func[, initializer]), as follows:

        If data_reducer is set to a function, combines the data
        fields of the Intervals with
            current_reduced_data = data_reducer(current_reduced_data, new_data)
        If data_reducer is None, the merged Interval's data
        field will be set to None, ignoring all the data fields
        of the merged Intervals.

        On encountering the first Interval to merge, if
        data_initializer is None (default), uses the first
        Interval's data field as the first value for
        current_reduced_data. If data_initializer is not None,
        current_reduced_data is set to a shallow copy of
        data_initiazer created with
            copy.copy(data_initializer).

        If strict is True (default), only discrete intervals are merged if
        their ranges are within the given distance; overlapping intervals
        will not be merged. If strict is False, both neighbors and overlapping
        intervals are merged.

        Completes in O(n*logn) time.
        Nc                  �   �� ��!�j                   � d<   �j                  ��       y t        ��      � d<    �� d   �j                   �      � d<   �j                  t        �j                  �j
                  � d   �      �       y r�   r�   r�   s   �����r   r�   z0IntervalTree.merge_neighbors.<locals>.new_series.  r�   r&   r�   r   r�   )r"   r�   r�   �distancer�   r�   r�   r�   �marginr�   r�   r�   r�   s    ``       @@@r   �merge_neighborszIntervalTree.merge_neighbors  s�   �� �F ��!�$�"4�"4�5�����&����	V� 	V� '�F���r�
������	�	�1���X�%��&�1�*�"�� �&)�%�)�)�V�Z�Z�&@��'�3�1=�o�a�>P�RX�R]�R]�1^�O�A�.�15�O�A�.�%-�e�k�k�;��XY�HZ�%[��r�
��L���% '�( 	���f�r&   c                 �,   � t        | j                  �      S )z�
        Constructs and returns a set of all intervals in the tree.

        Completes in O(n) time.
        :rtype: set of Interval
        )r   r   r,   s    r   �itemszIntervalTree.itemsN  �   � � �4�%�%�&�&r&   c                 �   � dt        | �      k(  S )zj
        Returns whether the tree is empty.

        Completes in O(1) time.
        :rtype: bool
        r   )rS   r,   s    r   r�   zIntervalTree.is_emptyW  s   � � �C��I�~�r&   c                 �f   � | j                   }|s
t        �       S |j                  |t        �       �      S )z�
        Returns the set of all intervals that contain p.

        Completes in O(m + log n) time, where:
          * n = size of the tree
          * m = number of matches
        :rtype: set of Interval
        )r   r   �search_point�r"   r�   �roots      r   ra   zIntervalTree.at`  s,   � � �}�}����5�L�� � ��C�E�*�*r&   r�   �returnc                 �D   � | j                   }|sy|j                  |d�      S )z@
        Returns the number of intervals that contain p
        r   )r   �count_pointr�   s      r   �countPointOverlapszIntervalTree.countPointOverlapsn  s&   � � �}�}��������1�%�%r&   c                 �D   � | j                   }|sy|j                  |d�      S r�   )r   �count_point2r�   s      r   �countPointOverlaps2z IntervalTree.countPointOverlaps2w  s&   � ��}�}���� � � ��A�&�&r&   c                 �D  � d}| j                   }|��|j                  D ]*  }|j                  |cxk  r|j                  k  s�#n �&|dz  }�, ||j                  k  r|j
                  r|j
                  }n+||j                  kD  r|j                  r|j                  }n	 |S |���|S )Nr   r   )r   �s_centerr/   r0   �x_center�	left_node�
right_node)r"   r�   �res�cursorr2   s        r   �countPointOverlaps3z IntervalTree.countPointOverlaps3�  s�   � ������� � � #�O�O���>�>�Q�6�(�,�,�6��1�H�C� ,�
 �6�?�?�"�v�'7�'7��)�)���V�_�_�$��):�):��*�*��� �
�! � �  �
r&   c           	      ��  ���� | j                   }|s
t        �       S ��(�}| j                  |j                  |j                  �      S ��k\  r
t        �       S |j                  �t        �       �      }| j                  ��j                  ��      }�j                  ��      }|j                  |j                  �fd�t        ||�      D �       �      �       t        ��fd�|D �       �      }|S )a#  
        Returns the set of all intervals fully contained in the range
        [begin, end).

        Completes in O(m + k*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * k = size of the search range
        :rtype: set of Interval
        c              3   �D   �K  � | ]  }�j                  �       |   �� � y �wr)   ��keys�r*   �indexr   s     �r   r+   z'IntervalTree.envelop.<locals>.<genexpr>�  �$   �� �� � *
�6T�U�N���!�%�(�6T��   � c              3   �^   �K  � | ]$  }|j                   �k\  r|j                  �k  r|�� �& y �wr)   )r/   r0   )r*   r$   r/   r0   s     ��r   r+   z'IntervalTree.envelop.<locals>.<genexpr>�  s.   �� �� � 
��2��x�x�5� �R�V�V�s�]� ��s   �*-)r   r   rg   r/   r0   r�   r   �bisect_leftr>   �search_overlap�xrange�	r"   r/   r0   r�   r$   rz   �bound_begin�	bound_endr   s	    ``     @r   rg   zIntervalTree.envelop�  s�   �� � �}�}����5�L��;��B��<�<����"�&�&�1�1��c�\��5�L��"�"�5�#�%�0���,�,��$�0�0��7��"�.�.�s�3�	����d�)�)� *
�6<�[�)�6T�*
� 
� 	� � 
��
� 
�� �r&   c           	      �  �� | j                   }|s
t        �       S |�(|}| j                  |j                  |j                  �      S ||k\  r
t        �       S |j                  |t        �       �      }| j                  ��j                  |�      }�j                  |�      }|j                  |j                  �fd�t        ||�      D �       �      �       |S )a  
        Returns a set of all intervals overlapping the given range.

        Completes in O(m + k*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * k = size of the search range
        :rtype: set of Interval
        c              3   �D   �K  � | ]  }�j                  �       |   �� � y �wr)   r�   r�   s     �r   r+   z'IntervalTree.overlap.<locals>.<genexpr>�  r�   r�   )r   r   rb   r/   r0   r�   r   r�   r>   r�   r�   r�   s	           @r   rb   zIntervalTree.overlap�  s�   �� � �}�}����5�L��;��B��<�<����"�&�&�1�1��c�\��5�L��"�"�5�#�%�0���,�,��$�0�0��7��"�.�.�s�3�	����d�)�)� *
�6<�[�)�6T�*
� 
� 	� �r&   c                 �V   � | j                   sy| j                   j                  �       d   S )zm
        Returns the lower bound of the first interval in the tree.

        Completes in O(1) time.
        r   �r   r�   r,   s    r   r/   zIntervalTree.begin�  s*   � � �"�"���"�"�'�'�)�!�,�,r&   c                 �V   � | j                   sy| j                   j                  �       d   S )zl
        Returns the upper bound of the last interval in the tree.

        Completes in O(1) time.
        r   r�   r�   r,   s    r   r0   zIntervalTree.end�  s*   � � �"�"���"�"�'�'�)�"�-�-r&   c                 �R   � t        | j                  �       | j                  �       �      S )z�
        Returns a minimum-spanning Interval that encloses all the
        members of this IntervalTree. If the tree is empty, returns
        null Interval.
        :rtype: Interval
        )r   r/   r0   r,   s    r   �rangezIntervalTree.range�  s   � � ��
�
��d�h�h�j�1�1r&   c                 �J   � | sy| j                  �       | j                  �       z
  S )z�
        Returns the length of the minimum-spanning Interval that
        encloses all the members of this IntervalTree. If the tree
        is empty, return 0.
        r   )r0   r/   r,   s    r   �spanzIntervalTree.span�  s!   � � ���x�x�z�D�J�J�L�(�(r&   c                 �v   � | j                   r| j                   j                  |��      S d}|st        |�       y|S )z�
        ## FOR DEBUGGING ONLY ##
        Pretty-prints the structure of the tree.
        If tostring is true, prints nothing and returns a string.
        :rtype: None or str
        )�tostringz<empty IntervalTree>N)r   �print_structure�print)r"   r�   rz   s      r   r�   zIntervalTree.print_structure�  s7   � � �=�=��=�=�0�0�(�0�C�C�+�F���f���r&   c                 ��  � | j                   �r�	 | j                  j                  �       | j                   k(  sJ �	 | D ](  }t        |t        �      r�J dj                  |�      �       � | D ](  }|j                  �       s�J dj                  |�      �       � i }| D ]l  }|j                  |v r||j                  xx   d	z  cc<   nd	||j                  <   |j                  |v r||j                  xx   d	z  cc<   �^d	||j                  <   �n t        | j                  j                  �       �      t        |j                  �       �      k(  sJ d
�       �| j                  j!                  �       D ](  \  }}||   |k(  r�J dj                  |||   |�      �       � | j                  j#                  t        �       �       y| j                  rJ d�       �| j                  �J d�       �y# t        $ r�}t	        d�       t        | j                  j                  �       �      }t	        d�       	  n# t        $ r	 ddlm} Y nw xY w ||| j                   z
  �       t	        d�        || j                   |z
  �       |�d}~ww xY w)zk
        ## FOR DEBUGGING ONLY ##
        Checks the table to ensure that the invariants are held.
        z7Error: the tree and the membership set are out of sync!z(top_node.all_children() - all_intervals:r   )�pprintz(all_intervals - top_node.all_children():Nz9Error: Only Interval objects allowed in IntervalTree: {0}z=Error: Null Interval objects not allowed in IntervalTree: {0}r   zDError: boundary_table is out of sync with the intervals in the tree!z5Error: boundary_table[{0}] should be {1}, but is {2}!z&Error: boundary table should be empty!zError: top_node isn't None!)r   r   �all_children�AssertionErrorr�   r   �	NameErrorr�   r[   r   r   r   r/   r0   r   r�   r�   �verify)r"   �e�tivsr�   r$   �bound_checkrQ   �vals           r   r�   zIntervalTree.verify  sl  � �
 �����}�}�1�1�3�t�7I�7I�I�I�I�" ��!�"�h�/� ��!�6�"�:��/� � ���:�:�<� ��!�6�"�:��'� � �K����8�8�{�*�����)�Q�.�)�,-�K����)��6�6�[�(�����'�1�,�'�*+�K����'� � �t�*�*�/�/�1�2�c�+�:J�:J�:L�6M�M� -�-�-�M� !�/�/�5�5�7���S�"�3�'�3�.� 4�#�#)�6��[��-�s�$4�4�.� 8� �M�M� � ���'� �*�*� 9�8�9�*��=�=�(� .�-�.�(��y "� ��M�� �4�=�=�5�5�7�8���@�A�.��� � .�-�.���t�d�0�0�0�1��@�A��t�)�)�D�0�1�����s;   �)G �	I1�#9I,�H �I,� H2�/I,�1H2�2:I,�,I1c                 �
  ��� t        | �      dk  ryt        | �      �| j                  j                  �       ���fd�}| j                  j                  ���       |�       d�}t	        |j                  �       �      }||d<   |r|S |S )z�
        Returns a number between 0 and 1, indicating how suboptimal the tree
        is. The lower, the better. Roughly, this number represents the
        fraction of flawed Intervals in the tree.
        :rtype: float
        r�   g        c                  �4   �� ��z
  } �dz
  }| t        |�      z  S )z�
            Returns a normalized score, indicating roughly how many times
            intervals share s_center with other intervals. Output is full-scale
            from 0 to 1.
            :rtype: float
            r   )�float)�raw�maximum�m�ns     ��r   �s_center_scorez*IntervalTree.score.<locals>.s_center_scorec  s&   �� � �a�%�C��!�e�G���w��'�'r&   )�depthr�   �_cumulative)rS   r   �count_nodes�depth_scorer�   �values)r"   �full_reportr�   �report�
cumulativer�   r�   s        @@r   �scorezIntervalTree.scoreV  s�   �� � �t�9��>����I���M�M�%�%�'��		(� �]�]�.�.�q�!�4�&�(�
�� �����)�
� *��}����M��r&   c                 ��   � 	 |j                   |j                  }}|�| j                  �       }|�t        | �      S |�| j	                  �       }| j                  ||�      S # t        $ r | j                  |�      cY S w xY w)a7  
        Returns a set of all intervals overlapping the given index or
        slice.

        Completes in O(k * log(n) + m) time, where:
          * n = size of the tree
          * m = number of matches
          * k = size of the search range (this is 1 for a point)
        :rtype: set of Interval
        )�start�stopr/   r   r0   rb   �AttributeErrorra   )r"   r�   r  r  s       r   �__getitem__zIntervalTree.__getitem__y  su   � �
	"��+�+�u�z�z�4�E��}��
�
����<��t�9�$��|��x�x�z���<�<��t�,�,��� 	"��7�7�5�>�!�	"�s   �6A �#A �A:�9A:c                 �R   � | j                  |j                  |j                  |�       y)a  
        Adds a new interval to the tree. A shortcut for
        add(Interval(index.start, index.stop, value)).

        If an identical Interval object with equal range and data
        already exists, does nothing.

        Completes in O(log n) time.
        N)r<   r  r  )r"   r�   �values      r   �__setitem__zIntervalTree.__setitem__�  s   � � 	�	�	�%�+�+�u�z�z�5�1r&   c                 �&   � | j                  |�       y)z5
        Delete all items overlapping point.
        N)re   )r"   rq   s     r   �__delitem__zIntervalTree.__delitem__�  s   � � 	���E�"r&   c                 �   � || j                   v S )z�
        Returns whether item exists as an Interval in the tree.
        This method only returns True for exact matches; for
        overlaps, see the overlaps() method.

        Completes in O(1) time.
        :rtype: bool
        )r   )r"   �items     r   �__contains__zIntervalTree.__contains__�  s   � � �t�)�)�)�)r&   c                 �    � t        |||�      | v S )zz
        Shortcut for (Interval(begin, end, data) in tree).

        Completes in O(1) time.
        :rtype: bool
        r   r:   s       r   �	containsizIntervalTree.containsi�  s   � � ��s�D�)�T�1�1r&   c                 �6   � | j                   j                  �       S )z�
        Returns an iterator over all the intervals in the tree.

        Completes in O(1) time.
        :rtype: collections.Iterable[Interval]
        )r   �__iter__r,   s    r   r  zIntervalTree.__iter__�  s   � � �!�!�*�*�,�,r&   c                 �,   � t        | j                  �      S )zr
        Returns how many intervals are in the tree.

        Completes in O(1) time.
        :rtype: int
        )rS   r   r,   s    r   �__len__zIntervalTree.__len__�  r�   r&   c                 �X   � t        |t        �      xr | j                  |j                  k(  S )z�
        Whether two IntervalTrees are equal.

        Completes in O(n) time if sizes are equal; O(1) time otherwise.
        :rtype: bool
        )r[   r   r   rO   s     r   �__eq__zIntervalTree.__eq__�  s,   � � �u�l�+� 6����%�"5�"5�5�	
r&   c                 �@   � t        | �      }|sydj                  |�      S )z
        :rtype: str
        zIntervalTree()zIntervalTree({0}))rR   r   )r"   r   s     r   �__repr__zIntervalTree.__repr__�  s$   � � �T�l���#�&�-�-�c�2�2r&   c                 �:   � t         t        | j                  �      ffS )z7
        For pickle-ing.
        :rtype: tuple
        )r   rR   r   r,   s    r   �
__reduce__zIntervalTree.__reduce__�  s   � �
 �f�T�%7�%7�8�:�:�:r&   r)   )NNT)NN)NNr   T)F)C�__name__�
__module__�__qualname__�__doc__�classmethodr   r%   r
   r    r4   r7   r�   r<   �appendir>   r@   rB   rD   rF   rJ   rL   rN   rV   rY   r]   r_   re   rh   rn   rr   rt   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   ra   �intr�   r�   r�   rg   rb   r/   r0   r�   r�   r�   r�   r  r  r  r  r  r  r  �iterr  r  r  �__str__r  � r&   r   r   r   +   s�  � �E�L �!� �!�%�(6�)� *� '�* �F�4� �G��*� 7�*�8�	!��4�
!� �!���� �2 �,��,?� 	5�
�,�.?�B:�| ����J�X'��+�&�C� &�C� &�'�C� '�C� '��C� �C� �0!�F�8-�.�2�)�� F.�P �F"�.
2�#�*� 2�-� �D�'�

�3� �G�;r&   r   N)r   r2   r   �noder   �numbersr   �sortedcontainers.sorteddictr   r
   �warningsr   �collections.abcr   �ImportError�collectionsr�   r�   r�   r   r&  r&   r   �<module>r.     se   ���* � � � 2� � �'�*��
�@;�:� @;�� � '�&�'��
 � ��F��s    �= �A �A�
A�A�APK     ���YI{[q*X  *X  -   intervaltree/__pycache__/node.cpython-312.pyc�
    �A`g�X  �                   �@   � d Z ddlmZ ddlmZmZ d� Z G d� de�      Zy)a  
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Core logic: internal tree nodes.

Copyright 2013-2018 Chaim Leib Halbert
Modifications Copyright 2014 Konstantin Tretyakov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
�    )�
attrgetter)�floor�logc                 �   � t        | d�      S )z$
    log base 2
    :rtype real
    �   )r   )�nums    ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\intervaltree\node.py�l2r
      s   � �
 �s�A�;��    c                   �  � e Zd ZdZd e�       ddfd�Zed� �       Zed� �       Zed� �       Z	d� Z
d� Zd	� Zd
� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Z e�       fd�Zd� Z d� Z!d� Z"d � Z#d!� Z$d"� Z%d$d#�Z&y)%�Node)�x_center�s_center�	left_node�
right_node�depth�balanceNc                 �   � || _         t        |�      | _        || _        || _        d| _        d| _        | j                  �        y �Nr   )r   �setr   r   r   r   r   �rotate)�selfr   r   r   r   s        r	   �__init__zNode.__init__.   s;   � �
 !����H����"���$�����
�������r   c                 �4   � |j                   }t        ||g�      S )�
        :rtype : Node
        )�beginr   )�cls�interval�centers      r	   �from_intervalzNode.from_interval;   s   � �
 �����F�X�J�'�'r   c                 �D   � |syt         j                  t        |�      �      S �r   N)r   �from_sorted_intervals�sorted)r   �	intervalss     r	   �from_intervalszNode.from_intervalsC   s    � �
 ���)�)�&��*;�<�<r   c                 �B   � |syt        �       }|j                  |�      }|S r"   )r   �init_from_sorted)r   r%   �nodes      r	   r#   zNode.from_sorted_intervalsL   s&   � �
 ���v���$�$�Y�/���r   c                 ��  � |t        |�      dz     }|j                  | _        t        �       | _        g }g }|D ]s  }|j
                  | j                  k  r|j                  |�       �.|j                  | j                  kD  r|j                  |�       �Y| j                  j                  |�       �u t        j                  |�      | _
        t        j                  |�      | _        | j                  �       S )Nr   )�lenr   r   r   r   �end�append�addr   r#   r   r   r   )r   r%   �	center_iv�s_left�s_right�ks         r	   r(   zNode.init_from_sortedW   s�   � � �c�)�n��1�2�	�!��������������A��u�u����%����a� ����4�=�=�(����q�!����!�!�!�$� � �3�3�F�;����4�4�W�=����{�{�}�r   c                 �8   � |j                  | j                  �      S )z0Returns whether interval overlaps self.x_center.)�contains_pointr   �r   r   s     r	   �
center_hitzNode.center_hitj   s   � ��&�&�t�}�}�5�5r   c                 �4   � |j                   | j                  kD  S )zr
        Assuming not center_hit(interval), return which branch
        (left=0, right=1) interval is in.
        )r   r   r5   s     r	   �
hit_branchzNode.hit_branchn   s   � �
 �~�~����-�-r   c                 ��   � | j                   r| j                   j                  nd}| j                  r| j                  j                  nd}dt        ||�      z   | _        ||z
  | _        y)zU
        Recalculate self.balance and self.depth based on child node values.
        r   �   N)r   r   r   �maxr   �r   �
left_depth�right_depths      r	   �refresh_balancezNode.refresh_balanceu   sQ   � � .2�^�^�T�^�^�)�)��
�/3���d�o�o�+�+�A����Z��5�5��
�"�Z�/��r   c                 ��   � | j                   r| j                   j                  �       nd}| j                  r| j                  j                  �       nd}dt        ||�      z   S )z�
        Recursively computes true depth of the subtree. Should only
        be needed for debugging. Unless something is wrong, the
        depth field should reflect the correct depth of the subtree.
        r   r:   )r   �compute_depthr   r;   r<   s      r	   rA   zNode.compute_depth~   sJ   � � 8<�~�~�T�^�^�1�1�3�1�
�9=���d�o�o�3�3�5�a���3�z�;�/�/�/r   c                 �  � | j                  �        t        | j                  �      dk  r| S | j                  dkD  }| |   j                  dkD  }||k(  s| |   j                  dk(  r| j                  �       S | j	                  �       S )zj
        Does rotating, if necessary, to balance this node, and
        returns the new top node.
        r   r   )r?   �absr   �srotate�drotate)r   �my_heavy�child_heavys      r	   r   zNode.rotate�   s{   � �
 	�����t�|�|��q� ��K��<�<�!�#���8�n�,�,�q�0���{�"�d�8�n�&<�&<��&A� �<�<�>�!��<�<�>�!r   c                 �f  � | j                   dkD  }| }| |   }||   | |<   | j                  �       ||<   ||   j                  D �cg c]  }|j                  |�      s�|�� }}|r9|D ]  }||   j	                  |�      ||<   � |j                  j                  |�       |j                  �        |S c c}w )z-Single rotation. Assumes that balance is +-2.r   )r   r   r   r6   �remove�updater?   )r   �heavy�light�save�iv�	promoteess         r	   rD   zNode.srotate�   s�   � � ���q� ���	���E�{�� �5�k��U���k�k�m��U�� #'�u�+�"6�"6�N�"6�B�$�/�/�"�:M�R�"6�	�N����"�5�k�0�0��4��U��  �
 �M�M� � ��+�������� Os   �B.�B.c                 �   � | j                   dkD  }| |   j                  �       | |<   | j                  �        | j                  �       }|S r   )r   rD   r?   )r   rF   �results      r	   rE   zNode.drotate�   sD   � ��<�<�!�#���h��/�/�1��X������ ������r   c                 �,  � | j                  |�      r| j                  j                  |�       | S | j                  |�      }| |   s*t        j                  |�      | |<   | j                  �        | S | |   j                  |�      | |<   | j                  �       S )zG
        Returns self after adding the interval and balancing.
        )r6   r   r.   r8   r   r    r?   r   )r   r   �	directions      r	   r.   zNode.add�   s�   � � �?�?�8�$��M�M���h�'��K�����1�I��	�?�"&�"4�"4�X�">��Y���$�$�&���"&�y�/�"5�"5�h�"?��Y���{�{�}�$r   c                 �.   � g }| j                  ||d��      S )z�
        Returns self after removing the interval and balancing.

        If interval is not present, raise ValueError.
        T��should_raise_error��remove_interval_helper�r   r   �dones      r	   rI   zNode.remove�   s!   � � ���*�*�8�T�d�*�S�Sr   c                 �.   � g }| j                  ||d��      S )zv
        Returns self after removing interval and balancing.

        If interval is not present, do nothing.
        FrU   rW   rY   s      r	   �discardzNode.discard�   s!   � � ���*�*�8�T�e�*�T�Tr   c                 ��  � | j                  |�      rn|s!|| j                  vr|j                  d�       | S 	 | j                  j                  |�       | j                  r|j                  d�       | S | j                  �       S | j                  |�      }| |   s|rt        �|j                  d�       | S | |   j                  |||�      | |<   |s| j                  �       S | S #  | j	                  �        t        |�      �xY w)aU  
        Returns self after removing interval and balancing.
        If interval doesn't exist, raise ValueError.

        This method may set done to [1] to tell all callers that
        rebalancing has completed.

        See Eternally Confuzzled's jsw_remove_r function (lines 1-32)
        in his AVL tree article for reference.
        r:   )r6   r   r-   rI   �print_structure�KeyError�pruner8   �
ValueErrorrX   r   )r   r   rZ   rV   rS   s        r	   rX   zNode.remove_interval_helper�   s�   � � �?�?�8�$�%�(�$�-�-�*G����A����)� ���$�$�X�.� �}�}����A���� �:�:�<������1�I��	�?�%�$�$����A���� #�9�o�D�D�X�t�Ug�h�D��O� � �{�{�}�$��K��A)��$�$�&��x�(�(�s   �C �C;c                 �L   � t        �       }|D ]  }| j                  ||�       � |S )zD
        Returns all intervals that overlap the point_list.
        )r   �search_point)r   �
point_listrQ   �js       r	   �search_overlapzNode.search_overlap,  s*   � � ����A����a��(� ��r   c                 �  � | j                   D ]*  }|j                  |cxk  r|j                  k  s�#n �&|dz  }�, || j                  k  r| d   r| d   j	                  ||�      S || j                  kD  r| d   r| d   j	                  ||�      S |S )Nr:   r   )r   r   r,   r   �count_point�r   �pointrQ   r2   s       r	   rh   zNode.count_point5  s�   � ����A��w�w�%�(�1�5�5�(��!��� � �4�=�=� �T�!�W���7�&�&�u�f�5�5��T�]�]�"�t�A�w���7�&�&�u�f�5�5��r   c                 �T  � | j                   D ]*  }|j                  |cxk  r|j                  k  s�#n �&|dz  }�, || j                  k  r(| j                  r| j                  j                  ||�      S || j                  kD  r(| j                  r| j                  j                  ||�      S |S )Nr:   )r   r   r,   r   r   �count_point2r   )r   rj   �res�is       r	   rl   zNode.count_point2?  s�   � ����A��w�w�%�(�1�5�5�(��q��� �
 �4�=�=� �T�^�^��>�>�.�.�u�c�:�:��T�]�]�"�t����?�?�/�/��s�;�;��
r   c                 �4  � | j                   D ]6  }|j                  |cxk  r|j                  k  s�#n �&|j                  |�       �8 || j                  k  r| d   r| d   j                  ||�      S || j                  kD  r| d   r| d   j                  ||�      S |S )z;
        Returns all intervals that contain point.
        r   r:   )r   r   r,   r.   r   rc   ri   s       r	   rc   zNode.search_pointM  s�   � � ���A��w�w�%�(�1�5�5�(��
�
�1�� � �4�=�=� �T�!�W���7�'�'��v�6�6��T�]�]�"�t�A�w���7�'�'��v�6�6��r   c                 ��   � | d   r| d   s| d    }| |   }|S | d   j                  �       \  }| d<   | d   | d   c|d<   |d<   |j                  �        |j                  �       }|S )z}
        On a subtree where the root node's s_center is empty,
        return a new subtree with no empty s_centers.
        r   r:   )�pop_greatest_childr?   r   )r   rS   rQ   �heirs       r	   r`   z
Node.pruneZ  s�   � �
 �A�w�d�1�g� ��G��I�
 �)�_�F��M� !��G�6�6�8�M�D�$�q�'� #'�q�'�4��7��T�!�W�d�1�g� � � �"��;�;�=�D� �Kr   c                 �:  � �	� � j                   s�t        � j                  t        dd�      ��      }|j	                  �       }� j
                  �	|rC|j	                  �       }|j                  |j                  k(  r�,t        �	|j                  �      �	|r�C�	� fd�}t        �	 |�       �      }� xj                  |j                  z  c_        � j                  r|� fS |� d   fS � d   j                  �       \  }� d<   t        � j                  �      D ]J  }|j                  |j
                  �      s�� j                  j                  |�       |j                  |�       �L � j                  r$� j                  �        � j                  �       }||fS � j!                  �       }||fS )a  
        Used when pruning a node with both a left and a right branch.
        Returns (greatest_child, node), where:
          * greatest_child is a new node to replace the removed node.
          * node is the subtree after:
              - removing the greatest child
              - balancing
              - moving overlapping nodes into greatest_child

        Assumes that self.s_center is not empty.

        See Eternally Confuzzled's jsw_remove_r function (lines 34-54)
        in his AVL tree article for reference.
        r,   r   )�keyc               3   �\   �K  � �j                   D ]  } | j                  ��      s�| �� � y �w�N)r   r4   )rN   �new_x_centerr   s    ��r	   �get_new_s_centerz1Node.pop_greatest_child.<locals>.get_new_s_center�  s'   �� �� ��-�-�B��(�(��6�b�� (�s   �!,�,r   r:   )r   r$   r   r   �popr   r,   r;   r   rq   r   r4   rI   r.   r?   r   r`   )
r   �ivs�max_iv�next_max_ivrx   �child�greatest_childrN   �new_selfrw   s
   `        @r	   rq   zNode.pop_greatest_child�  sh  �� �  ��� ����J�u�g�,F�G�C��W�W�Y�F��=�=�L��!�g�g�i���?�?�f�j�j�0�(�"�<����A�� �A�
 ��'7�'9�:�E��M�M�U�^�^�+�M� �}�}� �d�{�"� �d�1�g�~�%� )-�Q��(B�(B�(D�%�^�T�!�W� �$�-�-�(���$�$�^�%<�%<�=��M�M�(�(��,�"�&�&�r�*� )� �}�}�
 �$�$�&��;�;�=��%�x�/�/��:�:�<��
 &�x�/�/r   c                 �   � | j                   D ]  }|j                  |�      s� y | || j                  kD     }|xr |j                  |�      S )zB
        Returns whether this node or a child overlaps p.
        T)r   r4   r   )r   �prN   �branchs       r	   r4   zNode.contains_point�  sN   � � �-�-�B�� � ��#��  � �a�$�-�-�'�(���2�&�/�/��2�2r   c                 �4   � | j                  t        �       �      S rv   )�all_children_helperr   �r   s    r	   �all_childrenzNode.all_children�  s   � ��'�'���.�.r   c                 �   � |j                  | j                  �       | d   r| d   j                  |�       | d   r| d   j                  |�       |S )Nr   r:   )rJ   r   r�   )r   rQ   s     r	   r�   zNode.all_children_helper�  sI   � ����d�m�m�$���7���G�'�'��/���7���G�'�'��/��r   c           
      ��  � t        | j                  t        �      sJ �| j                  }t	        |�      dk  s&J dj                  | j                  d��      �      �       �| j                  �        || j                  k(  s&J dj                  | j                  d��      �      �       �| j                  s&J dj                  | j                  d��      �      �       �| j                  D ]�  }t        |d�      sJ �t        |d�      sJ �|j                  |j                  k  sJ �|j                  | j                  �      sJ �t        |�      D ];  }|j                  |�      s�J d	j                  ||| j                  d��      �      �       � �� | d
   rj| d
   j                  | j                  k  s J dj                  | j                  �      �       �| d
   j                  |j!                  | j                  g�      �       | d   rk| d   j                  | j                  kD  s J dj                  | j                  �      �       �| d   j                  |j!                  | j                  g�      �       yy)zw
        ## DEBUG ONLY ##
        Recursively ensures that the invariants of an interval subtree
        hold.
        r   z5Error: Rotation should have happened, but didn't! 
{}T)�tostringz*Error: self.balance not set correctly! 
{}zError: s_center is empty! 
{}r   r,   z&Error: Overlaps ancestor ({})! 
{}

{}r   z"Error: Out-of-order left child! {}r:   z#Error: Out-of-order right child! {}N)�
isinstancer   r   r   rC   �formatr^   r?   �hasattrr   r,   �overlapsr   r$   r4   �verify�union)r   �parents�balrN   �parents        r	   r�   zNode.verify�  s:  � � �$�-�-��-�.�-��l�l���3�x�!�|� 	�D�K�K��$�$�d�$�3��	�|� 	�����d�l�l�"� 	�9�@�@��$�$�d�$�3��	�"�
 �}�}� 	�,�3�3��$�$�d�$�3��	�}� �-�-�B��2�w�'�'�'��2�u�%�%�%��8�8�b�f�f�$�$�$��;�;�t�}�}�-�-�-� ��/���,�,�V�4� �?�F�F���D�$8�$8�$�$8�$G���4� *�  � ��7���7�#�#�d�m�m�3� K�4�;�;�D�M�M�J�K�3���G�N�N�7�=�=�$�-�-��9�:���7���7�#�#�d�m�m�3� L�5�<�<�T�]�]�K�L�3���G�N�N�7�=�=�$�-�-��9�:� r   c                 �6   � |r| j                   S | j                  S )zn
        Returns the left child if input is equivalent to False, or
        the right side otherwise.
        �r   r   )r   �indexs     r	   �__getitem__zNode.__getitem__  s   � �
 ��?�?�"��>�>�!r   c                 �&   � |r|| _         y|| _        y)z%Sets the left (0) or right (1) child.Nr�   )r   rt   �values      r	   �__setitem__zNode.__setitem__  s   � ��#�D�O�"�D�Nr   c                 �d   � dj                  | j                  | j                  | j                  �      S )z�
        Shows info about this node.

        Since Nodes are internal data structures not revealed to the
        user, I'm not bothering to make this copy-paste-executable as a
        constructor.
        z!Node<{0}, depth={1}, balance={2}>)r�   r   r   r   r�   s    r	   �__str__zNode.__str__$  s,   � � 3�9�9��M�M��J�J��L�L�
� 	
r   c                 �   � d}| j                   r|| j                   j                  �       z  }| j                  r|| j                  j                  �       z  }|S )zP
        Count the number of Nodes in this subtree.
        :rtype: int
        r:   )r   �count_nodesr   )r   �counts     r	   r�   zNode.count_nodes:  sJ   � �
 ���>�>��T�^�^�/�/�1�1�E��?�?��T�_�_�0�0�2�2�E��r   c                 �   � |dk(  rydt        t        t        |�      �      �      z   }dt        d|z   |z
  �      z  }|| j	                  d|�      z  S )z�
        Calculates flaws in balancing the tree.
        :param n: size of tree
        :param m: number of Nodes in tree
        :rtype: real
        r   g        r:   )�intr   r
   �float�depth_score_helper)r   �n�m�dopt�fs        r	   �depth_scorezNode.depth_scoreF  sV   � � ��6�� �3�u�R��U�|�$�$����a�!�e�d�l�#�#���4�*�*�1�d�3�3�3r   c                 �  � ||z
  }|dkD  r|t        | j                  �      z  }nd}| j                  r"|| j                  j                  |dz   |�      z  }| j                  r"|| j                  j                  |dz   |�      z  }|S )z�
        Gets a weighted count of the number of Intervals deeper than dopt.
        :param d: current depth, starting from 0
        :param dopt: optimal maximum depth of a leaf Node
        :rtype: real
        r   r:   )r+   r   r   r�   r   )r   �dr�   �dir�   s        r	   r�   zNode.depth_score_helperU  s}   � � ��X����6���T�]�]�+�+�E��E��?�?��T�_�_�7�7��A��t�D�D�E��>�>��T�^�^�6�6�q�1�u�d�C�C�E��r   c                 �:  � d}|dz  }t        | �      |z   g}| j                  r=t        | j                  �      D ]%  }|j                  |dz   t	        |�      z   |z   �       �' | j
                  rB|j                  |dz   �       |j                  | j
                  j                  |dz   d�      �       | j                  rB|j                  |dz   �       |j                  | j                  j                  |dz   d�      �       dj                  |�      }|r|S t        |�       y	)
z 
        For debugging.
        �
z    � z<:  r:   Tz>:  � N)
�strr   r$   r-   �reprr   r^   r   �join�print)r   �indentr�   �nl�sp�rlistrN   rQ   s           r	   r^   zNode.print_structureh  s�   � � ���f�_���T��R�� ���=�=��T�]�]�+�����R�#�X��R��0�2�5�6� ,��>�>��L�L��f��%��L�L����7�7���
�D�I�J��?�?��L�L��f��%��L�L����8�8��!��T�J�K���������M��&�Mr   )r   F)'�__name__�
__module__�__qualname__�	__slots__r   r   �classmethodr    r&   r#   r(   r6   r8   r?   rA   r   rD   rE   r.   rI   r\   rX   rf   rh   rl   rc   r`   rq   r4   r�   r�   r�   r�   r�   r�   r�   r�   r�   r^   � r   r	   r   r   %   s�   � ��I� ��%�� �	� �(� �(� �=� �=� �� ���&6�.�0�0�"�2�B	�%�"	T�U�8�t����'�RM0�b3�/�� !�U� (;�T"�#�
�,
�4��&r   r   N)	�__doc__�operatorr   �mathr   r   r
   �objectr   r�   r   r	   �<module>r�      s%   ���*  � ��X	�6� X	r   PK     ���Y	�ɞ>)  >)     intervaltree/interval.py#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Interval class

Copyright 2013-2018 Chaim Leib Halbert
Modifications copyright 2014 Konstantin Tretyakov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from numbers import Number
from collections import namedtuple


# noinspection PyBroadException
class Interval(namedtuple('IntervalBase', ['begin', 'end', 'data'])):
    __slots__ = ()  # Saves memory, avoiding the need to create __dict__ for each interval

    def __new__(cls, begin, end, data=None):
        return super(Interval, cls).__new__(cls, begin, end, data)
    
    def overlaps(self, begin, end=None):
        """
        Whether the interval overlaps the given point, range or Interval.
        :param begin: beginning point of the range, or the point, or an Interval
        :param end: end point of the range. Optional if not testing ranges.
        :return: True or False
        :rtype: bool
        """
        if end is not None:
            # An overlap means that some C exists that is inside both ranges:
            #   begin <= C < end
            # and 
            #   self.begin <= C < self.end
            # See https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap/3269471#3269471
            return begin < self.end and end > self.begin
        try:
            return self.overlaps(begin.begin, begin.end)
        except:
            return self.contains_point(begin)

    def overlap_size(self, begin, end=None):
        """
        Return the overlap size between two intervals or a point
        :param begin: beginning point of the range, or the point, or an Interval
        :param end: end point of the range. Optional if not testing ranges.
        :return: Return the overlap size, None if not overlap is found
        :rtype: depends on the given input (e.g., int will be returned for int interval and timedelta for
        datetime intervals)
        """
        overlaps = self.overlaps(begin, end)
        if not overlaps:
            return 0

        if end is not None:
            # case end is given
            i0 = max(self.begin, begin)
            i1 = min(self.end, end)
            return i1 - i0
        # assume the type is interval, in other cases, an exception will be thrown
        i0 = max(self.begin, begin.begin)
        i1 = min(self.end, begin.end)
        return i1 - i0

    def contains_point(self, p):
        """
        Whether the Interval contains p.
        :param p: a point
        :return: True or False
        :rtype: bool
        """
        return self.begin <= p <= self.end
    
    def range_matches(self, other):
        """
        Whether the begins equal and the ends equal. Compare __eq__().
        :param other: Interval
        :return: True or False
        :rtype: bool
        """
        return (
            self.begin == other.begin and 
            self.end == other.end
        )
    
    def contains_interval(self, other):
        """
        Whether other is contained in this Interval.
        :param other: Interval
        :return: True or False
        :rtype: bool
        """
        return (
            self.begin <= other.begin and
            self.end >= other.end
        )
    
    def distance_to(self, other):
        """
        Returns the size of the gap between intervals, or 0 
        if they touch or overlap.
        :param other: Interval or point
        :return: distance
        :rtype: Number
        """
        if self.overlaps(other):
            return 0
        try:
            if self.begin < other.begin:
                return other.begin - self.end
            else:
                return self.begin - other.end
        except:
            if self.end <= other:
                return other - self.end
            else:
                return self.begin - other

    def is_null(self):
        """
        Whether this equals the null interval.
        :return: True if end <= begin else False
        :rtype: bool
        """
        return self.begin > self.end

    def length(self):
        """
        The distance covered by this Interval.
        :return: length
        :type: Number
        """
        if self.is_null():
            return 0
        return self.end - self.begin

    def __hash__(self):
        """
        Depends on begin and end only.
        :return: hash
        :rtype: Number
        """
        return hash((self.begin, self.end))

    def __eq__(self, other):
        """
        Whether the begins equal, the ends equal, and the data fields
        equal. Compare range_matches().
        :param other: Interval
        :return: True or False
        :rtype: bool
        """
        return (
            self.begin == other.begin and
            self.end == other.end and
            self.data == other.data
        )

    def __cmp__(self, other):
        """
        Tells whether other sorts before, after or equal to this
        Interval.

        Sorting is by begins, then by ends, then by data fields.

        If data fields are not both sortable types, data fields are
        compared alphabetically by type name.
        :param other: Interval
        :return: -1, 0, 1
        :rtype: int
        """
        s = self[0:2]
        try:
            o = other[0:2]
        except:
            o = (other,)
        if s != o:
            return -1 if s < o else 1
        try:
            if self.data == other.data:
                return 0
            return -1 if self.data < other.data else 1
        except TypeError:
            s = type(self.data).__name__
            o = type(other.data).__name__
            if s == o:
                return 0
            return -1 if s < o else 1

    def __lt__(self, other):
        """
        Less than operator. Parrots __cmp__()
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        return self.__cmp__(other) < 0

    def __gt__(self, other):
        """
        Greater than operator. Parrots __cmp__()
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        return self.__cmp__(other) > 0

    def _raise_if_null(self, other):
        """
        :raises ValueError: if either self or other is a null Interval
        """
        if self.is_null():
            raise ValueError("Cannot compare null Intervals!")
        if hasattr(other, 'is_null') and other.is_null():
            raise ValueError("Cannot compare null Intervals!")

    def lt(self, other):
        """
        Strictly less than. Returns True if no part of this Interval
        extends higher than or into other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        self._raise_if_null(other)
        return self.end <= getattr(other, 'begin', other)

    def le(self, other):
        """
        Less than or overlaps. Returns True if no part of this Interval
        extends higher than other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        self._raise_if_null(other)
        return self.end <= getattr(other, 'end', other)

    def gt(self, other):
        """
        Strictly greater than. Returns True if no part of this Interval
        extends lower than or into other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        self._raise_if_null(other)
        if hasattr(other, 'end'):
            return self.begin >= other.end
        else:
            return self.begin > other

    def ge(self, other):
        """
        Greater than or overlaps. Returns True if no part of this Interval
        extends lower than other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        self._raise_if_null(other)
        return self.begin >= getattr(other, 'begin', other)

    def _get_fields(self):
        """
        Used by str, unicode, repr and __reduce__.

        Returns only the fields necessary to reconstruct the Interval.
        :return: reconstruction info
        :rtype: tuple
        """
        if self.data is not None:
            return self.begin, self.end, self.data
        else:
            return self.begin, self.end
    
    def __repr__(self):
        """
        Executable string representation of this Interval.
        :return: string representation
        :rtype: str
        """
        if isinstance(self.begin, Number):
            s_begin = str(self.begin)
            s_end = str(self.end)
        else:
            s_begin = repr(self.begin)
            s_end = repr(self.end)
        if self.data is None:
            return "Interval({0}, {1})".format(s_begin, s_end)
        else:
            return "Interval({0}, {1}, {2})".format(s_begin, s_end, repr(self.data))

    __str__ = __repr__

    def copy(self):
        """
        Shallow copy.
        :return: copy of self
        :rtype: Interval
        """
        return Interval(self.begin, self.end, self.data)
    
    def __reduce__(self):
        """
        For pickle-ing.
        :return: pickle data
        :rtype: tuple
        """
        return Interval, self._get_fields()
PK     ˀ�Yb%�ū  ū     intervaltree/intervaltree.py

"""
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Core logic.

Copyright 2013-2018 Chaim Leib Halbert
Modifications Copyright 2014 Konstantin Tretyakov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from .interval import Interval
from .node import Node
from numbers import Number
from sortedcontainers.sorteddict import SortedDict
from copy import copy
from warnings import warn

try:
    from collections.abc import MutableSet  # Python 3?
except ImportError:
    from collections import MutableSet

try:
    xrange  # Python 2?
except NameError:  # pragma: no cover
    xrange = range


# noinspection PyBroadException
class IntervalTree(MutableSet):
    """
    A binary lookup tree of intervals.
    The intervals contained in the tree are represented using ``Interval(a, b, data)`` objects.
    Each such object represents a half-open interval ``[a, b)`` with optional data.

    Examples:
    ---------

    Initialize a blank tree::

        >>> tree = IntervalTree()
        >>> tree
        IntervalTree()

    Initialize a tree from an iterable set of Intervals in O(n * log n)::

        >>> tree = IntervalTree([Interval(-10, 10), Interval(-20.0, -10.0)])
        >>> tree
        IntervalTree([Interval(-20.0, -10.0), Interval(-10, 10)])
        >>> len(tree)
        2

    Note that this is a set, i.e. repeated intervals are ignored. However,
    Intervals with different data fields are regarded as different::

        >>> tree = IntervalTree([Interval(-10, 10), Interval(-10, 10), Interval(-10, 10, "x")])
        >>> tree
        IntervalTree([Interval(-10, 10), Interval(-10, 10, 'x')])
        >>> len(tree)
        2

    Insertions::
        >>> tree = IntervalTree()
        >>> tree[0:1] = "data"
        >>> tree.add(Interval(10, 20))
        >>> tree.addi(19.9, 20)
        >>> tree
        IntervalTree([Interval(0, 1, 'data'), Interval(10, 20), Interval(19.9, 20)])
        >>> tree.update([Interval(19.9, 20.1), Interval(20.1, 30)])
        >>> len(tree)
        5

        Inserting the same Interval twice does nothing::
            >>> tree = IntervalTree()
            >>> tree[-10:20] = "arbitrary data"
            >>> tree[-10:20] = None  # Note that this is also an insertion
            >>> tree
            IntervalTree([Interval(-10, 20), Interval(-10, 20, 'arbitrary data')])
            >>> tree[-10:20] = None  # This won't change anything
            >>> tree[-10:20] = "arbitrary data" # Neither will this
            >>> len(tree)
            2

    Deletions::
        >>> tree = IntervalTree(Interval(b, e) for b, e in [(-10, 10), (-20, -10), (10, 20)])
        >>> tree
        IntervalTree([Interval(-20, -10), Interval(-10, 10), Interval(10, 20)])
        >>> tree.remove(Interval(-10, 10))
        >>> tree
        IntervalTree([Interval(-20, -10), Interval(10, 20)])
        >>> tree.remove(Interval(-10, 10))
        Traceback (most recent call last):
        ...
        ValueError
        >>> tree.discard(Interval(-10, 10))  # Same as remove, but no exception on failure
        >>> tree
        IntervalTree([Interval(-20, -10), Interval(10, 20)])

    Delete intervals, overlapping a given point::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.1)
        >>> tree
        IntervalTree([Interval(-1.1, 1.1)])

    Delete intervals, overlapping an interval::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> tree.remove_overlap(0, 0.5)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.7, 1.8)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.6, 1.6)  # Null interval does nothing
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.6, 1.5)  # Ditto
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])

    Delete intervals, enveloped in the range::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> tree.remove_envelop(-1.0, 1.5)
        >>> tree
        IntervalTree([Interval(-1.1, 1.1), Interval(0.5, 1.7)])
        >>> tree.remove_envelop(-1.1, 1.5)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_envelop(0.5, 1.5)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_envelop(0.5, 1.7)
        >>> tree
        IntervalTree()

    Point queries::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree[-1.1]   == set([Interval(-1.1, 1.1)])
        >>> assert tree.at(1.1) == set([Interval(-0.5, 1.5), Interval(0.5, 1.7)])   # Same as tree[1.1]
        >>> assert tree.at(1.5) == set([Interval(0.5, 1.7)])                        # Same as tree[1.5]

    Interval overlap queries

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree.overlap(1.7, 1.8) == set()
        >>> assert tree.overlap(1.5, 1.8) == set([Interval(0.5, 1.7)])
        >>> assert tree[1.5:1.8] == set([Interval(0.5, 1.7)])                       # same as previous
        >>> assert tree.overlap(1.1, 1.8) == set([Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree[1.1:1.8] == set([Interval(-0.5, 1.5), Interval(0.5, 1.7)])  # same as previous

    Interval envelop queries::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree.envelop(-0.5, 0.5) == set()
        >>> assert tree.envelop(-0.5, 1.5) == set([Interval(-0.5, 1.5)])

    Membership queries::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> Interval(-0.5, 0.5) in tree
        False
        >>> Interval(-1.1, 1.1) in tree
        True
        >>> Interval(-1.1, 1.1, "x") in tree
        False
        >>> tree.overlaps(-1.1)
        True
        >>> tree.overlaps(1.7)
        False
        >>> tree.overlaps(1.7, 1.8)
        False
        >>> tree.overlaps(-1.2, -1.1)
        False
        >>> tree.overlaps(-1.2, -1.0)
        True

    Sizing::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> len(tree)
        3
        >>> tree.is_empty()
        False
        >>> IntervalTree().is_empty()
        True
        >>> not tree
        False
        >>> not IntervalTree()
        True
        >>> print(tree.begin())    # using print() because of floats in Python 2.6
        -1.1
        >>> print(tree.end())      # ditto
        1.7

    Iteration::

        >>> tree = IntervalTree([Interval(-11, 11), Interval(-5, 15), Interval(5, 17)])
        >>> [iv.begin for iv in sorted(tree)]
        [-11, -5, 5]
        >>> assert tree.items() == set([Interval(-5, 15), Interval(-11, 11), Interval(5, 17)])

    Copy- and typecasting, pickling::

        >>> tree0 = IntervalTree([Interval(0, 1, "x"), Interval(1, 2, ["x"])])
        >>> tree1 = IntervalTree(tree0)  # Shares Interval objects
        >>> tree2 = tree0.copy()         # Shallow copy (same as above, as Intervals are singletons)
        >>> import pickle
        >>> tree3 = pickle.loads(pickle.dumps(tree0))  # Deep copy
        >>> list(tree0[1])[0].data[0] = "y"  # affects shallow copies, but not deep copies
        >>> tree0
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['y'])])
        >>> tree1
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['y'])])
        >>> tree2
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['y'])])
        >>> tree3
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['x'])])

    Equality testing::

        >>> IntervalTree([Interval(0, 1)]) == IntervalTree([Interval(0, 1)])
        True
        >>> IntervalTree([Interval(0, 1)]) == IntervalTree([Interval(0, 1, "x")])
        False
    """
    @classmethod
    def from_tuples(cls, tups):
        """
        Create a new IntervalTree from an iterable of 2- or 3-tuples,
         where the tuple lists begin, end, and optionally data.
        """
        ivs = [Interval(*t) for t in tups]
        return IntervalTree(ivs)

    def __init__(self, intervals=None):
        """
        Set up a tree. If intervals is provided, add all the intervals
        to the tree.

        Completes in O(n*log n) time.
        """
        intervals = set(intervals) if intervals is not None else set()
        for iv in intervals:
            if iv.is_null():
                raise ValueError(
                    "IntervalTree: Null Interval objects not allowed in IntervalTree:"
                    " {0}".format(iv)
                )
        self.all_intervals = intervals
        self.top_node = Node.from_intervals(self.all_intervals)
        self.boundary_table = SortedDict()
        for iv in self.all_intervals:
            self._add_boundaries(iv)

    def copy(self):
        """
        Construct a new IntervalTree using shallow copies of the
        intervals in the source tree.

        Completes in O(n*log n) time.
        :rtype: IntervalTree
        """
        return IntervalTree(iv.copy() for iv in self)

    def _add_boundaries(self, interval):
        """
        Records the boundaries of the interval in the boundary table.
        """
        begin = interval.begin
        end = interval.end
        if begin in self.boundary_table:
            self.boundary_table[begin] += 1
        else:
            self.boundary_table[begin] = 1

        if end in self.boundary_table:
            self.boundary_table[end] += 1
        else:
            self.boundary_table[end] = 1

    def _remove_boundaries(self, interval):
        """
        Removes the boundaries of the interval from the boundary table.
        """
        begin = interval.begin
        end = interval.end
        if self.boundary_table[begin] == 1:
            del self.boundary_table[begin]
        else:
            self.boundary_table[begin] -= 1

        if self.boundary_table[end] == 1:
            del self.boundary_table[end]
        else:
            self.boundary_table[end] -= 1

    def add(self, interval):
        """
        Adds an interval to the tree, if not already present.

        Completes in O(log n) time.
        """
        if interval in self:
            return

        if interval.is_null():
            raise ValueError(
                "IntervalTree: Null Interval objects not allowed in IntervalTree:"
                " {0}".format(interval)
            )

        if not self.top_node:
            self.top_node = Node.from_interval(interval)
        else:
            self.top_node = self.top_node.add(interval)
        self.all_intervals.add(interval)
        self._add_boundaries(interval)
    append = add

    def addi(self, begin, end, data=None):
        """
        Shortcut for add(Interval(begin, end, data)).

        Completes in O(log n) time.
        """
        return self.add(Interval(begin, end, data))
    appendi = addi

    def update(self, intervals):
        """
        Given an iterable of intervals, add them to the tree.

        Completes in O(m*log(n+m), where m = number of intervals to
        add.
        """
        for iv in intervals:
            self.add(iv)

    def remove(self, interval):
        """
        Removes an interval from the tree, if present. If not, raises
        ValueError.

        Completes in O(log n) time.
        """
        #self.verify()
        if interval not in self:
            #print(self.all_intervals)
            raise ValueError
        self.top_node = self.top_node.remove(interval)
        self.all_intervals.remove(interval)
        self._remove_boundaries(interval)
        #self.verify()

    def removei(self, begin, end, data=None):
        """
        Shortcut for remove(Interval(begin, end, data)).

        Completes in O(log n) time.
        """
        return self.remove(Interval(begin, end, data))

    def discard(self, interval):
        """
        Removes an interval from the tree, if present. If not, does
        nothing.

        Completes in O(log n) time.
        """
        if interval not in self:
            return
        self.all_intervals.discard(interval)
        self.top_node = self.top_node.discard(interval)
        self._remove_boundaries(interval)

    def discardi(self, begin, end, data=None):
        """
        Shortcut for discard(Interval(begin, end, data)).

        Completes in O(log n) time.
        """
        return self.discard(Interval(begin, end, data))

    def difference(self, other):
        """
        Returns a new tree, comprising all intervals in self but not
        in other.
        """
        ivs = set()
        for iv in self:
            if iv not in other:
                ivs.add(iv)
        return IntervalTree(ivs)

    def difference_update(self, other):
        """
        Removes all intervals in other from self.
        """
        for iv in other:
            self.discard(iv)

    def union(self, other):
        """
        Returns a new tree, comprising all intervals from self
        and other.
        """
        return IntervalTree(set(self).union(other))

    def intersection(self, other):
        """
        Returns a new tree of all intervals common to both self and
        other.
        """
        ivs = set()
        shorter, longer = sorted([self, other], key=len)
        for iv in shorter:
            if iv in longer:
                ivs.add(iv)
        return IntervalTree(ivs)

    def intersection_update(self, other):
        """
        Removes intervals from self unless they also exist in other.
        """
        ivs = list(self)
        for iv in ivs:
            if iv not in other:
                self.remove(iv)

    def symmetric_difference(self, other):
        """
        Return a tree with elements only in self or other but not
        both.
        """
        if not isinstance(other, set): other = set(other)
        me = set(self)
        ivs = me.difference(other).union(other.difference(me))
        return IntervalTree(ivs)

    def symmetric_difference_update(self, other):
        """
        Throws out all intervals except those only in self or other,
        not both.
        """
        other = set(other)
        ivs = list(self)
        for iv in ivs:
            if iv in other:
                self.remove(iv)
                other.remove(iv)
        self.update(other)

    def remove_overlap(self, begin, end=None):
        """
        Removes all intervals overlapping the given point or range.

        Completes in O((r+m)*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * r = size of the search range (this is 1 for a point)
        """
        hitlist = self.at(begin) if end is None else self.overlap(begin, end)
        for iv in hitlist:
            self.remove(iv)

    def remove_envelop(self, begin, end):
        """
        Removes all intervals completely enveloped in the given range.

        Completes in O((r+m)*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * r = size of the search range
        """
        hitlist = self.envelop(begin, end)
        for iv in hitlist:
            self.remove(iv)

    def chop(self, begin, end, datafunc=None):
        """
        Like remove_envelop(), but trims back Intervals hanging into
        the chopped area so that nothing overlaps.
        """
        insertions = set()
        begin_hits = [iv for iv in self.at(begin) if iv.begin < begin]
        end_hits = [iv for iv in self.at(end) if iv.end > end]

        if datafunc:
            for iv in begin_hits:
                insertions.add(Interval(iv.begin, begin, datafunc(iv, True)))
            for iv in end_hits:
                insertions.add(Interval(end, iv.end, datafunc(iv, False)))
        else:
            for iv in begin_hits:
                insertions.add(Interval(iv.begin, begin, iv.data))
            for iv in end_hits:
                insertions.add(Interval(end, iv.end, iv.data))

        self.remove_envelop(begin, end)
        self.difference_update(begin_hits)
        self.difference_update(end_hits)
        self.update(insertions)

    def slice(self, point, datafunc=None):
        """
        Split Intervals that overlap point into two new Intervals. if
        specified, uses datafunc(interval, islower=True/False) to
        set the data field of the new Intervals.
        :param point: where to slice
        :param datafunc(interval, isupper): callable returning a new
        value for the interval's data field
        """
        hitlist = set(iv for iv in self.at(point) if iv.begin < point)
        insertions = set()
        if datafunc:
            for iv in hitlist:
                insertions.add(Interval(iv.begin, point, datafunc(iv, True)))
                insertions.add(Interval(point, iv.end, datafunc(iv, False)))
        else:
            for iv in hitlist:
                insertions.add(Interval(iv.begin, point, iv.data))
                insertions.add(Interval(point, iv.end, iv.data))
        self.difference_update(hitlist)
        self.update(insertions)

    def clear(self):
        """
        Empties the tree.

        Completes in O(1) tine.
        """
        self.__init__()

    def find_nested(self):
        """
        Returns a dictionary mapping parent intervals to sets of
        intervals overlapped by and contained in the parent.

        Completes in O(n^2) time.
        :rtype: dict of [Interval, set of Interval]
        """
        result = {}

        def add_if_nested():
            if parent.contains_interval(child):
                if parent not in result:
                    result[parent] = set()
                result[parent].add(child)

        long_ivs = sorted(self.all_intervals, key=Interval.length, reverse=True)
        for i, parent in enumerate(long_ivs):
            for child in long_ivs[i + 1:]:
                add_if_nested()
        return result

    def overlaps(self, begin, end=None):
        """
        Returns whether some interval in the tree overlaps the given
        point or range.

        Completes in O(r*log n) time, where r is the size of the
        search range.
        :rtype: bool
        """
        if end is not None:
            return self.overlaps_range(begin, end)
        elif isinstance(begin, Number):
            return self.overlaps_point(begin)
        else:
            return self.overlaps_range(begin.begin, begin.end)

    def overlaps_point(self, p):
        """
        Returns whether some interval in the tree overlaps p.

        Completes in O(log n) time.
        :rtype: bool
        """
        if self.is_empty():
            return False
        return bool(self.top_node.contains_point(p))

        
    def overlaps_range(self, begin, end):
        """
        Returns whether some interval in the tree overlaps the given
        range. Returns False if given a null interval over which to
        test.

        Completes in O(r*log n) time, where r is the range length and n
        is the table size.
        :rtype: bool
        """
        if self.is_empty():
            return False
        elif begin >= end:
            return False
        elif self.overlaps_point(begin):
            return True
        return any(
            self.overlaps_point(bound)
            for bound in self.boundary_table
            if begin < bound < end
        )

    def split_overlaps(self):
        """
        Finds all intervals with overlapping ranges and splits them
        along the range boundaries.

        Completes in worst-case O(n^2*log n) time (many interval
        boundaries are inside many intervals), best-case O(n*log n)
        time (small number of overlaps << n per interval).
        """
        if not self:
            return
        if len(self.boundary_table) == 2:
            return

        bounds = sorted(self.boundary_table)  # get bound locations

        new_ivs = set()
        for lbound, ubound in zip(bounds[:-1], bounds[1:]):
            for iv in self[lbound]:
                new_ivs.add(Interval(lbound, ubound, iv.data))

        self.__init__(new_ivs)

    def merge_overlaps(self, data_reducer=None, data_initializer=None, strict=True):
        """
        Finds all intervals with overlapping ranges and merges them
        into a single interval. If provided, uses data_reducer and
        data_initializer with similar semantics to Python's built-in
        reduce(reducer_func[, initializer]), as follows:

        If data_reducer is set to a function, combines the data
        fields of the Intervals with
            current_reduced_data = data_reducer(current_reduced_data, new_data)
        If data_reducer is None, the merged Interval's data
        field will be set to None, ignoring all the data fields
        of the merged Intervals.

        On encountering the first Interval to merge, if
        data_initializer is None (default), uses the first
        Interval's data field as the first value for
        current_reduced_data. If data_initializer is not None,
        current_reduced_data is set to a shallow copy of
        data_initializer created with copy.copy(data_initializer).

        If strict is True (default), intervals are only merged if
        their ranges actually overlap; adjacent, touching intervals
        will not be merged. If strict is False, intervals are merged
        even if they are only end-to-end adjacent.

        Completes in O(n*logn) time.
        """
        if not self:
            return

        sorted_intervals = sorted(self.all_intervals)  # get sorted intervals
        merged = []
        # use mutable object to allow new_series() to modify it
        current_reduced = [None]
        higher = None  # iterating variable, which new_series() needs access to

        def new_series():
            if data_initializer is None:
                current_reduced[0] = higher.data
                merged.append(higher)
                return
            else:  # data_initializer is not None
                current_reduced[0] = copy(data_initializer)
                current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                merged.append(Interval(higher.begin, higher.end, current_reduced[0]))

        for higher in sorted_intervals:
            if merged:  # series already begun
                lower = merged[-1]
                if (higher.begin < lower.end or
                    not strict and higher.begin == lower.end):  # should merge
                    upper_bound = max(lower.end, higher.end)
                    if data_reducer is not None:
                        current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                    else:  # annihilate the data, since we don't know how to merge it
                        current_reduced[0] = None
                    merged[-1] = Interval(lower.begin, upper_bound, current_reduced[0])
                else:
                    new_series()
            else:  # not merged; is first of Intervals to merge
                new_series()

        self.__init__(merged)

    def merge_equals(self, data_reducer=None, data_initializer=None):
        """
        Finds all intervals with equal ranges and merges them
        into a single interval. If provided, uses data_reducer and
        data_initializer with similar semantics to Python's built-in
        reduce(reducer_func[, initializer]), as follows:

        If data_reducer is set to a function, combines the data
        fields of the Intervals with
            current_reduced_data = data_reducer(current_reduced_data, new_data)
        If data_reducer is None, the merged Interval's data
        field will be set to None, ignoring all the data fields
        of the merged Intervals.

        On encountering the first Interval to merge, if
        data_initializer is None (default), uses the first
        Interval's data field as the first value for
        current_reduced_data. If data_initializer is not None,
        current_reduced_data is set to a shallow copy of
        data_initiazer created with
            copy.copy(data_initializer).

        Completes in O(n*logn) time.
        """
        if not self:
            return

        sorted_intervals = sorted(self.all_intervals)  # get sorted intervals
        merged = []
        # use mutable object to allow new_series() to modify it
        current_reduced = [None]
        higher = None  # iterating variable, which new_series() needs access to

        def new_series():
            if data_initializer is None:
                current_reduced[0] = higher.data
                merged.append(higher)
                return
            else:  # data_initializer is not None
                current_reduced[0] = copy(data_initializer)
                current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                merged.append(Interval(higher.begin, higher.end, current_reduced[0]))

        for higher in sorted_intervals:
            if merged:  # series already begun
                lower = merged[-1]
                if higher.range_matches(lower):  # should merge
                    upper_bound = max(lower.end, higher.end)
                    if data_reducer is not None:
                        current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                    else:  # annihilate the data, since we don't know how to merge it
                        current_reduced[0] = None
                    merged[-1] = Interval(lower.begin, upper_bound, current_reduced[0])
                else:
                    new_series()
            else:  # not merged; is first of Intervals to merge
                new_series()

        self.__init__(merged)

    def merge_neighbors(
        self,
        data_reducer=None,
        data_initializer=None,
        distance=1,
        strict=True,
    ):
        """
        Finds all adjacent intervals with range terminals less than or equal to
        the given distance and merges them into a single interval. If provided,
        uses data_reducer and data_initializer with similar semantics to
        Python's built-in reduce(reducer_func[, initializer]), as follows:

        If data_reducer is set to a function, combines the data
        fields of the Intervals with
            current_reduced_data = data_reducer(current_reduced_data, new_data)
        If data_reducer is None, the merged Interval's data
        field will be set to None, ignoring all the data fields
        of the merged Intervals.

        On encountering the first Interval to merge, if
        data_initializer is None (default), uses the first
        Interval's data field as the first value for
        current_reduced_data. If data_initializer is not None,
        current_reduced_data is set to a shallow copy of
        data_initiazer created with
            copy.copy(data_initializer).

        If strict is True (default), only discrete intervals are merged if
        their ranges are within the given distance; overlapping intervals
        will not be merged. If strict is False, both neighbors and overlapping
        intervals are merged.

        Completes in O(n*logn) time.
        """
        if not self:
            return

        sorted_intervals = sorted(self.all_intervals)  # get sorted intervals
        merged = []
        # use mutable object to allow new_series() to modify it
        current_reduced = [None]
        higher = None  # iterating variable, which new_series() needs access to

        def new_series():
            if data_initializer is None:
                current_reduced[0] = higher.data
                merged.append(higher)
                return
            else:  # data_initializer is not None
                current_reduced[0] = copy(data_initializer)
                current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                merged.append(Interval(higher.begin, higher.end, current_reduced[0]))

        for higher in sorted_intervals:
            if merged:  # series already begun
                lower = merged[-1]
                margin = higher.begin - lower.end
                if margin <= distance:  # should merge
                    if strict and margin < 0:
                        new_series()
                        continue
                    else:
                        upper_bound = max(lower.end, higher.end)
                        if data_reducer is not None:
                            current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                        else:  # annihilate the data, since we don't know how to merge it
                            current_reduced[0] = None
                        merged[-1] = Interval(lower.begin, upper_bound, current_reduced[0])
                else:
                    new_series()
            else:  # not merged; is first of Intervals to merge
                new_series()

        self.__init__(merged)

    def items(self):
        """
        Constructs and returns a set of all intervals in the tree.

        Completes in O(n) time.
        :rtype: set of Interval
        """
        return set(self.all_intervals)

    def is_empty(self):
        """
        Returns whether the tree is empty.

        Completes in O(1) time.
        :rtype: bool
        """
        return 0 == len(self)

    def at(self, p):
        """
        Returns the set of all intervals that contain p.

        Completes in O(m + log n) time, where:
          * n = size of the tree
          * m = number of matches
        :rtype: set of Interval
        """
        root = self.top_node
        if not root:
            return set()
        return root.search_point(p, set())
    
    def countPointOverlaps(self, p: int) -> int:
        """
        Returns the number of intervals that contain p
        """
        root = self.top_node
        if not root:
            return 0
        return root.count_point(p, 0)
        
    def countPointOverlaps2(self, p:int) -> int:
        root = self.top_node
        
        if not root:
            return 0
        
        # now go down the tree looking at the nodes
        return root.count_point2(p, 0)

    def countPointOverlaps3(self, p:int) -> int:
        res = 0
        cursor = self.top_node
        
        # go down the tree looking for xValue
        while cursor is not None:
            
            # print(f"looking for {p} in {cursor.x_center}")
            for interval in cursor.s_center:
                # print(f"checking {interval}")
                if interval.begin <= p <= interval.end:
                    res += 1

            if p < cursor.x_center and cursor.left_node:
                cursor = cursor.left_node
            elif p > cursor.x_center and cursor.right_node:
                cursor = cursor.right_node
            else: break

            
        
        return res


    def envelop(self, begin, end=None):
        """
        Returns the set of all intervals fully contained in the range
        [begin, end).

        Completes in O(m + k*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * k = size of the search range
        :rtype: set of Interval
        """
        root = self.top_node
        if not root:
            return set()
        if end is None:
            iv = begin
            return self.envelop(iv.begin, iv.end)
        elif begin >= end:
            return set()
        result = root.search_point(begin, set()) # bound_begin might be greater
        boundary_table = self.boundary_table
        bound_begin = boundary_table.bisect_left(begin)
        bound_end = boundary_table.bisect_left(end)  # up to, but not including end
        result.update(root.search_overlap(
            # slice notation is slightly slower
            boundary_table.keys()[index] for index in xrange(bound_begin, bound_end)
        ))

        # TODO: improve envelop() to use node info instead of less-efficient filtering
        result = set(
            iv for iv in result
            if iv.begin >= begin and iv.end <= end
        )
        return result

    def overlap(self, begin, end=None):
        """
        Returns a set of all intervals overlapping the given range.

        Completes in O(m + k*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * k = size of the search range
        :rtype: set of Interval
        """
        root = self.top_node
        if not root:
            return set()
        if end is None:
            iv = begin
            return self.overlap(iv.begin, iv.end)
        elif begin >= end:
            return set()
        result = root.search_point(begin, set())  # bound_begin might be greater
        boundary_table = self.boundary_table
        bound_begin = boundary_table.bisect_left(begin)
        bound_end = boundary_table.bisect_left(end)  # up to, but not including end
        result.update(root.search_overlap(
            # slice notation is slightly slower
            boundary_table.keys()[index] for index in xrange(bound_begin, bound_end)
        ))
        return result

    def begin(self):
        """
        Returns the lower bound of the first interval in the tree.

        Completes in O(1) time.
        """
        if not self.boundary_table:
            return 0
        return self.boundary_table.keys()[0]

    def end(self):
        """
        Returns the upper bound of the last interval in the tree.

        Completes in O(1) time.
        """
        if not self.boundary_table:
            return 0
        return self.boundary_table.keys()[-1]

    def range(self):
        """
        Returns a minimum-spanning Interval that encloses all the
        members of this IntervalTree. If the tree is empty, returns
        null Interval.
        :rtype: Interval
        """
        return Interval(self.begin(), self.end())

    def span(self):
        """
        Returns the length of the minimum-spanning Interval that
        encloses all the members of this IntervalTree. If the tree
        is empty, return 0.
        """
        if not self:
            return 0
        return self.end() - self.begin()

    def print_structure(self, tostring=False):
        """
        ## FOR DEBUGGING ONLY ##
        Pretty-prints the structure of the tree.
        If tostring is true, prints nothing and returns a string.
        :rtype: None or str
        """
        if self.top_node:
            return self.top_node.print_structure(tostring=tostring)
        else:
            result = "<empty IntervalTree>"
            if not tostring:
                print(result)
            else:
                return result

    def verify(self):
        """
        ## FOR DEBUGGING ONLY ##
        Checks the table to ensure that the invariants are held.
        """
        if self.all_intervals:
            ## top_node.all_children() == self.all_intervals
            try:
                assert self.top_node.all_children() == self.all_intervals
            except AssertionError as e:
                print(
                    'Error: the tree and the membership set are out of sync!'
                )
                tivs = set(self.top_node.all_children())
                print('top_node.all_children() - all_intervals:')
                try:
                    pprint
                except NameError:
                    from pprint import pprint
                pprint(tivs - self.all_intervals)
                print('all_intervals - top_node.all_children():')
                pprint(self.all_intervals - tivs)
                raise e

            ## All members are Intervals
            for iv in self:
                assert isinstance(iv, Interval), (
                    "Error: Only Interval objects allowed in IntervalTree:"
                    " {0}".format(iv)
                )

            ## No null intervals
            for iv in self:
                assert not iv.is_null(), (
                    "Error: Null Interval objects not allowed in IntervalTree:"
                    " {0}".format(iv)
                )

            ## Reconstruct boundary_table
            bound_check = {}
            for iv in self:
                if iv.begin in bound_check:
                    bound_check[iv.begin] += 1
                else:
                    bound_check[iv.begin] = 1
                if iv.end in bound_check:
                    bound_check[iv.end] += 1
                else:
                    bound_check[iv.end] = 1

            ## Reconstructed boundary table (bound_check) ==? boundary_table
            assert set(self.boundary_table.keys()) == set(bound_check.keys()),\
                'Error: boundary_table is out of sync with ' \
                'the intervals in the tree!'

            # For efficiency reasons this should be iteritems in Py2, but we
            # don't care much for efficiency in debug methods anyway.
            for key, val in self.boundary_table.items():
                assert bound_check[key] == val, \
                    'Error: boundary_table[{0}] should be {1},' \
                    ' but is {2}!'.format(
                        key, bound_check[key], val)

            ## Internal tree structure
            self.top_node.verify(set())
        else:
            ## Verify empty tree
            assert not self.boundary_table, \
                "Error: boundary table should be empty!"
            assert self.top_node is None, \
                "Error: top_node isn't None!"

    def score(self, full_report=False):
        """
        Returns a number between 0 and 1, indicating how suboptimal the tree
        is. The lower, the better. Roughly, this number represents the
        fraction of flawed Intervals in the tree.
        :rtype: float
        """
        if len(self) <= 2:
            return 0.0

        n = len(self)
        m = self.top_node.count_nodes()

        def s_center_score():
            """
            Returns a normalized score, indicating roughly how many times
            intervals share s_center with other intervals. Output is full-scale
            from 0 to 1.
            :rtype: float
            """
            raw = n - m
            maximum = n - 1
            return raw / float(maximum)

        report = {
            "depth": self.top_node.depth_score(n, m),
            "s_center": s_center_score(),
        }
        cumulative = max(report.values())
        report["_cumulative"] = cumulative
        if full_report:
            return report
        return cumulative


    def __getitem__(self, index):
        """
        Returns a set of all intervals overlapping the given index or
        slice.

        Completes in O(k * log(n) + m) time, where:
          * n = size of the tree
          * m = number of matches
          * k = size of the search range (this is 1 for a point)
        :rtype: set of Interval
        """
        try:
            start, stop = index.start, index.stop
            if start is None:
                start = self.begin()
                if stop is None:
                    return set(self)
            if stop is None:
                stop = self.end()
            return self.overlap(start, stop)
        except AttributeError:
            return self.at(index)

    def __setitem__(self, index, value):
        """
        Adds a new interval to the tree. A shortcut for
        add(Interval(index.start, index.stop, value)).

        If an identical Interval object with equal range and data
        already exists, does nothing.

        Completes in O(log n) time.
        """
        self.addi(index.start, index.stop, value)

    def __delitem__(self, point):
        """
        Delete all items overlapping point.
        """
        self.remove_overlap(point)

    def __contains__(self, item):
        """
        Returns whether item exists as an Interval in the tree.
        This method only returns True for exact matches; for
        overlaps, see the overlaps() method.

        Completes in O(1) time.
        :rtype: bool
        """
        # Removed point-checking code; it might trick the user into
        # thinking that this is O(1), which point-checking isn't.
        #if isinstance(item, Interval):
        return item in self.all_intervals
        #else:
        #    return self.contains_point(item)

    def containsi(self, begin, end, data=None):
        """
        Shortcut for (Interval(begin, end, data) in tree).

        Completes in O(1) time.
        :rtype: bool
        """
        return Interval(begin, end, data) in self

    def __iter__(self):
        """
        Returns an iterator over all the intervals in the tree.

        Completes in O(1) time.
        :rtype: collections.Iterable[Interval]
        """
        return self.all_intervals.__iter__()
    iter = __iter__

    def __len__(self):
        """
        Returns how many intervals are in the tree.

        Completes in O(1) time.
        :rtype: int
        """
        return len(self.all_intervals)

    def __eq__(self, other):
        """
        Whether two IntervalTrees are equal.

        Completes in O(n) time if sizes are equal; O(1) time otherwise.
        :rtype: bool
        """
        return (
            isinstance(other, IntervalTree) and
            self.all_intervals == other.all_intervals
        )

    def __repr__(self):
        """
        :rtype: str
        """
        ivs = sorted(self)
        if not ivs:
            return "IntervalTree()"
        else:
            return "IntervalTree({0})".format(ivs)

    __str__ = __repr__

    def __reduce__(self):
        """
        For pickle-ing.
        :rtype: tuple
        """
        return IntervalTree, (sorted(self.all_intervals),)

PK     ˀ�Y��_I(-  (-     intervaltree/LICENSE.txt
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
PK     ˀ�Y/����X  �X     intervaltree/node.py#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Core logic: internal tree nodes.

Copyright 2013-2018 Chaim Leib Halbert
Modifications Copyright 2014 Konstantin Tretyakov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from operator import attrgetter
from math import floor, log


def l2(num):
    """
    log base 2
    :rtype real
    """
    return log(num, 2)


class Node(object):
    __slots__ = (
        'x_center',
        's_center',
        'left_node',
        'right_node',
        'depth',
        'balance'
    )
    def __init__(self,
                 x_center=None,
                 s_center=set(),
                 left_node=None,
                 right_node=None):
        self.x_center = x_center
        self.s_center = set(s_center)
        self.left_node = left_node
        self.right_node = right_node
        self.depth = 0    # will be set when rotated
        self.balance = 0  # ditto
        self.rotate()

    @classmethod
    def from_interval(cls, interval):
        """
        :rtype : Node
        """
        center = interval.begin
        return Node(center, [interval])

    @classmethod
    def from_intervals(cls, intervals):
        """
        :rtype : Node
        """
        if not intervals:
            return None
        return Node.from_sorted_intervals(sorted(intervals))

    @classmethod
    def from_sorted_intervals(cls, intervals):
        """
        :rtype : Node
        """
        if not intervals:
            return None
        node = Node()
        node = node.init_from_sorted(intervals)
        return node

    def init_from_sorted(self, intervals):
        # assumes that intervals is a non-empty collection.
        # Else, next line raises IndexError
        center_iv = intervals[len(intervals) // 2]
        self.x_center = center_iv.begin
        self.s_center = set()
        s_left = []
        s_right = []
        for k in intervals:
            if k.end <= self.x_center:
                s_left.append(k)
            elif k.begin > self.x_center:
                s_right.append(k)
            else:
                self.s_center.add(k)
        self.left_node = Node.from_sorted_intervals(s_left)
        self.right_node = Node.from_sorted_intervals(s_right)
        return self.rotate()

    def center_hit(self, interval):
        """Returns whether interval overlaps self.x_center."""
        return interval.contains_point(self.x_center)

    def hit_branch(self, interval):
        """
        Assuming not center_hit(interval), return which branch
        (left=0, right=1) interval is in.
        """
        return interval.begin > self.x_center

    def refresh_balance(self):
        """
        Recalculate self.balance and self.depth based on child node values.
        """
        left_depth = self.left_node.depth if self.left_node else 0
        right_depth = self.right_node.depth if self.right_node else 0
        self.depth = 1 + max(left_depth, right_depth)
        self.balance = right_depth - left_depth

    def compute_depth(self):
        """
        Recursively computes true depth of the subtree. Should only
        be needed for debugging. Unless something is wrong, the
        depth field should reflect the correct depth of the subtree.
        """
        left_depth = self.left_node.compute_depth() if self.left_node else 0
        right_depth = self.right_node.compute_depth() if self.right_node else 0
        return 1 + max(left_depth, right_depth)

    def rotate(self):
        """
        Does rotating, if necessary, to balance this node, and
        returns the new top node.
        """
        self.refresh_balance()
        if abs(self.balance) < 2:
            return self
        # balance > 0  is the heavy side
        my_heavy = self.balance > 0
        child_heavy = self[my_heavy].balance > 0
        if my_heavy == child_heavy or self[my_heavy].balance == 0:
            ## Heavy sides same
            #    self     save
            #  save   -> 1   self
            # 1
            #
            ## Heavy side balanced
            #    self     save         save
            #  save   -> 1   self  -> 1  self.rot()
            #  1  2         2
            return self.srotate()
        else:
            return self.drotate()

    def srotate(self):
        """Single rotation. Assumes that balance is +-2."""
        #     self        save         save
        #   save 3  ->   1   self  -> 1   self.rot()
        #  1   2            2   3
        #
        #  self            save                save
        # 3   save  ->  self  1    -> self.rot()   1
        #    2   1     3   2

        #assert(self.balance != 0)
        heavy = self.balance > 0
        light = not heavy
        save = self[heavy]
        #print("srotate: bal={},{}".format(self.balance, save.balance))
        #self.print_structure()
        self[heavy] = save[light]   # 2
        #assert(save[light])
        save[light] = self.rotate()  # Needed to ensure the 2 and 3 are balanced under new subnode

        # Some intervals may overlap both self.x_center and save.x_center
        # Promote those to the new tip of the tree
        promotees = [iv for iv in save[light].s_center if save.center_hit(iv)]
        if promotees:
            for iv in promotees:
                save[light] = save[light].remove(iv)  # may trigger pruning
            # TODO: Use Node.add() here, to simplify future balancing improvements.
            # For now, this is the same as augmenting save.s_center, but that may
            # change.
            save.s_center.update(promotees)
        save.refresh_balance()
        return save

    def drotate(self):
        # First rotation
        my_heavy = self.balance > 0
        self[my_heavy] = self[my_heavy].srotate()
        self.refresh_balance()

        # Second rotation
        result = self.srotate()

        return result

    def add(self, interval):
        """
        Returns self after adding the interval and balancing.
        """
        if self.center_hit(interval):
            self.s_center.add(interval)
            return self
        else:
            direction = self.hit_branch(interval)
            if not self[direction]:
                self[direction] = Node.from_interval(interval)
                self.refresh_balance()
                return self
            else:
                self[direction] = self[direction].add(interval)
                return self.rotate()

    def remove(self, interval):
        """
        Returns self after removing the interval and balancing.

        If interval is not present, raise ValueError.
        """
        # since this is a list, called methods can set this to [1],
        # making it true
        done = []
        return self.remove_interval_helper(interval, done, should_raise_error=True)

    def discard(self, interval):
        """
        Returns self after removing interval and balancing.

        If interval is not present, do nothing.
        """
        done = []
        return self.remove_interval_helper(interval, done, should_raise_error=False)

    def remove_interval_helper(self, interval, done, should_raise_error):
        """
        Returns self after removing interval and balancing.
        If interval doesn't exist, raise ValueError.

        This method may set done to [1] to tell all callers that
        rebalancing has completed.

        See Eternally Confuzzled's jsw_remove_r function (lines 1-32)
        in his AVL tree article for reference.
        """
        #trace = interval.begin == 347 and interval.end == 353
        #if trace: print('\nRemoving from {} interval {}'.format(
        #   self.x_center, interval))
        if self.center_hit(interval):
            #if trace: print('Hit at {}'.format(self.x_center))
            if not should_raise_error and interval not in self.s_center:
                done.append(1)
                #if trace: print('Doing nothing.')
                return self
            try:
                # raises error if interval not present - this is
                # desired.
                self.s_center.remove(interval)
            except:
                self.print_structure()
                raise KeyError(interval)
            if self.s_center:     # keep this node
                done.append(1)    # no rebalancing necessary
                #if trace: print('Removed, no rebalancing.')
                return self

            # If we reach here, no intervals are left in self.s_center.
            # So, prune self.
            return self.prune()
        else:  # interval not in s_center
            direction = self.hit_branch(interval)

            if not self[direction]:
                if should_raise_error:
                    raise ValueError
                done.append(1)
                return self

            #if trace:
            #   print('Descending to {} branch'.format(
            #       ['left', 'right'][direction]
            #       ))
            self[direction] = self[direction].remove_interval_helper(interval, done, should_raise_error)

            # Clean up
            if not done:
                #if trace:
                #    print('Rotating {}'.format(self.x_center))
                #    self.print_structure()
                return self.rotate()
            return self

    def search_overlap(self, point_list):
        """
        Returns all intervals that overlap the point_list.
        """
        result = set()
        for j in point_list:
            self.search_point(j, result)
        return result
    
    def count_point(self, point, result):
        for k in self.s_center:
            if k.begin <= point <= k.end:
                result += 1
        if point < self.x_center and self[0]:
            return self[0].count_point(point, result)
        elif point > self.x_center and self[1]:
            return self[1].count_point(point, result)
        return result
    
    def count_point2(self, point, res):
        for i in self.s_center:
            if i.begin <= point <= i.end:
                res += 1
        
        
        if point < self.x_center and self.left_node:
            return self.left_node.count_point2(point, res)
        elif point > self.x_center and self.right_node:
            return self.right_node.count_point2(point, res)
            
        return res
    

    def search_point(self, point, result):
        """
        Returns all intervals that contain point.
        """
        for k in self.s_center:
            if k.begin <= point <= k.end:
                result.add(k)
        if point < self.x_center and self[0]:
            return self[0].search_point(point, result)
        elif point > self.x_center and self[1]:
            return self[1].search_point(point, result)
        return result

    def prune(self):
        """
        On a subtree where the root node's s_center is empty,
        return a new subtree with no empty s_centers.
        """
        if not self[0] or not self[1]:    # if I have an empty branch
            direction = not self[0]       # graft the other branch here
            #if trace:
            #    print('Grafting {} branch'.format(
            #       'right' if direction else 'left'))

            result = self[direction]
            #if result: result.verify()
            return result
        else:
            # Replace the root node with the greatest predecessor.
            heir, self[0] = self[0].pop_greatest_child()
            #if trace:
            #    print('Replacing {} with {}.'.format(
            #        self.x_center, heir.x_center
            #        ))
            #    print('Removed greatest predecessor:')
            #    self.print_structure()

            #if self[0]: self[0].verify()
            #if self[1]: self[1].verify()

            # Set up the heir as the new root node
            (heir[0], heir[1]) = (self[0], self[1])
            #if trace: print('Setting up the heir:')
            #if trace: heir.print_structure()

            # popping the predecessor may have unbalanced this node;
            # fix it
            heir.refresh_balance()
            heir = heir.rotate()
            #heir.verify()
            #if trace: print('Rotated the heir:')
            #if trace: heir.print_structure()
            return heir

    def pop_greatest_child(self):
        """
        Used when pruning a node with both a left and a right branch.
        Returns (greatest_child, node), where:
          * greatest_child is a new node to replace the removed node.
          * node is the subtree after:
              - removing the greatest child
              - balancing
              - moving overlapping nodes into greatest_child

        Assumes that self.s_center is not empty.

        See Eternally Confuzzled's jsw_remove_r function (lines 34-54)
        in his AVL tree article for reference.
        """
        #print('Popping from {}'.format(self.x_center))
        if not self.right_node:         # This node is the greatest child.
            # To reduce the chances of an overlap with a parent, return
            # a child node containing the smallest possible number of
            # intervals, as close as possible to the maximum bound.
            ivs = sorted(self.s_center, key=attrgetter('end', 'begin'))
            max_iv = ivs.pop()
            new_x_center = self.x_center
            while ivs:
                next_max_iv = ivs.pop()
                if next_max_iv.end == max_iv.end: continue
                new_x_center = max(new_x_center, next_max_iv.end)
            def get_new_s_center():
                for iv in self.s_center:
                    if iv.contains_point(new_x_center): yield iv

            # Create a new node with the largest x_center possible.
            child = Node(new_x_center, get_new_s_center())
            self.s_center -= child.s_center

            #print('Pop hit! Returning child   = {}'.format(
            #    child.print_structure(tostring=True)
            #    ))
            #assert not child[0]
            #assert not child[1]

            if self.s_center:
                #print('     and returning newnode = {}'.format( self ))
                #self.verify()
                return child, self
            else:
                #print('     and returning newnode = {}'.format( self[0] ))
                #if self[0]: self[0].verify()
                return child, self[0]  # Rotate left child up

        else:
            #print('Pop descent to {}'.format(self[1].x_center))
            (greatest_child, self[1]) = self[1].pop_greatest_child()

            # Move any overlaps into greatest_child
            for iv in set(self.s_center):
                if iv.contains_point(greatest_child.x_center):
                    self.s_center.remove(iv)
                    greatest_child.add(iv)

            #print('Pop Returning child   = {}'.format(
            #    greatest_child.print_structure(tostring=True)
            #    ))
            if self.s_center:
                #print('and returning newnode = {}'.format(
                #    new_self.print_structure(tostring=True)
                #    ))
                #new_self.verify()
                self.refresh_balance()
                new_self = self.rotate()
                return greatest_child, new_self
            else:
                new_self = self.prune()
                #print('and returning prune = {}'.format(
                #    new_self.print_structure(tostring=True)
                #    ))
                #if new_self: new_self.verify()
                return greatest_child, new_self

    # TODO: adapt this to count the number of intervals that overlap with the point
    # this should use a global counter
    def contains_point(self, p):
        """
        Returns whether this node or a child overlaps p.
        """
        for iv in self.s_center:
            if iv.contains_point(p):
                return True
        branch = self[p > self.x_center]
        return branch and branch.contains_point(p)

    def all_children(self):
        return self.all_children_helper(set())

    def all_children_helper(self, result):
        result.update(self.s_center)
        if self[0]:
            self[0].all_children_helper(result)
        if self[1]:
            self[1].all_children_helper(result)
        return result

    def verify(self, parents=set()):
        """
        ## DEBUG ONLY ##
        Recursively ensures that the invariants of an interval subtree
        hold.
        """
        assert(isinstance(self.s_center, set))

        bal = self.balance
        assert abs(bal) < 2, \
            "Error: Rotation should have happened, but didn't! \n{}".format(
                self.print_structure(tostring=True)
            )
        self.refresh_balance()
        assert bal == self.balance, \
            "Error: self.balance not set correctly! \n{}".format(
                self.print_structure(tostring=True)
            )

        assert self.s_center, \
            "Error: s_center is empty! \n{}".format(
                self.print_structure(tostring=True)
            )
        for iv in self.s_center:
            assert hasattr(iv, 'begin')
            assert hasattr(iv, 'end')
            assert iv.begin < iv.end
            assert iv.overlaps(self.x_center)
            for parent in sorted(parents):
                assert not iv.contains_point(parent), \
                    "Error: Overlaps ancestor ({})! \n{}\n\n{}".format(
                        parent, iv, self.print_structure(tostring=True)
                    )
        if self[0]:
            assert self[0].x_center < self.x_center, \
                "Error: Out-of-order left child! {}".format(self.x_center)
            self[0].verify(parents.union([self.x_center]))
        if self[1]:
            assert self[1].x_center > self.x_center, \
                "Error: Out-of-order right child! {}".format(self.x_center)
            self[1].verify(parents.union([self.x_center]))

    def __getitem__(self, index):
        """
        Returns the left child if input is equivalent to False, or
        the right side otherwise.
        """
        if index:
            return self.right_node
        else:
            return self.left_node

    def __setitem__(self, key, value):
        """Sets the left (0) or right (1) child."""
        if key:
            self.right_node = value
        else:
            self.left_node = value

    def __str__(self):
        """
        Shows info about this node.

        Since Nodes are internal data structures not revealed to the
        user, I'm not bothering to make this copy-paste-executable as a
        constructor.
        """
        return "Node<{0}, depth={1}, balance={2}>".format(
            self.x_center,
            self.depth,
            self.balance
        )
        #fieldcount = 'c_count,has_l,has_r = <{}, {}, {}>'.format(
        #    len(self.s_center),
        #    bool(self.left_node),
        #    bool(self.right_node)
        #)
        #fields = [self.x_center, self.balance, fieldcount]
        #return "Node({}, b={}, {})".format(*fields)

    # NOTE: use this to count the number of intervals that overlap with the point
    def count_nodes(self):
        """
        Count the number of Nodes in this subtree.
        :rtype: int
        """
        count = 1
        if self.left_node:
            count += self.left_node.count_nodes()
        if self.right_node:
            count += self.right_node.count_nodes()
        return count

    def depth_score(self, n, m):
        """
        Calculates flaws in balancing the tree.
        :param n: size of tree
        :param m: number of Nodes in tree
        :rtype: real
        """
        if n == 0:
            return 0.0

        # dopt is the optimal maximum depth of the tree
        dopt = 1 + int(floor(l2(m)))
        f = 1 / float(1 + n - dopt)
        return f * self.depth_score_helper(1, dopt)

    def depth_score_helper(self, d, dopt):
        """
        Gets a weighted count of the number of Intervals deeper than dopt.
        :param d: current depth, starting from 0
        :param dopt: optimal maximum depth of a leaf Node
        :rtype: real
        """
        # di is how may levels deeper than optimal d is
        di = d - dopt
        if di > 0:
            count = di * len(self.s_center)
        else:
            count = 0
        if self.right_node:
            count += self.right_node.depth_score_helper(d + 1, dopt)
        if self.left_node:
            count += self.left_node.depth_score_helper(d + 1, dopt)
        return count

    def print_structure(self, indent=0, tostring=False):
        """
        For debugging.
        """
        nl = '\n'
        sp = indent * '    '

        rlist = [str(self) + nl]
        if self.s_center:
            for iv in sorted(self.s_center):
                rlist.append(sp + ' ' + repr(iv) + nl)
        if self.left_node:
            rlist.append(sp + '<:  ')  # no CR
            rlist.append(self.left_node.print_structure(indent + 1, True))
        if self.right_node:
            rlist.append(sp + '>:  ')  # no CR
            rlist.append(self.right_node.print_structure(indent + 1, True))
        result = ''.join(rlist)
        if tostring:
            return result
        else:
            print(result)
PK     g��Yb�lZa  a     planesweep.pyimport math

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
PK     �j�Y               priorityqueue/PK     �|�Y               priorityqueue/__pycache__/PK     �|�Y[݁��  �  9   priorityqueue/__pycache__/PrioritizedItem.cpython-312.pyc�
    �F\g�   �                   �L   � d dl mZmZ d dlmZ  ed��       G d� d�      �       Zy)�    )�	dataclass�field)�AnyT)�orderc                   �@   � e Zd ZU eeeef   ed<    ed��      Ze	ed<   y)�PrioritizedItem�priorityF)�compare�itemN)
�__name__�
__module__�__qualname__�tuple�float�int�__annotations__r   r   r   � �    ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\priorityqueue\PrioritizedItem.pyr   r      s#   � ��E�5�#�%�&�&��E�"�D�#�"r   r   N)�dataclassesr   r   �typingr   r   r   r   r   �<module>r      s'   �� (� �
���#� #� �#r   PK     �|�Yϸn�   �       priorityqueue/PrioritizedItem.pyfrom dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: tuple[float, float, int]
    item: Any=field(compare=False)
    
    
PK     ˀ�Y               sortedcontainers/PK     ˀ�Y�꒤�  �     sortedcontainers/__init__.py"""Sorted Containers -- Sorted List, Sorted Dict, Sorted Set

Sorted Containers is an Apache2 licensed containers library, written in
pure-Python, and fast as C-extensions.

Python's standard library is great until you need a sorted collections
type. Many will attest that you can get really far without one, but the moment
you **really need** a sorted list, dict, or set, you're faced with a dozen
different implementations, most using C-extensions without great documentation
and benchmarking.

In Python, we can do better. And we can do it in pure-Python!

::

    >>> from sortedcontainers import SortedList
    >>> sl = SortedList(['e', 'a', 'c', 'd', 'b'])
    >>> sl
    SortedList(['a', 'b', 'c', 'd', 'e'])
    >>> sl *= 1000000
    >>> sl.count('c')
    1000000
    >>> sl[-3:]
    ['e', 'e', 'e']
    >>> from sortedcontainers import SortedDict
    >>> sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
    >>> sd
    SortedDict({'a': 1, 'b': 2, 'c': 3})
    >>> sd.popitem(index=-1)
    ('c', 3)
    >>> from sortedcontainers import SortedSet
    >>> ss = SortedSet('abracadabra')
    >>> ss
    SortedSet(['a', 'b', 'c', 'd', 'r'])
    >>> ss.bisect_left('c')
    2

Sorted Containers takes all of the work out of Python sorted types - making
your deployment and use of Python easy. There's no need to install a C compiler
or pre-build and distribute custom extensions. Performance is a feature and
testing has 100% coverage with unit tests and hours of stress.

:copyright: (c) 2014-2019 by Grant Jenks.
:license: Apache 2.0, see LICENSE for more details.

"""


from .sortedlist import SortedList, SortedKeyList, SortedListWithKey
from .sortedset import SortedSet
from .sorteddict import (
    SortedDict,
    SortedKeysView,
    SortedItemsView,
    SortedValuesView,
)

__all__ = [
    'SortedList',
    'SortedKeyList',
    'SortedListWithKey',
    'SortedDict',
    'SortedKeysView',
    'SortedItemsView',
    'SortedValuesView',
    'SortedSet',
]

__title__ = 'sortedcontainers'
__version__ = '2.4.0'
__build__ = 0x020400
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = '2014-2019, Grant Jenks'
PK     ���Y               sortedcontainers/__pycache__/PK     ���Y�Z�X	  X	  5   sortedcontainers/__pycache__/__init__.cpython-312.pyc�
    �A`g�  �                   �`   � d Z ddlmZmZmZ ddlmZ ddlmZm	Z	m
Z
mZ g d�ZdZdZdZd	Zd
ZdZy)a  Sorted Containers -- Sorted List, Sorted Dict, Sorted Set

Sorted Containers is an Apache2 licensed containers library, written in
pure-Python, and fast as C-extensions.

Python's standard library is great until you need a sorted collections
type. Many will attest that you can get really far without one, but the moment
you **really need** a sorted list, dict, or set, you're faced with a dozen
different implementations, most using C-extensions without great documentation
and benchmarking.

In Python, we can do better. And we can do it in pure-Python!

::

    >>> from sortedcontainers import SortedList
    >>> sl = SortedList(['e', 'a', 'c', 'd', 'b'])
    >>> sl
    SortedList(['a', 'b', 'c', 'd', 'e'])
    >>> sl *= 1000000
    >>> sl.count('c')
    1000000
    >>> sl[-3:]
    ['e', 'e', 'e']
    >>> from sortedcontainers import SortedDict
    >>> sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
    >>> sd
    SortedDict({'a': 1, 'b': 2, 'c': 3})
    >>> sd.popitem(index=-1)
    ('c', 3)
    >>> from sortedcontainers import SortedSet
    >>> ss = SortedSet('abracadabra')
    >>> ss
    SortedSet(['a', 'b', 'c', 'd', 'r'])
    >>> ss.bisect_left('c')
    2

Sorted Containers takes all of the work out of Python sorted types - making
your deployment and use of Python easy. There's no need to install a C compiler
or pre-build and distribute custom extensions. Performance is a feature and
testing has 100% coverage with unit tests and hours of stress.

:copyright: (c) 2014-2019 by Grant Jenks.
:license: Apache 2.0, see LICENSE for more details.

�   )�
SortedList�SortedKeyList�SortedListWithKey)�	SortedSet)�
SortedDict�SortedKeysView�SortedItemsView�SortedValuesView)r   r   r   r   r   r	   r
   r   �sortedcontainersz2.4.0i  zGrant Jenksz
Apache 2.0z2014-2019, Grant JenksN)�__doc__�
sortedlistr   r   r   �	sortedsetr   �
sorteddictr   r   r	   r
   �__all__�	__title__�__version__�	__build__�
__author__�__license__�__copyright__� �    ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\sortedcontainers\__init__.py�<module>r      sH   ��-�` E� D�  �� �	�� �	����	��
���(�r   PK     ���Y�3xҶl  �l  7   sortedcontainers/__pycache__/sorteddict.cpython-312.pyc�
    �A`g�[  �                   ��   � d Z ddlZddlZddlmZ ddlmZmZ ddlm	Z	 	 ddl
mZmZmZmZmZ  G d� d	e�      Zd
� Z G d� dee�      Z G d� dee�      Z G d� dee�      Zy# e$ r ddlmZmZmZmZmZ Y �Hw xY w)a�  Sorted Dict
==============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted dict implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedDict`
* :class:`SortedKeysView`
* :class:`SortedItemsView`
* :class:`SortedValuesView`

�    N)�chain�   )�
SortedList�recursive_repr��	SortedSet)�	ItemsView�KeysView�Mapping�
ValuesView�Sequencec                   �  � e Zd ZdZd� Zed� �       Zed� �       Zd� Zd� Z	d� Z
d� Zd	� ZeZd
� Zd� Zd� Zd� ZeZed(d��       Zd� Zd� Zd� Zej2                  dk  r9d� Z edd�      Z edd�      Z edd�      Z edd�      Z edd�      Z edd�      Z  G d� de!�      Z" e"�       Z#e#fd �Z$d)d!�Z%d)d"�Z&d(d#�Z'd$� Z(e(Z)d%� Z* e+�       d&� �       Z,d'� Z-y)*�
SortedDicta�  Sorted dict is a sorted mutable mapping.

    Sorted dict keys are maintained in sorted order. The design of sorted dict
    is simple: sorted dict inherits from dict to store items and maintains a
    sorted list of keys.

    Sorted dict keys must be hashable and comparable. The hash and total
    ordering of keys must not change while they are stored in the sorted dict.

    Mutable mapping methods:

    * :func:`SortedDict.__getitem__` (inherited from dict)
    * :func:`SortedDict.__setitem__`
    * :func:`SortedDict.__delitem__`
    * :func:`SortedDict.__iter__`
    * :func:`SortedDict.__len__` (inherited from dict)

    Methods for adding items:

    * :func:`SortedDict.setdefault`
    * :func:`SortedDict.update`

    Methods for removing items:

    * :func:`SortedDict.clear`
    * :func:`SortedDict.pop`
    * :func:`SortedDict.popitem`

    Methods for looking up items:

    * :func:`SortedDict.__contains__` (inherited from dict)
    * :func:`SortedDict.get` (inherited from dict)
    * :func:`SortedDict.peekitem`

    Methods for views:

    * :func:`SortedDict.keys`
    * :func:`SortedDict.items`
    * :func:`SortedDict.values`

    Methods for miscellany:

    * :func:`SortedDict.copy`
    * :func:`SortedDict.fromkeys`
    * :func:`SortedDict.__reversed__`
    * :func:`SortedDict.__eq__` (inherited from dict)
    * :func:`SortedDict.__ne__` (inherited from dict)
    * :func:`SortedDict.__repr__`
    * :func:`SortedDict._check`

    Sorted list methods available (applies to keys):

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.count`
    * :func:`SortedList.index`
    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList._reset`

    Additional sorted list methods available, if key-function used:

    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Sorted dicts may only be compared for equality and inequality.

    c                 �*  � |r%|d   �t        |d   �      r|d   x}| _        |dd }n	dx}| _        t        |��      | _        | j                  }|j                  | _        |j                  | _        |j                  | _	        |j                  | _        |j                  | _        |j                  | _        |j                   | _        |j$                  | _        |j&                  | _        |j&                  | _        |j*                  | _        |j,                  | _        |j.                  | _        |j0                  | _        |�D|j2                  | _        |j4                  | _        |j6                  | _        |j8                  | _         | j:                  |i |�� y)aQ  Initialize sorted dict instance.

        Optional key-function argument defines a callable that, like the `key`
        argument to the built-in `sorted` function, extracts a comparison key
        from each dictionary key. If no function is specified, the default
        compares the dictionary keys directly. The key-function argument must
        be provided as a positional argument and must come before all other
        arguments.

        Optional iterable argument provides an initial sequence of pairs to
        initialize the sorted dict. Each pair in the sequence defines the key
        and corresponding value. If a key is seen more than once, the last
        value associated with it is stored in the new sorted dict.

        Optional mapping argument provides an initial mapping of items to
        initialize the sorted dict.

        If keyword arguments are given, the keywords themselves, with their
        associated values, are added as items to the dictionary. If a key is
        specified both in the positional argument and as a keyword argument,
        the value associated with the keyword is stored in the
        sorted dict.

        Sorted dict keys must be hashable, per the requirement for Python's
        dictionaries. Keys (or the result of the key-function) must also be
        comparable, per the requirement for sorted lists.

        >>> d = {'alpha': 1, 'beta': 2}
        >>> SortedDict([('alpha', 1), ('beta', 2)]) == d
        True
        >>> SortedDict({'alpha': 1, 'beta': 2}) == d
        True
        >>> SortedDict(alpha=1, beta=2) == d
        True

        r   Nr   )�key)�callable�_keyr   �_list�add�	_list_add�clear�_list_clear�__iter__�
_list_iter�__reversed__�_list_reversed�pop�	_list_pop�remove�_list_remove�update�_list_update�bisect_left�bisect_right�bisect�index�irange�islice�_reset�bisect_key_left�bisect_key_right�
bisect_key�
irange_key�_update)�self�args�kwargsr   r   s        ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\sortedcontainers\sorteddict.py�__init__zSortedDict.__init__q   sR  � �J �T�!�W�_���a��(9�#�A�w�&�D�4�9����8�D�#�#�D�4�9��D�)��
�
 �
�
������� �;�;����.�.���#�0�0��������!�L�L���!�L�L��� !�,�,����(�(���!�.�.����[�[��
��l�l����l�l����l�l�����#(�#8�#8�D� �$)�$:�$:�D�!�#�.�.�D�O�#�.�.�D�O�����d�%�f�%�    c                 �   � | j                   S )z�Function used to extract comparison key from keys.

        Sorted dict compares keys directly when the key function is none.

        )r   �r/   s    r2   r   zSortedDict.key�   s   � � �y�y�r4   c                 �   � 	 | j                   S # t        $ r3 t        j                  dt        d��       t        | �      x}| _         |cY S w xY w)z�Cached reference of sorted keys view.

        Deprecated in version 2 of Sorted Containers. Use
        :func:`SortedDict.keys` instead.

        z>sorted_dict.iloc is deprecated. Use SortedDict.keys() instead.�   )�
stacklevel)�_iloc�AttributeError�warnings�warn�DeprecationWarning�SortedKeysView)r/   r:   s     r2   �iloczSortedDict.iloc�   sO   � �
	��:�:���� 	��M�M�2�"��	� "0��!5�5�E�D�J��L�	�s   � �9A
�	A
c                 �N   � t         j                  | �       | j                  �        y)zPRemove all items from sorted dict.

        Runtime complexity: `O(n)`

        N)�dictr   r   r6   s    r2   r   zSortedDict.clear�   s   � � 	�
�
�4�����r4   c                 �R   � t         j                  | |�       | j                  |�       y)a�  Remove item from sorted dict identified by `key`.

        ``sd.__delitem__(key)`` <==> ``del sd[key]``

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> del sd['b']
        >>> sd
        SortedDict({'a': 1, 'c': 3})
        >>> del sd['z']
        Traceback (most recent call last):
          ...
        KeyError: 'z'

        :param key: `key` for item lookup
        :raises KeyError: if key not found

        N)rB   �__delitem__r    )r/   r   s     r2   rD   zSortedDict.__delitem__�   s"   � �( 	����s�#����#�r4   c                 �"   � | j                  �       S )z�Return an iterator over the keys of the sorted dict.

        ``sd.__iter__()`` <==> ``iter(sd)``

        Iterating the sorted dict while adding or deleting items may raise a
        :exc:`RuntimeError` or fail to iterate over all keys.

        )r   r6   s    r2   r   zSortedDict.__iter__   s   � � ��� � r4   c                 �"   � | j                  �       S )a  Return a reverse iterator over the keys of the sorted dict.

        ``sd.__reversed__()`` <==> ``reversed(sd)``

        Iterating the sorted dict while adding or deleting items may raise a
        :exc:`RuntimeError` or fail to iterate over all keys.

        )r   r6   s    r2   r   zSortedDict.__reversed__  s   � � �"�"�$�$r4   c                 �\   � || vr| j                  |�       t        j                  | ||�       y)a�  Store item in sorted dict with `key` and corresponding `value`.

        ``sd.__setitem__(key, value)`` <==> ``sd[key] = value``

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict()
        >>> sd['c'] = 3
        >>> sd['a'] = 1
        >>> sd['b'] = 2
        >>> sd
        SortedDict({'a': 1, 'b': 2, 'c': 3})

        :param key: key for item
        :param value: value for item

        N)r   rB   �__setitem__)r/   r   �values      r2   rH   zSortedDict.__setitem__  s)   � �$ �d�?��N�N�3������s�E�*r4   c                 �   � t        |t        �      st        S t        | j	                  �       |j	                  �       �      }| j                  | j                  |�      S �N��
isinstancer   �NotImplementedr   �items�	__class__r   �r/   �otherrO   s      r2   �__or__zSortedDict.__or__1  s?   � ��%��)�!�!��d�j�j�l�E�K�K�M�2���~�~�d�i�i��/�/r4   c                 �   � t        |t        �      st        S t        |j	                  �       | j	                  �       �      }| j                  | j                  |�      S rK   rL   rQ   s      r2   �__ror__zSortedDict.__ror__8  s?   � ��%��)�!�!��e�k�k�m�T�Z�Z�\�2���~�~�d�i�i��/�/r4   c                 �(   � | j                  |�       | S rK   )r.   )r/   rR   s     r2   �__ior__zSortedDict.__ior__?  s   � ����U���r4   c                 �V   � | j                  | j                  | j                  �       �      S )zyReturn a shallow copy of the sorted dict.

        Runtime complexity: `O(n)`

        :return: new sorted dict

        )rP   r   rO   r6   s    r2   �copyzSortedDict.copyD  s   � � �~�~�d�i�i�����6�6r4   Nc                 �&   ��  | �fd�|D �       �      S )z�Return a new sorted dict initailized from `iterable` and `value`.

        Items in the sorted dict have keys from `iterable` and values equal to
        `value`.

        Runtime complexity: `O(n*log(n))`

        :return: new sorted dict

        c              3   �&   �K  � | ]  }|�f�� �
 y �wrK   � )�.0r   rI   s     �r2   �	<genexpr>z&SortedDict.fromkeys.<locals>.<genexpr>]  s   �� �� �4�8�C�C��<�8��   �r\   )�cls�iterablerI   s     `r2   �fromkeyszSortedDict.fromkeysQ  s   �� � �4�8�4�4�4r4   c                 �   � t        | �      S )z�Return new sorted keys view of the sorted dict's keys.

        See :class:`SortedKeysView` for details.

        :return: new sorted keys view

        )r?   r6   s    r2   �keyszSortedDict.keys`  s   � � �d�#�#r4   c                 �   � t        | �      S )z�Return new sorted items view of the sorted dict's items.

        See :class:`SortedItemsView` for details.

        :return: new sorted items view

        )�SortedItemsViewr6   s    r2   rO   zSortedDict.itemsk  s   � � �t�$�$r4   c                 �   � t        | �      S )z�Return new sorted values view of the sorted dict's values.

        See :class:`SortedValuesView` for details.

        :return: new sorted values view

        )�SortedValuesViewr6   s    r2   �valueszSortedDict.valuesv  s   � �  ��%�%r4   i   c                 �f   �� dj                  | |��      ��fd�}| |_        �|_        t        |�      S )NzQSortedDict.{original}() is not implemented. Use SortedDict.{alternate}() instead.)�original�	alternatec                 �   �� t        ��      �rK   )r;   )r/   �messages    �r2   �methodz6SortedDict.__make_raise_attributeerror.<locals>.method�  s   �� �$�W�-�-r4   )�format�__name__�__doc__�property)rk   rl   ro   rn   s      @r2   �__make_raise_attributeerrorz&SortedDict.__make_raise_attributeerror�  s;   �� �9��f�h�)�f�<� �.� '�F�O�$�F�N��F�#�#r4   �	iteritemsrO   �iterkeysrd   �
itervaluesri   �	viewitems�viewkeys�
viewvaluesc                   �   � e Zd Zd� Zy)�SortedDict._NotGivenc                  �   � y)Nz<not-given>r\   r6   s    r2   �__repr__zSortedDict._NotGiven.__repr__�  s   � � r4   N)rq   �
__module__�__qualname__r~   r\   r4   r2   �	_NotGivenr|   �  s   � �	!r4   r�   c                 �   � || v r'| j                  |�       t        j                  | |�      S || j                  u rt	        |�      �|S )a�  Remove and return value for item identified by `key`.

        If the `key` is not found then return `default` if given. If `default`
        is not given then raise :exc:`KeyError`.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> sd.pop('c')
        3
        >>> sd.pop('z', 26)
        26
        >>> sd.pop('y')
        Traceback (most recent call last):
          ...
        KeyError: 'y'

        :param key: `key` for item
        :param default: `default` value if key not found (optional)
        :return: value for item
        :raises KeyError: if `key` not found and `default` not given

        )r    rB   r   �_SortedDict__not_given�KeyError�r/   r   �defaults      r2   r   zSortedDict.pop�  sG   � �0 �$�;����c�"��8�8�D�#�&�&��$�*�*�*��s�m�#��Nr4   c                 �r   � | st        d�      �| j                  |�      }t        j                  | |�      }||fS )a_  Remove and return ``(key, value)`` pair at `index` from sorted dict.

        Optional argument `index` defaults to -1, the last item in the sorted
        dict. Specify ``index=0`` for the first item in the sorted dict.

        If the sorted dict is empty, raises :exc:`KeyError`.

        If the `index` is out of range, raises :exc:`IndexError`.

        Runtime complexity: `O(log(n))`

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> sd.popitem()
        ('c', 3)
        >>> sd.popitem(0)
        ('a', 1)
        >>> sd.popitem(100)
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param int index: `index` of item (default -1)
        :return: key and value pair
        :raises KeyError: if sorted dict is empty
        :raises IndexError: if `index` out of range

        zpopitem(): dictionary is empty)r�   r   rB   r   )r/   r&   r   rI   s       r2   �popitemzSortedDict.popitem�  s;   � �8 ��;�<�<��n�n�U�#������s�#���U�|�r4   c                 �.   � | j                   |   }|| |   fS )a0  Return ``(key, value)`` pair at `index` in sorted dict.

        Optional argument `index` defaults to -1, the last item in the sorted
        dict. Specify ``index=0`` for the first item in the sorted dict.

        Unlike :func:`SortedDict.popitem`, the sorted dict is not modified.

        If the `index` is out of range, raises :exc:`IndexError`.

        Runtime complexity: `O(log(n))`

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> sd.peekitem()
        ('c', 3)
        >>> sd.peekitem(0)
        ('a', 1)
        >>> sd.peekitem(100)
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param int index: index of item (default -1)
        :return: key and value pair
        :raises IndexError: if `index` out of range

        )r   )r/   r&   r   s      r2   �peekitemzSortedDict.peekitem�  s    � �6 �j�j�����D��I�~�r4   c                 �h   � || v r| |   S t         j                  | ||�       | j                  |�       |S )a�  Return value for item identified by `key` in sorted dict.

        If `key` is in the sorted dict then return its value. If `key` is not
        in the sorted dict then insert `key` with value `default` and return
        `default`.

        Optional argument `default` defaults to none.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict()
        >>> sd.setdefault('a', 1)
        1
        >>> sd.setdefault('a', 10)
        1
        >>> sd
        SortedDict({'a': 1})

        :param key: key for item
        :param default: value for item (default None)
        :return: value for item identified by `key`

        )rB   rH   r   r�   s      r2   �
setdefaultzSortedDict.setdefault  s8   � �0 �$�;���9������s�G�,����s���r4   c                 ��  � | s>t        j                  | g|��i |�� | j                  t         j                  | �      �       y|s't	        |�      dk(  rt        |d   t         �      r|d   }nt        |i |��}dt	        |�      z  t	        | �      kD  rKt         j                  | |�       | j                  �        | j                  t         j                  | �      �       y|D ]  }| j                  |||   �       � y)as  Update sorted dict with items from `args` and `kwargs`.

        Overwrites existing items.

        Optional arguments `args` and `kwargs` may be a mapping, an iterable of
        pairs or keyword arguments. See :func:`SortedDict.__init__` for
        details.

        :param args: mapping or iterable of pairs
        :param kwargs: keyword arguments mapping

        Nr   r   �
   )rB   r!   r"   r   �lenrM   r   �_setitem)r/   r0   r1   �pairsr   s        r2   r!   zSortedDict.update!  s�   � � ��K�K��.�t�.�v�.����d�m�m�D�1�2���#�d�)�q�.�Z��Q���-F���G�E��$�)�&�)�E���U��O�s�4�y�(��K�K��e�$��������d�m�m�D�1�2������c�5��:�.� r4   c                 �^   � t         j                  | �      }t        | �      | j                  |ffS )z�Support for pickle.

        The tricks played with caching references in
        :func:`SortedDict.__init__` confuse pickle so customize the reducer.

        )rB   rY   �typer   )r/   rO   s     r2   �
__reduce__zSortedDict.__reduce__C  s)   � � �	�	�$����T�
�T�Y�Y��.�/�/r4   c                 ��   � �� � j                   }t        � �      j                  }|�dndj                  |�      }dj                  �dj	                  �� fd�� j
                  D �       �      }dj                  |||�      S )z�Return string representation of sorted dict.

        ``sd.__repr__()`` <==> ``repr(sd)``

        :return: string representation

        � z{0!r}, z{0!r}: {1!r}z, c              3   �6   �K  � | ]  } �|�|   �      �� � y �wrK   r\   )r]   r   �item_formatr/   s     ��r2   r^   z&SortedDict.__repr__.<locals>.<genexpr>[  s   �� �� �L��#�+�c�4��9�5��s   �z{0}({1}{{{2}}}))r   r�   rq   rp   �joinr   )r/   r   �	type_name�key_argrO   r�   s   `    @r2   r~   zSortedDict.__repr__N  sk   �� � �y�y����J�'�'�	���"�)�*:�*:�4�*@��$�+�+���	�	�L����L�L�� �'�'�	�7�E�B�Br4   c                 �   � � � j                   }|j                  �        t        � �      t        |�      k(  sJ �t        � fd�|D �       �      sJ �y)zNCheck invariants of sorted dict.

        Runtime complexity: `O(n)`

        c              3   �&   �K  � | ]  }|�v �� �
 y �wrK   r\   )r]   r   r/   s     �r2   r^   z$SortedDict._check.<locals>.<genexpr>h  s   �� �� �0�%�3�3�$�;�%�r_   N)r   �_checkr�   �all)r/   r   s   ` r2   r�   zSortedDict._check_  sA   �� � �
�
�������4�y�C��J�&�&�&��0�%�0�0�0�0r4   rK   )�����).rq   r   r�   rr   r3   rs   r   r@   r   rD   r   r   rH   r�   rS   rU   rW   rY   �__copy__�classmethodrb   rd   rO   ri   �sys�
hexversion�&_SortedDict__make_raise_attributeerrorru   rv   rw   rx   ry   rz   �objectr�   r�   r   r�   r�   r�   r!   r.   r�   r   r~   r�   r\   r4   r2   r   r   +   sP  � �D�JI&�X �� �� �� ��*��0	!�	%�+�, �H�0�0��
7� �H� �5� �5�$�%�&� �~�~�
�"�	$� 0��W�E�	�.�z�6�B��0��x�H�
�/��W�E�	�.�z�6�B��0��x�H�
�!�F� !�
 �+�K�*� �B!�H�>�>/�> �G�0� ��C� �C� 	1r4   r   c                 ��   � | j                   }|j                  }t        j                  }t	        |t
        �      r||   }||= |D ]  } |||�       � y|j                  |�      } |||�       y)a
  Remove item at `index` from sorted dict.

    ``view.__delitem__(index)`` <==> ``del view[index]``

    Supports slicing.

    Runtime complexity: `O(log(n))` -- approximate.

    >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
    >>> view = sd.keys()
    >>> del view[0]
    >>> sd
    SortedDict({'b': 2, 'c': 3})
    >>> del view[-1]
    >>> sd
    SortedDict({'b': 2})
    >>> del view[:]
    >>> sd
    SortedDict({})

    :param index: integer or slice for indexing
    :raises IndexError: if index out of range

    N)�_mappingr   rB   rD   rM   �slicer   )r/   r&   r�   r   �dict_delitemrd   r   s          r2   �_view_delitemr�   k  si   � �2 �}�}�H��N�N�E��#�#�L��%����U�|���%�L��C���3�'� � �i�i�����X�s�#r4   c                   �.   � e Zd ZdZdZed� �       Zd� ZeZ	y)r?   z�Sorted keys view is a dynamic view of the sorted dict's keys.

    When the sorted dict's keys change, the view reflects those changes.

    The keys view implements the set and sequence abstract base classes.

    r\   c                 �   � t        |�      S rK   r   �r`   �its     r2   �_from_iterablezSortedKeysView._from_iterable�  �   � ���}�r4   c                 �4   � | j                   j                  |   S )a�  Lookup key at `index` in sorted keys views.

        ``skv.__getitem__(index)`` <==> ``skv[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> skv = sd.keys()
        >>> skv[0]
        'a'
        >>> skv[-1]
        'c'
        >>> skv[:]
        ['a', 'b', 'c']
        >>> skv[100]
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param index: integer or slice for indexing
        :return: key or list of keys
        :raises IndexError: if index out of range

        )r�   r   )r/   r&   s     r2   �__getitem__zSortedKeysView.__getitem__�  s   � �6 �}�}�"�"�5�)�)r4   N�
rq   r   r�   rr   �	__slots__r�   r�   r�   r�   rD   r\   r4   r2   r?   r?   �  s.   � �� �I� �� ��*�<  �Kr4   r?   c                   �.   � e Zd ZdZdZed� �       Zd� ZeZ	y)rf   z�Sorted items view is a dynamic view of the sorted dict's items.

    When the sorted dict's items change, the view reflects those changes.

    The items view implements the set and sequence abstract base classes.

    r\   c                 �   � t        |�      S rK   r   r�   s     r2   r�   zSortedItemsView._from_iterable�  r�   r4   c                 �   � | j                   }|j                  }t        |t        �      r||   }|D �cg c]	  }|||   f�� c}S ||   }|||   fS c c}w )a�  Lookup item at `index` in sorted items view.

        ``siv.__getitem__(index)`` <==> ``siv[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> siv = sd.items()
        >>> siv[0]
        ('a', 1)
        >>> siv[-1]
        ('c', 3)
        >>> siv[:]
        [('a', 1), ('b', 2), ('c', 3)]
        >>> siv[100]
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param index: integer or slice for indexing
        :return: item or list of items
        :raises IndexError: if index out of range

        �r�   r   rM   r�   �r/   r&   r�   �_mapping_listrd   r   s         r2   r�   zSortedItemsView.__getitem__�  sf   � �6 �=�=�� �����e�U�#� ��'�D�48�9�D�S�S�(�3�-�(�D�9�9��E�"���H�S�M�!�!�� :s   �ANr�   r\   r4   r2   rf   rf   �  s/   � �� �I� �� ��#"�L  �Kr4   rf   c                   �   � e Zd ZdZdZd� ZeZy)rh   z�Sorted values view is a dynamic view of the sorted dict's values.

    When the sorted dict's values change, the view reflects those changes.

    The values view implements the sequence abstract base class.

    r\   c                 �   � | j                   }|j                  }t        |t        �      r||   }|D �cg c]  }||   ��	 c}S ||   }||   S c c}w )a�  Lookup value at `index` in sorted values view.

        ``siv.__getitem__(index)`` <==> ``siv[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> svv = sd.values()
        >>> svv[0]
        1
        >>> svv[-1]
        3
        >>> svv[:]
        [1, 2, 3]
        >>> svv[100]
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        r�   r�   s         r2   r�   zSortedValuesView.__getitem__  s\   � �6 �=�=�� �����e�U�#� ��'�D�-1�2�T�c�H�S�M�T�2�2��E�"����}��� 3s   �AN)rq   r   r�   rr   r�   r�   r�   rD   r\   r4   r2   rh   rh   �  s   � �� �I�#�L  �Kr4   rh   )rr   r�   r<   �	itertoolsr   �
sortedlistr   r   �	sortedsetr   �collections.abcr	   r
   r   r   r   �ImportError�collectionsrB   r   r�   r?   rf   rh   r\   r4   r2   �<module>r�      s�   ���$ � � � 2�  �O�� �}1�� }1�@#$�L. �X�x� . �b6 �i�� 6 �r1 �z�8� 1 ��q � O�N�N�O�s   �A! �!A7�6A7PK     ���Ynj���R �R 7   sortedcontainers/__pycache__/sortedlist.cpython-312.pyc�
    �A`g�4 �                   �  � d Z ddlmZ ddlZddlZddlmZmZmZ ddl	m
Z
mZmZ ddlmZ ddlmZmZmZmZmZmZmZmZ ddlmZ 	 dd	lmZmZ dd
lm Z  ddlm!Z! e!dk  rddl	m"Z# ddl	m$Z% 	 ddl&m'Z' nddlm)Z) 	 ddl*m'Z' dd�Z, G d� de�      Z-d� Z. G d� de-�      Z/e/Z0y# e$ r dd	lmZmZ Y �aw xY w# e$ r	 ddl(m'Z' Y �@w xY w# e$ r	 ddl+m'Z' Y �Qw xY w)ab  Sorted List
==============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted list implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedList`
* :class:`SortedKeyList`

�    )�print_functionN)�bisect_left�bisect_right�insort)�chain�repeat�starmap)�log)�add�eq�ne�gt�ge�lt�le�iadd)�dedent)�Sequence�MutableSequence)�wraps)�
hexversioni   )�imap)�izip)�	get_ident)�reducec                 �   � � � fd�}|S )zHDecorator to make a repr function return fillvalue for a recursive call.c                 �J   �� �� t        �       �t        � �      ��� fd��       }|S )Nc                 ��   �� t        | �      t        �       f}|�v r�S �j                  |�       	  �| �      }�j                  |�       |S # �j                  |�       w xY w�N)�idr   r   �discard)�self�key�result�	fillvalue�repr_running�user_functions      �����C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\sortedcontainers\sortedlist.py�wrapperz<recursive_repr.<locals>.decorating_function.<locals>.wrapper@   sc   �� ��T�(�I�K�'�C��l�"� � ����S�!�*�&�t�,���$�$�S�)��M�� �$�$�S�)�s   �A
 �
A)�setr   )r'   r)   r&   r%   s   ` @�r(   �decorating_functionz+recursive_repr.<locals>.decorating_function=   s(   �� ��u��	�}�	�		� 
�		� ��    � )r%   r+   s   ` r(   �recursive_reprr.   7   s   �� ��" �r,   c                   ��  � e Zd ZdZdZd:d�Zd:d�Zed� �       Zd� Z	d� Z
e
Zd	� Zd
� Zd� ZeZd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� ZeZd� Zd� Zd� Zd� Zd;d�Zd� Z	 	 d<d�Z d� Z!d� Z"d� Z#e#Z$e#Z%d� Z&d � Z'e'Z(d!� Z)d"� Z*d#� Z+d=d$�Z,d:d%�Z-d&� Z.e.Z/d'� Z0d(� Z1e1Z2d)� Z3d*� Z4 e4e5d+d,�      Z6 e4e7d-d.�      Z8 e4e9d/d0�      Z: e4e;d1d2�      Z< e4e=d3d4�      Z> e4e?d5d6�      Z@ eAe4�      Z4d7� ZB eC�       d8� �       ZDd9� ZEy)>�
SortedLista�  Sorted list is a sorted mutable sequence.

    Sorted list values are maintained in sorted order.

    Sorted list values must be comparable. The total ordering of values must
    not change while they are stored in the sorted list.

    Methods for adding values:

    * :func:`SortedList.add`
    * :func:`SortedList.update`
    * :func:`SortedList.__add__`
    * :func:`SortedList.__iadd__`
    * :func:`SortedList.__mul__`
    * :func:`SortedList.__imul__`

    Methods for removing values:

    * :func:`SortedList.clear`
    * :func:`SortedList.discard`
    * :func:`SortedList.remove`
    * :func:`SortedList.pop`
    * :func:`SortedList.__delitem__`

    Methods for looking up values:

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.count`
    * :func:`SortedList.index`
    * :func:`SortedList.__contains__`
    * :func:`SortedList.__getitem__`

    Methods for iterating values:

    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList.__iter__`
    * :func:`SortedList.__reversed__`

    Methods for miscellany:

    * :func:`SortedList.copy`
    * :func:`SortedList.__len__`
    * :func:`SortedList.__repr__`
    * :func:`SortedList._check`
    * :func:`SortedList._reset`

    Sorted lists use lexicographical ordering semantics when compared to other
    sequences.

    Some methods of mutable sequences are not supported and will raise
    not-implemented error.

    i�  Nc                 �   � |�J �d| _         | j                  | _        g | _        g | _        g | _        d| _        |�| j                  |�       yy)a�  Initialize sorted list instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted list.

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList()
        >>> sl
        SortedList([])
        >>> sl = SortedList([3, 1, 2, 5, 4])
        >>> sl
        SortedList([1, 2, 3, 4, 5])

        :param iterable: initial values (optional)

        Nr   )�_len�DEFAULT_LOAD_FACTOR�_load�_lists�_maxes�_index�_offset�_update�r"   �iterabler#   s      r(   �__init__zSortedList.__init__�   sU   � �$ �{��{���	��-�-��
����������������L�L��"�  r,   c                 �   � |�t         j                  | �      S | t        u rt         j                  t        �      S t	        d�      �)aJ  Create new sorted list or sorted-key list instance.

        Optional `key`-function argument will return an instance of subtype
        :class:`SortedKeyList`.

        >>> sl = SortedList()
        >>> isinstance(sl, SortedList)
        True
        >>> sl = SortedList(key=lambda x: -x)
        >>> isinstance(sl, SortedList)
        True
        >>> isinstance(sl, SortedKeyList)
        True

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)
        :return: sorted list or sorted-key list instance

        z&inherit SortedKeyList for key argument)�object�__new__r0   �SortedKeyList�	TypeError��clsr;   r#   s      r(   r?   zSortedList.__new__�   s;   � �* �;��>�>�#�&�&��j� ��~�~�m�4�4�� H�I�Ir,   c                  �   � y)z�Function used to extract comparison key from values.

        Sorted list compares values directly so the key function is none.

        Nr-   �r"   s    r(   r#   zSortedList.key�   s   � � r,   c                 �   � t        t        | j                  g �      }| j                  �        || _        | j                  |�       y)a�  Reset sorted list load factor.

        The `load` specifies the load-factor of the list. The default load
        factor of 1000 works well for lists from tens to tens-of-millions of
        values. Good practice is to use a value that is the cube root of the
        list size. With billions of elements, the best load factor depends on
        your usage. It's best to leave the load factor at the default until you
        start benchmarking.

        See :doc:`implementation` and :doc:`performance-scale` for more
        information.

        Runtime complexity: `O(n)`

        :param int load: load-factor for sorted list sublists

        N)r   r   r5   �_clearr4   r9   )r"   �load�valuess      r(   �_resetzSortedList._reset�   s2   � �$ ��d�k�k�2�.��������
����V�r,   c                 �z   � d| _         | j                  dd�= | j                  dd�= | j                  dd�= d| _        y)zQRemove all values from sorted list.

        Runtime complexity: `O(n)`

        r   N)r2   r5   r6   r7   r8   rE   s    r(   �clearzSortedList.clear�   s3   � � ��	��K�K��N��K�K��N��K�K��N���r,   c                 �\  � | j                   }| j                  }|rZt        ||�      }|t        |�      k(  r|dz  }||   j	                  |�       |||<   nt        ||   |�       | j                  |�       n#|j	                  |g�       |j	                  |�       | xj                  dz  c_        y)a  Add `value` to sorted list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList()
        >>> sl.add(3)
        >>> sl.add(1)
        >>> sl.add(2)
        >>> sl
        SortedList([1, 2, 3])

        :param value: value to add to sorted list

        �   N)r5   r6   r   �len�appendr   �_expandr2   )r"   �valuer5   r6   �poss        r(   r   zSortedList.add�   s�   � � ����������v�u�-�C��c�&�k�!��q����s��"�"�5�)�#��s���v�c�{�E�*��L�L����M�M�5�'�"��M�M�%� ��	�	�Q��	r,   c                 �  � | j                   }| j                  }| j                  }t        ||   �      |dz  kD  rV| j                  }||   }||d }||d�= |d   ||<   |j                  |dz   |�       |j                  |dz   |d   �       |dd�= y|r7| j                  |z   }|r||xx   dz  cc<   |dz
  dz	  }|r�|dxx   dz  cc<   yy�a>  Split sublists with length greater than double the load-factor.

        Updates the index when the sublist length is less than double the load
        level. This requires incrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        rN   N�����r   )r4   r5   r7   rO   r6   �insertr8   )	r"   rS   r4   r5   r7   r6   �
_lists_pos�half�childs	            r(   rQ   zSortedList._expand!  s�   � � �
�
�����������v�c�{��u��z�*��[�[�F����J��e�f�%�D��5�6�"�$�R�.�F�3�K��M�M�#��'�4�(��M�M�#��'�4��8�,��q�	�����s�*����5�M�Q�&�M�"�Q�Y�1�,�E� � �q�	�Q��	� r,   c           	      �*  ��� | j                   }| j                  }t        |�      �|rzt        ��      dz  | j                  k\  rC|j                  ��       t        t        |g �      ��j                  �        | j                  �        n| j                  }�D ]
  } ||�       � y| j                  �|j                  ��fd�t        dt        ��      ��      D �       �       |j                  d� |D �       �       t        ��      | _        | j                  dd�= y)a  Update sorted list by adding all values from `iterable`.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> sl = SortedList()
        >>> sl.update([3, 1, 2])
        >>> sl
        SortedList([1, 2, 3])

        :param iterable: iterable of values to add

        �   Nc              3   �.   �K  � | ]  }�||�z    �� � y �wr   r-   ��.0rS   r4   rI   s     ��r(   �	<genexpr>z$SortedList.update.<locals>.<genexpr>a  �$   �� �� � ?�!=�#� �S�#��+�/�!=��   �r   c              3   �&   K  � | ]	  }|d    �� � y�w�rV   Nr-   �r_   �sublists     r(   r`   z$SortedList.update.<locals>.<genexpr>c  s   � �� �8��g�g�b�k���   �)r5   r6   �sortedrO   r2   rP   r   r   �sortrG   r   r4   �extend�ranger7   )r"   r;   r5   r6   �_add�valr4   rI   s         @@r(   �updatezSortedList.updateC  s�   �� � ����������!����6�{�Q��$�)�)�+����f�%���f�b�1�����������x�x��!�C���I� "���
�
����� ?�!&�q�#�f�+�u�!=�?� 	?����8��8�8���K��	��K�K��Nr,   c                 �   � | j                   }|syt        ||�      }|t        |�      k(  ry| j                  }t        ||   |�      }||   |   |k(  S )aZ  Return true if `value` is an element of the sorted list.

        ``sl.__contains__(value)`` <==> ``value in sl``

        Runtime complexity: `O(log(n))`

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> 3 in sl
        True

        :param value: search for value in sorted list
        :return: true if `value` in sorted list

        F)r6   r   rO   r5   �r"   rR   r6   rS   r5   �idxs         r(   �__contains__zSortedList.__contains__j  s[   � � �������&�%�(���#�f�+��������&��+�u�-���c�{�3��5�(�(r,   c                 ��   � | j                   }|syt        ||�      }|t        |�      k(  ry| j                  }t        ||   |�      }||   |   |k(  r| j	                  ||�       yy)ao  Remove `value` from sorted list if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> sl.discard(5)
        >>> sl.discard(0)
        >>> sl == [1, 2, 3, 4]
        True

        :param value: `value` to discard from sorted list

        N)r6   r   rO   r5   �_deleterp   s         r(   r!   zSortedList.discard�  sk   � �  �������&�%�(���#�f�+��������&��+�u�-���#�;�s��u�$��L�L��c�"� %r,   c                 �`  � | j                   }|st        dj                  |�      �      �t        ||�      }|t	        |�      k(  rt        dj                  |�      �      �| j
                  }t        ||   |�      }||   |   |k(  r| j                  ||�       yt        dj                  |�      �      �)a  Remove `value` from sorted list; `value` must be a member.

        If `value` is not a member, raise ValueError.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> sl.remove(5)
        >>> sl == [1, 2, 3, 4]
        True
        >>> sl.remove(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 not in list

        :param value: `value` to remove from sorted list
        :raises ValueError: if `value` is not in sorted list

        �{0!r} not in listN)r6   �
ValueError�formatr   rO   r5   rt   rp   s         r(   �removezSortedList.remove�  s�   � �( ������0�7�7��>�?�?��&�%�(���#�f�+���0�7�7��>�?�?������&��+�u�-���#�;�s��u�$��L�L��c�"��0�7�7��>�?�?r,   c                 �.  � | j                   }| j                  }| j                  }||   }||= | xj                  dz  c_        t	        |�      }|| j
                  dz	  kD  rH|d   ||<   |r=| j                  |z   }|dkD  r||xx   dz  cc<   |dz
  dz	  }|dkD  r�|dxx   dz  cc<   yyt	        |�      dkD  rK|s|dz  }|dz
  }	||	   j                  ||   �       ||	   d   ||	<   ||= ||= |dd�= | j                  |	�       y|r	|d   ||<   y||= ||= |dd�= y�a�  Delete value at the given `(pos, idx)`.

        Combines lists that are less than half the load level.

        Updates the index when the sublist length is more than half the load
        level. This requires decrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        :param int pos: lists index
        :param int idx: sublist index

        rN   rV   r   N)	r5   r6   r7   r2   rO   r4   r8   rj   rQ   )
r"   rS   rq   r5   r6   r7   rX   �len_lists_posrZ   �prevs
             r(   rt   zSortedList._delete�  sC  � � �������������C�[�
��s�O��	�	�Q��	��J����D�J�J�!�O�,�$�R�.�F�3�K�����s�*���a�i��5�M�Q�&�M�"�Q�Y�1�,�E� �a�i� �q�	�Q��	� � ��[�1�_���q�����7�D��4�L����s��,�!�$�<��+�F�4�L��s���s���q�	��L�L����$�R�.�F�3�K��s���s���q�	r,   c                 �   � |s|S | j                   }|s| j                  �        d}|| j                  z  }|r|dz  s|||dz
     z  }|dz
  dz	  }|r�||z   S )a�  Convert an index pair (lists index, sublist index) into a single
        index number that corresponds to the position of the value in the
        sorted list.

        Many queries require the index be built. Details of the index are
        described in ``SortedList._build_index``.

        Indexing requires traversing the tree from a leaf node to the root. The
        parent of each node is easily computable at ``(pos - 1) // 2``.

        Left-child nodes are always at odd indices and right-child nodes are
        always at even indices.

        When traversing up from a right-child node, increment the total by the
        left-child node.

        The final index is the sum from traversal and the index in the sublist.

        For example, using the index from ``SortedList._build_index``::

            _index = 14 5 9 3 2 4 5
            _offset = 3

        Tree::

                 14
              5      9
            3   2  4   5

        Converting an index pair (2, 3) into a single index involves iterating
        like so:

        1. Starting at the leaf node: offset + alpha = 3 + 2 = 5. We identify
           the node as a left-child node. At such nodes, we simply traverse to
           the parent.

        2. At node 9, position 2, we recognize the node as a right-child node
           and accumulate the left-child in our total. Total is now 5 and we
           traverse to the parent at position 0.

        3. Iteration ends at the root.

        The index is then the sum of the total and sublist index: 5 + 3 = 8.

        :param int pos: lists index
        :param int idx: sublist index
        :return: index in sorted list

        r   rN   )r7   �_build_indexr8   )r"   rS   rq   r7   �totals        r(   �_loczSortedList._loc  sz   � �d ��J������������ 	�t�|�|��� �
 ��7����a���(�� ��7�q�.�C� � �s�{�r,   c                 �  � |dk  rZt        | j                  d   �      }| |k  rt        | j                  �      dz
  ||z   fS || j                  z  }|dk  r%t        d�      �|| j                  k\  rt        d�      �|t        | j                  d   �      k  rd|fS | j                  }|s| j                  �        d}d}t        |�      }||k  r%||   }||k  r|}n
||z  }|dz   }|dz  dz   }||k  r�%|| j                  z
  |fS )ai  Convert an index into an index pair (lists index, sublist index)
        that can be used to access the corresponding lists position.

        Many queries require the index be built. Details of the index are
        described in ``SortedList._build_index``.

        Indexing requires traversing the tree to a leaf node. Each node has two
        children which are easily computable. Given an index, pos, the
        left-child is at ``pos * 2 + 1`` and the right-child is at ``pos * 2 +
        2``.

        When the index is less than the left-child, traversal moves to the
        left sub-tree. Otherwise, the index is decremented by the left-child
        and traversal moves to the right sub-tree.

        At a child node, the indexing pair is computed from the relative
        position of the child node as compared with the offset and the remaining
        index.

        For example, using the index from ``SortedList._build_index``::

            _index = 14 5 9 3 2 4 5
            _offset = 3

        Tree::

                 14
              5      9
            3   2  4   5

        Indexing position 8 involves iterating like so:

        1. Starting at the root, position 0, 8 is compared with the left-child
           node (5) which it is greater than. When greater the index is
           decremented and the position is updated to the right child node.

        2. At node 9 with index 3, we again compare the index to the left-child
           node with value 4. Because the index is the less than the left-child
           node, we simply traverse to the left.

        3. At node 4 with index 3, we recognize that we are at a leaf node and
           stop iterating.

        4. To compute the sublist index, we subtract the offset from the index
           of the leaf node: 5 - 3 = 2. To compute the index in the sublist, we
           simply use the index remaining from iteration. In this case, 3.

        The final index pair from our example is (2, 3) which corresponds to
        index 8 in the sorted list.

        :param int idx: index in sorted list
        :return: (lists index, sublist index) pair

        r   rV   rN   �list index out of range)rO   r5   r2   �
IndexErrorr7   r   r8   )r"   rq   �last_lenr7   rS   rZ   �	len_index�index_childs           r(   �_poszSortedList._posY  s%  � �n ��7��4�;�;�r�?�+�H����!��4�;�;�'�!�+�X��^�;�;��4�9�9��C��Q�w� �!:�;�;��D�I�I���6�7�7���T�[�[��^�$�$��c�6�M����������������K�	��i�� ��-�K��[� ����{�"���a�i���A�X��N�E� �i�� �d�l�l�"�C�(�(r,   c           	      �  � t        t        t        | j                  �      �      }t        |�      dk(  r|| j                  dd d| _        yt        |�      }t        |�      }t        t        t        t        ||�      �      �      }t        |�      dz  r|j                  |d   �       t        |�      dk(  r||z   | j                  dd d| _        ydt        t        t        |�      dz
  d�      �      dz   z  }|j                  t        d|t        |�      z
  �      �       ||g}t        |d   �      dkD  r_t        |d   �      }t        |�      }t        t        t        t        ||�      �      �      }|j                  |�       t        |d   �      dkD  r�_t        t         t#        |�      | j                  �       |dz  dz
  | _        y)a  Build a positional index for indexing the sorted list.

        Indexes are represented as binary trees in a dense array notation
        similar to a binary heap.

        For example, given a lists representation storing integers::

            0: [1, 2, 3]
            1: [4, 5]
            2: [6, 7, 8, 9]
            3: [10, 11, 12, 13, 14]

        The first transformation maps the sub-lists by their length. The
        first row of the index is the length of the sub-lists::

            0: [3, 2, 4, 5]

        Each row after that is the sum of consecutive pairs of the previous
        row::

            1: [5, 9]
            2: [14]

        Finally, the index is built by concatenating these lists together::

            _index = [14, 5, 9, 3, 2, 4, 5]

        An offset storing the start of the first row is also stored::

            _offset = 3

        When built, the index can be used for efficient indexing into the list.
        See the comment and notes on ``SortedList._pos`` for details.

        rN   Nr   rV   �   )�list�maprO   r5   r7   r8   �iterr	   r   �ziprP   �intr
   rj   r   r   r   �reversed)r"   �row0�head�tail�row1�size�tree�rows           r(   r   zSortedList._build_index�  sn  � �H �C��T�[�[�)�*���t�9��>�!�D�K�K��N��D�L���D�z���D�z���G�C��T�4��1�2���t�9�q�=��K�K��R��!��t�9��>�!�D�[�D�K�K��N��D�L���S��S��Y��]�A�.�/�!�3�4�����F�1�d�S��Y�.�/�0��d�|���$�r�(�m�a����R��>�D���:�D��w�s�C��d�O�4�5�C��K�K���	 �$�r�(�m�a�� 	�t�X�d�^�T�[�[�1��a�x�!�|��r,   c                 �  � t        |t        �      �r|j                  | j                  �      \  }}}|dk(  r�||k  r�|dk(  r|| j                  k(  r| j	                  �       S | j                  d||z
  z  k  ri| j                  t        d|�      �      }|| j                  k  r|| j                  t        |d�      �      z  }| j	                  �        | j                  |�      S t        |||�      }|dkD  rt        |�      }| j                  | j                  }}|D ]  } ||�      \  }	}
 ||	|
�       � y| j                  |�      \  }	}
| j                  |	|
�       y)a�  Remove value at `index` from sorted list.

        ``sl.__delitem__(index)`` <==> ``del sl[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> del sl[2]
        >>> sl
        SortedList(['a', 'b', 'd', 'e'])
        >>> del sl[:2]
        >>> sl
        SortedList(['d', 'e'])

        :param index: integer or slice for indexing
        :raises IndexError: if index out of range

        rN   r   �   N)�
isinstance�slice�indicesr2   rG   �_getitemr9   rk   r�   r�   rt   )r"   �index�start�stop�steprI   r�   r�   rt   rS   rq   s              r(   �__delitem__zSortedList.__delitem__�  s/  � �* �e�U�#� %���d�i�i� 8��E�4���q�y�U�T�\��A�:�$�$�)�)�"3��;�;�=�(��Y�Y�!�t�e�|�"4�4�!�]�]�5��u�+=�>�F��d�i�i�'��$�-�-��d�D�0A�"B�B���K�K�M��<�<��/�/��E�4��.�G�
 �a�x�"�7�+�� �I�I�t�|�|�'�D� ����;���S���S�!� !� �y�y��'�H�C���L�L��c�"r,   c                 �  � � � j                   }t        |t        �      �rX|j                  � j                  �      \  }}}|dk(  r�||k  r�|dk(  r*|� j                  k(  rt        t        � j                   g �      S � j                  |�      \  }}||   }||z   |z
  }	t        |�      |	k\  r|||	 S |� j                  k(  rt        |�      dz
  }
t        ||
   �      }	n� j                  |�      \  }
}	||   |d }||dz   |
 }t        t        ||�      }|||
   d|	 z  }|S |dk(  r8||kD  r3� j                  t        |dz   |dz   �      �      }|j                  �        |S t        |||�      }t        � fd�|D �       �      S � j                  r|dk(  r|d   d   S |dk(  r|d   d   S t        d�      �d|cxk  rt        |d   �      k  rn n|d   |   S t        |d   �      }| |cxk  rdk  rn n|d   ||z      S � j                  |�      \  }}||   |   S )a�  Lookup value at `index` in sorted list.

        ``sl.__getitem__(index)`` <==> ``sl[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl[1]
        'b'
        >>> sl[-1]
        'e'
        >>> sl[2:5]
        ['c', 'd', 'e']

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        rN   r   NrV   c              3   �@   �K  � | ]  }�j                  |�      �� � y �wr   )r�   )r_   r�   r"   s     �r(   r`   z)SortedList.__getitem__.<locals>.<genexpr>s  s   �� �� �B�'�����e�,�'�s   �r�   )r5   r�   r�   r�   r2   r   r   r�   rO   r�   �reverserk   r�   r�   )r"   r�   r5   r�   r�   r�   �	start_pos�	start_idx�
start_list�stop_idx�stop_pos�prefix�middler$   r�   �len_lastrS   rq   s   `                 r(   �__getitem__zSortedList.__getitem__0  s<  �� �, �����e�U�#� %���d�i�i� 8��E�4���q�y�U�T�\� �A�:�$�$�)�)�"3�!�$����R�8�8�'+�y�y��'7�$�	�9�#�I�.�
�$�t�+�e�3��
 �z�?�h�.�%�i��9�9��4�9�9�$�"�6�{�Q��H�"�6�(�#3�4�H�)-���4��&�H�h��	�*�9�:�6����Q���9����f�f�5���&��*�9�H�5�5�����r�z�e�d�l����u�T�A�X�u�q�y�'A�B����� ��� �E�4��.�G��B�'�B�B�B��y�y��A�:�!�!�9�Q�<�'��b�[�!�"�:�b�>�)� �!:�;�;��E�*�C��q�	�N�*��a�y��'�'��6�"�:��H��y�5�$�1�$��b�z�(�U�"2�3�3��y�y��'�H�C���#�;�s�#�#r,   c                 �   � d}t        |�      �)z�Raise not-implemented error.

        ``sl.__setitem__(index, value)`` <==> ``sl[index] = value``

        :raises NotImplementedError: use ``del sl[index]`` and
            ``sl.add(value)`` instead

        z3use ``del sl[index]`` and ``sl.add(value)`` instead��NotImplementedError)r"   r�   rR   �messages       r(   �__setitem__zSortedList.__setitem__�  s   � � H��!�'�*�*r,   c                 �@   � t        j                  | j                  �      S )z�Return an iterator over the sorted list.

        ``sl.__iter__()`` <==> ``iter(sl)``

        Iterating the sorted list while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        )r   �from_iterabler5   rE   s    r(   �__iter__zSortedList.__iter__�  s   � � �"�"�4�;�;�/�/r,   c                 �n   � t        j                  t        t        t        | j                  �      �      �      S )z�Return a reverse iterator over the sorted list.

        ``sl.__reversed__()`` <==> ``reversed(sl)``

        Iterating the sorted list while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        )r   r�   r�   r�   r5   rE   s    r(   �__reversed__zSortedList.__reversed__�  s%   � � �"�"�3�x��$�+�+�1F�#G�H�Hr,   c                 �   � t        d�      �)a�  Raise not-implemented error.

        Sorted list maintains values in ascending sort order. Values may not be
        reversed in-place.

        Use ``reversed(sl)`` for an iterator over values in descending sort
        order.

        Implemented to override `MutableSequence.reverse` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``reversed(sl)`` instead

        zuse ``reversed(sl)`` insteadr�   rE   s    r(   r�   zSortedList.reverse�  s   � � "�"@�A�Ar,   c                 �  � | j                   }|st        d�      S t        ||�      j                  | j                   �      \  }}}||k\  rt        d�      S | j                  } ||�      \  }}||k(  r1t        | j                  �      dz
  }	t        | j                  d   �      }
n ||�      \  }	}
| j                  |||	|
|�      S )a�  Return an iterator that slices sorted list from `start` to `stop`.

        The `start` and `stop` index are treated inclusive and exclusive,
        respectively.

        Both `start` and `stop` default to `None` which is automatically
        inclusive of the beginning and end of the sorted list.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> sl = SortedList('abcdefghij')
        >>> it = sl.islice(2, 6)
        >>> list(it)
        ['c', 'd', 'e', 'f']

        :param int start: start index (inclusive)
        :param int stop: stop index (exclusive)
        :param bool reverse: yield values in reverse order
        :return: iterator

        r-   rN   rV   )r2   r�   r�   r�   r�   rO   r5   �_islice)r"   r�   r�   r�   r2   �_r�   �min_pos�min_idx�max_pos�max_idxs              r(   �islicezSortedList.islice�  s�   � �. �y�y�����8�O��u�d�+�3�3�D�I�I�>���t�Q��D�=���8�O��y�y����;�����4�<��$�+�+�&��*�G��$�+�+�b�/�*�G�#�D�z��G�W��|�|�G�W�g�w��H�Hr,   c           
      �@  � | j                   }||kD  rt        d�      S ||k(  rU|r.t        t        ||�      �      }t	        ||   j
                  |�      S t        ||�      }t	        ||   j
                  |�      S |dz   }||k(  r�|rot        |t        ||   �      �      }	t        |�      }
t        t	        ||   j
                  t        |
�      �      t	        ||   j
                  t        |	�      �      �      S t        |t        ||   �      �      }	t        |�      }
t        t	        ||   j
                  |	�      t	        ||   j
                  |
�      �      S |r�t        |t        ||   �      �      }	t        ||�      }t	        |j
                  t        |�      �      }t        |�      }
t        t	        ||   j
                  t        |
�      �      t        j                  t	        t        |�      �      t	        ||   j
                  t        |	�      �      �      S t        |t        ||   �      �      }	t        ||�      }t	        |j
                  |�      }t        |�      }
t        t	        ||   j
                  |	�      t        j                  |�      t	        ||   j
                  |
�      �      S )ay  Return an iterator that slices sorted list using two index pairs.

        The index pairs are (min_pos, min_idx) and (max_pos, max_idx), the
        first inclusive and the latter exclusive. See `_pos` for details on how
        an index is converted to an index pair.

        When `reverse` is `True`, values are yielded from the iterator in
        reverse order.

        r-   rN   )	r5   r�   r�   rk   r�   r�   rO   r   r�   )r"   r�   r�   r�   r�   r�   r5   r�   �next_pos�min_indices�max_indices�sublist_indices�sublistss                r(   r�   zSortedList._islice�  sU  � � �����W����8�O��g���"�5��'�#:�;���6�'�?�6�6��@�@��G�W�-�G��v�g��2�2�G�<�<��Q�;���w���#�G�S����-A�B��#�G�n�����w��3�3�X�k�5J�K���w��3�3�X�k�5J�K�� �
  ���V�G�_�)=�>�K���.�K���F�7�O�/�/��=��F�7�O�/�/��=�� �
 ����V�G�_�)=�>�K�#�H�g�6�O��6�-�-�x��/H�I�H���.�K���F�7�O�/�/��+�1F�G��#�#�C��(�$;�<��F�7�O�/�/��+�1F�G�� � �G�S����%9�:����'�2���v�)�)�?�;���G�n�����w��+�+�[�9�����)���w��+�+�[�9�
� 	
r,   c                 �  � | j                   }|st        d�      S | j                  }|�d}d}nn|d   r5t        ||�      }|t	        |�      k(  rt        d�      S t        ||   |�      }n4t        ||�      }|t	        |�      k(  rt        d�      S t        ||   |�      }|�t	        |�      dz
  }	t	        ||	   �      }
n�|d   r>t        ||�      }	|	t	        |�      k(  r|	dz  }	t	        ||	   �      }
nMt        ||	   |�      }
n=t        ||�      }	|	t	        |�      k(  r|	dz  }	t	        ||	   �      }
nt        ||	   |�      }
| j                  |||	|
|�      S )a�  Create an iterator of values between `minimum` and `maximum`.

        Both `minimum` and `maximum` default to `None` which is automatically
        inclusive of the beginning and end of the sorted list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> sl = SortedList('abcdefghij')
        >>> it = sl.irange('c', 'f')
        >>> list(it)
        ['c', 'd', 'e', 'f']

        :param minimum: minimum value to start iterating
        :param maximum: maximum value to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        r-   r   rN   )r6   r�   r5   r   rO   r   r�   )r"   �minimum�maximum�	inclusiver�   r6   r5   r�   r�   r�   r�   s              r(   �irangezSortedList.irange0  sZ  � �6 �������8�O�����
 �?��G��G���|�%�f�g�6���c�&�k�)���8�O�%�f�W�o�w�?��&�v�w�7���c�&�k�)���8�O�&�v�g���@��
 �?��&�k�A�o�G��&��/�*�G���|�&�v�w�7���c�&�k�)��q�L�G�!�&��/�2�G�*�6�'�?�G�D�G�%�f�g�6���c�&�k�)��q�L�G�!�&��/�2�G�)�&��/�7�C�G��|�|�G�W�g�w��H�Hr,   c                 �   � | j                   S )z~Return the size of the sorted list.

        ``sl.__len__()`` <==> ``len(sl)``

        :return: size of sorted list

        )r2   rE   s    r(   �__len__zSortedList.__len__�  s   � � �y�y�r,   c                 ��   � | j                   }|syt        ||�      }|t        |�      k(  r| j                  S t        | j                  |   |�      }| j                  ||�      S )a�  Return an index to insert `value` in the sorted list.

        If the `value` is already present, the insertion point will be before
        (to the left of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([10, 11, 12, 13, 14])
        >>> sl.bisect_left(12)
        2

        :param value: insertion index of value in sorted list
        :return: index

        r   )r6   r   rO   r2   r5   r�   �r"   rR   r6   rS   rq   s        r(   r   zSortedList.bisect_left�  s[   � �$ �������&�%�(���#�f�+���9�9���$�+�+�c�*�E�2���y�y��c�"�"r,   c                 ��   � | j                   }|syt        ||�      }|t        |�      k(  r| j                  S t        | j                  |   |�      }| j                  ||�      S )a  Return an index to insert `value` in the sorted list.

        Similar to `bisect_left`, but if `value` is already present, the
        insertion point will be after (to the right of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([10, 11, 12, 13, 14])
        >>> sl.bisect_right(12)
        3

        :param value: insertion index of value in sorted list
        :return: index

        r   )r6   r   rO   r2   r5   r�   r�   s        r(   r   zSortedList.bisect_right�  s[   � �$ �������6�5�)���#�f�+���9�9���4�;�;�s�+�U�3���y�y��c�"�"r,   c                 �  � | j                   }|syt        ||�      }|t        |�      k(  ry| j                  }t        ||   |�      }t	        ||�      }|t        |�      k(  r| j
                  | j                  ||�      z
  S t	        ||   |�      }||k(  r||z
  S | j                  ||�      }| j                  ||�      }	||	z
  S )a)  Return number of occurrences of `value` in the sorted list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        >>> sl.count(3)
        3

        :param value: value to count in sorted list
        :return: count

        r   )r6   r   rO   r5   r   r2   r�   )
r"   rR   r6   �pos_leftr5   �idx_left�	pos_right�	idx_right�right�lefts
             r(   �countzSortedList.count�  s�   � � �������v�u�-���s�6�{�"�������v�h�/��7�� ���/�	���F��#��9�9�t�y�y��8�<�<�<� ��	�!2�E�:�	��y� ��x�'�'��	�	�)�Y�/���y�y��8�,���t�|�r,   c                 �$   � | j                  | �      S )zyReturn a shallow copy of the sorted list.

        Runtime complexity: `O(n)`

        :return: new sorted list

        )�	__class__rE   s    r(   �copyzSortedList.copy�  s   � � �~�~�d�#�#r,   c                 �   � t        d�      �)z�Raise not-implemented error.

        Implemented to override `MutableSequence.append` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``sl.add(value)`` instead

        �use ``sl.add(value)`` insteadr�   �r"   rR   s     r(   rP   zSortedList.append  s   � � "�"A�B�Br,   c                 �   � t        d�      �)z�Raise not-implemented error.

        Implemented to override `MutableSequence.extend` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``sl.update(values)`` instead

        z!use ``sl.update(values)`` insteadr�   �r"   rI   s     r(   rj   zSortedList.extend  s   � � "�"E�F�Fr,   c                 �   � t        d�      �)zjRaise not-implemented error.

        :raises NotImplementedError: use ``sl.add(value)`` instead

        r�   r�   )r"   r�   rR   s      r(   rW   zSortedList.insert  s   � � "�"A�B�Br,   c                 �n  � | j                   st        d�      �| j                  }|dk(  r|d   d   }| j                  dd�       |S |dk(  r;t	        |�      dz
  }t	        ||   �      dz
  }||   |   }| j                  ||�       |S d|cxk  rt	        |d   �      k  rn n|d   |   }| j                  d|�       |S t	        |d   �      }| |cxk  rdk  r2n n/t	        |�      dz
  }||z   }||   |   }| j                  ||�       |S | j                  |�      \  }}||   |   }| j                  ||�       |S )a  Remove and return value at `index` in sorted list.

        Raise :exc:`IndexError` if the sorted list is empty or index is out of
        range.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl.pop()
        'e'
        >>> sl.pop(2)
        'c'
        >>> sl
        SortedList(['a', 'b', 'd'])

        :param int index: index of value (default -1)
        :return: value
        :raises IndexError: if index is out of range

        zpop index out of ranger   rV   rN   )r2   r�   r5   rt   rO   r�   )r"   r�   r5   rm   rS   �locr�   rq   s           r(   �popzSortedList.pop'  sL  � �. �y�y��5�6�6������A�:���)�A�,�C��L�L��A���J��B�;��f�+��/�C��f�S�k�"�Q�&�C���+�c�"�C��L�L��c�"��J���&��F�1�I��&���)�E�"�C��L�L��E�"��J��v�b�z�?���9�u� �q� ��f�+��/�C��U�"�C���+�c�"�C��L�L��c�"��J��9�9�U�#���S��S�k�#������S�#���
r,   c                 �  � | j                   }|st        dj                  |�      �      �|�d}|dk  r||z  }|dk  rd}|�|}|dk  r||z  }||kD  r|}||k  rt        dj                  |�      �      �| j                  }t	        ||�      }|t        |�      k(  rt        dj                  |�      �      �| j                  }t	        ||   |�      }||   |   |k7  rt        dj                  |�      �      �|dz  }| j                  ||�      }	||	k  r|	|k  r|	S | j                  |�      dz
  }
||
k  r|S t        dj                  |�      �      �)aq  Return first index of value in sorted list.

        Raise ValueError if `value` is not present.

        Index must be between `start` and `stop` for the `value` to be
        considered present. The default value, None, for `start` and `stop`
        indicate the beginning and end of the sorted list.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl.index('d')
        3
        >>> sl.index('z')
        Traceback (most recent call last):
          ...
        ValueError: 'z' is not in list

        :param value: value in sorted list
        :param int start: start index (default None, start of sorted list)
        :param int stop: stop index (default None, end of sorted list)
        :return: index of value
        :raises ValueError: if value is not present

        �{0!r} is not in listr   rN   )	r2   rw   rx   r6   r   rO   r5   r�   �_bisect_right)r"   rR   r�   r�   r2   r6   r�   r5   r�   r�   r�   s              r(   r�   zSortedList.indexc  sp  � �8 �y�y����3�:�:�5�A�B�B��=��E��1�9��T�M�E��1�9��E��<��D��!�8��D�L�D��$�;��D��5�=��3�:�:�5�A�B�B������v�u�-���s�6�{�"��3�:�:�5�A�B�B������v�h�/��7���(��H�%��.��3�:�:�5�A�B�B���	���y�y��8�,���D�=��t�|����&�&�u�-��1�E���~����/�6�6�u�=�>�>r,   c                 �|   � t        t        | j                  g �      }|j                  |�       | j	                  |�      S )a�  Return new sorted list containing all values in both sequences.

        ``sl.__add__(other)`` <==> ``sl + other``

        Values in `other` do not need to be in sorted order.

        Runtime complexity: `O(n*log(n))`

        >>> sl1 = SortedList('bat')
        >>> sl2 = SortedList('cat')
        >>> sl1 + sl2
        SortedList(['a', 'a', 'b', 'c', 't', 't'])

        :param other: other iterable
        :return: new sorted list

        )r   r   r5   rj   r�   �r"   �otherrI   s      r(   �__add__zSortedList.__add__�  s1   � �$ ��d�k�k�2�.�����e���~�~�f�%�%r,   c                 �(   � | j                  |�       | S )a�  Update sorted list with values from `other`.

        ``sl.__iadd__(other)`` <==> ``sl += other``

        Values in `other` do not need to be in sorted order.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> sl = SortedList('bat')
        >>> sl += 'cat'
        >>> sl
        SortedList(['a', 'a', 'b', 'c', 't', 't'])

        :param other: other iterable
        :return: existing sorted list

        )r9   )r"   r�   s     r(   �__iadd__zSortedList.__iadd__�  s   � �$ 	���U���r,   c                 �`   � t        t        | j                  g �      |z  }| j                  |�      S )aj  Return new sorted list with `num` shallow copies of values.

        ``sl.__mul__(num)`` <==> ``sl * num``

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList('abc')
        >>> sl * 3
        SortedList(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'])

        :param int num: count of shallow copies
        :return: new sorted list

        )r   r   r5   r�   �r"   �numrI   s      r(   �__mul__zSortedList.__mul__�  s*   � � ��d�k�k�2�.��4���~�~�f�%�%r,   c                 �   � t        t        | j                  g �      |z  }| j                  �        | j	                  |�       | S )a�  Update the sorted list with `num` shallow copies of values.

        ``sl.__imul__(num)`` <==> ``sl *= num``

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList('abc')
        >>> sl *= 3
        >>> sl
        SortedList(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'])

        :param int num: count of shallow copies
        :return: existing sorted list

        )r   r   r5   rG   r9   r�   s      r(   �__imul__zSortedList.__imul__�  s5   � �  ��d�k�k�2�.��4���������V���r,   c                 �   � � � fd�}� j                   }dj                  |�      |_         d}t        |j                  |||�      �      |_        |S )zMake comparator method.c                 ��   �� t        |t        �      st        S | j                  }t	        |�      }||k7  r�t
        u ry�t        u ryt        | |�      D ]  \  }}||k7  s� �||�      c S   �||�      S )z,Compare method for sorted list and sequence.FT)r�   r   �NotImplementedr2   rO   r   r   r�   )r"   r�   �self_len�	len_other�alpha�beta�seq_ops         �r(   �comparerz'SortedList.__make_cmp.<locals>.comparer  sy   �� ��e�X�.�%�%��y�y�H��E�
�I��9�$��R�<� ��R�<��"�4��/���t��D�=�!�%��.�.�  0� �(�I�.�.r,   z__{0}__a7  Return true if and only if sorted list is {0} `other`.

        ``sl.__{1}__(other)`` <==> ``sl {2} other``

        Comparisons use lexicographical order as with sequences.

        Runtime complexity: `O(n)`

        :param other: `other` sequence
        :return: true if sorted list is {0} `other`

        )�__name__rx   r   �__doc__)r�   �symbol�docr�   �seq_op_name�doc_strs   `     r(   �
__make_cmpzSortedList.__make_cmp
  sN   �� �	/�( �o�o��%�,�,�[�9����� "�'�.�.��k�6�"J�K����r,   z==zequal toz!=znot equal to�<z	less than�>zgreater thanz<=zless than or equal toz>=zgreater than or equal toc                 �T   � t        t        | j                  g �      }t        | �      |ffS r   )r   r   r5   �typer�   s     r(   �
__reduce__zSortedList.__reduce__;  s%   � ���d�k�k�2�.���T�
�V�I�&�&r,   c                 �^   � dj                  t        | �      j                  t        | �      �      S )z�Return string representation of sorted list.

        ``sl.__repr__()`` <==> ``repr(sl)``

        :return: string representation

        z
{0}({1!r}))rx   r  r�   r�   rE   s    r(   �__repr__zSortedList.__repr__@  s%   � � �"�"�4��:�#6�#6��T�
�C�Cr,   c                 �  �� 	 | j                   dk\  sJ �t        | j                  �      t        | j                  �      k(  sJ �| j                  t        d� | j                  D �       �      k(  sJ �| j                  D ],  }t        dt        |�      �      D ]  }||dz
     ||   k  r�J � �. t        dt        | j                  �      �      D ],  }| j                  |dz
     d   | j                  |   d   k  r�,J � t        t        | j                  �      �      D ]&  }| j                  |   | j                  |   d   k(  r�&J � | j                   dz  �t        �fd�| j                  D �       �      sJ �| j                   dz	  }t        dt        | j                  �      dz
  �      D ]  }t        | j                  |   �      |k\  r�J � | j                  �rw| j                  | j                  d   k(  sJ �t        | j                  �      | j                  t        | j                  �      z   k(  sJ �t        t        | j                  �      �      D ];  }| j                  | j                  |z      }|t        | j                  |   �      k(  r�;J � t        | j                  �      D ]�  }|dz  dz   }|t        | j                  �      k\  r| j                  |   dk(  r�6J �|dz   t        | j                  �      k(  r"| j                  |   | j                  |   k(  r�sJ �| j                  |   | j                  |dz      z   }|| j                  |   k(  r��J � yy#  t        j                  t        j                  ��       t        d| j                  �       t        d	| j                   �       t        d
| j                  �       t        dt        | j                  �      �       t        d| j                  �       t        dt        | j                  �      �       t        d| j                  �       t        dt        | j                  �      �       t        d| j                  �       � xY w)zNCheck invariants of sorted list.

        Runtime complexity: `O(n)`

        r\   c              3   �2   K  � | ]  }t        |�      �� � y �wr   �rO   re   s     r(   r`   z$SortedList._check.<locals>.<genexpr>U  �   � �� �#L��W�C��L���   �rN   rV   r   c              3   �:   �K  � | ]  }t        |�      �k  �� � y �wr   r  �r_   rf   �doubles     �r(   r`   z$SortedList._check.<locals>.<genexpr>j  �   �� �� �I�[�'�s�7�|�v�-�[��   ���filerO   rH   �offsetr�   r�   �	len_maxes�maxes�	len_lists�listsN)r4   rO   r6   r5   r2   �sumrk   �allr7   r8   �	traceback�	print_exc�sys�stdout�print)r"   rf   rS   rY   �leafrZ   �	child_sumr  s          @r(   �_checkzSortedList._checkL  s�  �� �A	��:�:��?�"�?��t�{�{�#�s�4�;�;�'7�7�7�7��9�9��#L����#L� L�L�L�L�  �;�;�� ��C��L�1�C�"�3��7�+�w�s�|�;�;�;� 2� '� �Q��D�K�K� 0�1���{�{�3��7�+�B�/�4�;�;�s�3C�A�3F�F�F�F� 2�
 �S����-�.���{�{�3�'�4�;�;�s�+;�B�+?�?�?�?� /�
 �Z�Z�1�_�F��I�T�[�[�I�I�I�I�
 �:�:��?�D��Q��D�K�K� 0�1� 4�5���4�;�;�s�+�,��4�4�4� 6� �{�{��y�y�D�K�K��N�2�2�2��4�;�;�'�4�<�<�#�d�k�k�:J�+J�J�J�J� !��T�[�[�!1�2�C��;�;�t�|�|�c�'9�:�D��3�t�{�{�3�'7�#8�8�8�8� 3� !����.�C� �A�X��N�E���D�K�K� 0�0�#�{�{�3�/�1�4�4�4����c�$�+�+�&6�6�#�{�{�3�/�4�;�;�u�3E�E�E�E�$(�K�K��$6����U�Q�Y�9O�$O�	�(�D�K�K��,<�<�<�<� /� ��*	����S�Z�Z�0��%����#��&�$�*�*�%��(�D�L�L�)��+�s�4�;�;�/�0��'�4�;�;�'��+�s�4�;�;�/�0��'�4�;�;�'��+�s�4�;�;�/�0��'�4�;�;�'��sB   �BM �"AM �2AM �9BM �;C M �<AM �
<M �6M �>M �DQ�NN)NNF�NN)TTF)rV   )Fr�   �
__module__�__qualname__r�   r3   r<   r?   �propertyr#   rJ   rL   rG   r   rQ   rn   r9   rr   r!   ry   rt   r�   r�   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r   r   �bisectr�   r�   r�   �__copy__rP   rj   rW   r�   r�   r�   �__radd__r�   r�   �__rmul__r�   �_SortedList__make_cmpr   �__eq__r   �__ne__r   �__lt__r   �__gt__r   �__le__r   �__ge__�staticmethodr	  r.   r  r&  r-   r,   r(   r0   r0   U   s�  � �6�n ��#�<J�< �� ���0
� �F�!�H�D"�H �G�)�>#�B$@�N4�nN�b[)�|B$�J1#�hV$�p �H�
+�	0�	I�B�$+I�\=
�@ <H��PI�f�#�@#�> �F� �M�%�P$� �H�	C�	G�C�9�xJ?�Z&�, �H��,&�$ �H��,%�P ��D�*�-�F���D�.�1�F���C��-�F���C��0�F���D�"9�:�F���D�"<�=�F��j�)�J�'�
 ��D� �D�Gr,   r0   c                 �   � | S )zIdentity function.r-   )rR   s    r(   �identityr9  �  s   � ��Lr,   c                   �  � e Zd ZdZdefd�Zdefd�Zed� �       Zd� Z	e	Z
d� Zd� Zd	� ZeZd
� Zd� Zd� Zd� Z	 	 dd�Z	 	 dd�ZeZd� Zd� ZeZd� ZeZd� ZeZeZd� Zd� ZeZ dd�Z!d� Z"e"Z#d� Z$d� Z% e&�       d� �       Z'd� Z(y)r@   ai  Sorted-key list is a subtype of sorted list.

    The sorted-key list maintains values in comparison order based on the
    result of a key function applied to every value.

    All the same methods that are available in :class:`SortedList` are also
    available in :class:`SortedKeyList`.

    Additional methods provided:

    * :attr:`SortedKeyList.key`
    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Some examples below use:

    >>> from operator import neg
    >>> neg
    <built-in function neg>
    >>> neg(1)
    -1

    Nc                 �   � || _         d| _        | j                  | _        g | _        g | _        g | _        g | _        d| _        |�| j                  |�       yy)a6  Initialize sorted-key list instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted-key list.

        Optional `key` argument defines a callable that, like the `key`
        argument to Python's `sorted` function, extracts a comparison key from
        each value. The default is the identity function.

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl
        SortedKeyList([], key=<built-in function neg>)
        >>> skl = SortedKeyList([3, 1, 2], key=neg)
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)

        r   N)
�_keyr2   r3   r4   r5   �_keysr6   r7   r8   r9   r:   s      r(   r<   zSortedKeyList.__init__�  sY   � �0 ��	���	��-�-��
������
�������������L�L��"�  r,   c                 �,   � t         j                  | �      S r   )r>   r?   rB   s      r(   r?   zSortedKeyList.__new__�  s   � ��~�~�c�"�"r,   c                 �   � | j                   S )z4Function used to extract comparison key from values.)r<  rE   s    r(   r#   zSortedKeyList.key�  s   � � �y�y�r,   c                 �   � d| _         | j                  dd�= | j                  dd�= | j                  dd�= | j                  dd�= y)zURemove all values from sorted-key list.

        Runtime complexity: `O(n)`

        r   N)r2   r5   r=  r6   r7   rE   s    r(   rL   zSortedKeyList.clear�  s7   � � ��	��K�K��N��J�J�q�M��K�K��N��K�K��Nr,   c                 �6  � | j                   }| j                  }| j                  }| j                  |�      }|r�t	        ||�      }|t        |�      k(  r3|dz  }||   j                  |�       ||   j                  |�       |||<   n9t	        ||   |�      }||   j                  ||�       ||   j                  ||�       | j                  |�       n5|j                  |g�       |j                  |g�       |j                  |�       | xj                  dz  c_	        y)a{  Add `value` to sorted-key list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl.add(3)
        >>> skl.add(1)
        >>> skl.add(2)
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param value: value to add to sorted-key list

        rN   N)
r5   r=  r6   r<  r   rO   rP   rW   rQ   r2   )r"   rR   r5   r=  r6   r#   rS   rq   s           r(   r   zSortedKeyList.add�  s�   � �  �����
�
�������i�i������v�s�+�C��c�&�k�!��q����s��"�"�5�)��c�
�!�!�#�&�!��s��"�5��:�s�3���s��"�"�3��.��c�
�!�!�#�s�+��L�L����M�M�5�'�"��L�L�#����M�M�#���	�	�Q��	r,   c                 �  � | j                   }| j                  }| j                  }t        ||   �      | j                  dz  kD  r�| j
                  }| j                  }||   }||   }||d }	||d }
||d�= ||d�= |d   ||<   |j                  |dz   |	�       |j                  |dz   |
�       |j                  |dz   |
d   �       |dd�= y|r7| j                  |z   }|r||xx   dz  cc<   |dz
  dz	  }|r�|dxx   dz  cc<   yyrU   )r5   r=  r7   rO   r4   r6   rW   r8   )r"   rS   r5   r=  r7   r6   r4   rX   �	_keys_posrY   �	half_keysrZ   s               r(   rQ   zSortedKeyList._expand  s  � � �����
�
�������u�S�z�?�d�j�j�A�o�.��[�[�F��J�J�E����J��c�
�I��e�f�%�D�!�%�&�)�I��5�6�"��%�&�!�#�B�-�F�3�K��M�M�#��'�4�(��L�L��q��)�,��M�M�#��'�9�R�=�1��q�	�����s�*����5�M�Q�&�M�"�Q�Y�1�,�E� � �q�	�Q��	� r,   c           	      �  � ��� � j                   }� j                  }� j                  }t        |� j                  ��      �|r�t        ��      dz  � j                  k\  rO|j                  ��       t        t        |g �      ��j                  � j                  ��       � j                  �        n� j                  }�D ]
  } ||�       � y� j                  �|j                  ��fd�t        dt        ��      ��      D �       �       |j                  � fd�|D �       �       |j                  d� |D �       �       t        ��      � _        � j                   dd�= y)at  Update sorted-key list by adding all values from `iterable`.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl.update([3, 1, 2])
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param iterable: iterable of values to add

        �r#   r\   Nc              3   �.   �K  � | ]  }�||�z    �� � y �wr   r-   r^   s     ��r(   r`   z'SortedKeyList.update.<locals>.<genexpr>e  ra   rb   r   c              3   �\   �K  � | ]#  }t        t        �j                  |�      �      �� �% y �wr   )r�   r�   r<  )r_   �_listr"   s     �r(   r`   z'SortedKeyList.update.<locals>.<genexpr>g  s"   �� �� �E�f�U�T�#�d�i�i��/�0�f�s   �),c              3   �&   K  � | ]	  }|d    �� � y�wrd   r-   re   s     r(   r`   z'SortedKeyList.update.<locals>.<genexpr>h  s   � �� �7��g�g�b�k��rg   )r5   r=  r6   rh   r<  rO   r2   rP   r   r   ri   rG   r   r4   rj   rk   r7   )	r"   r;   r5   r=  r6   rl   rm   r4   rI   s	   `      @@r(   rn   zSortedKeyList.updateE  s  �� � �����
�
��������d�i�i�0����6�{�Q��$�)�)�+����f�%���f�b�1������	�	��*������x�x��!�C���I� "���
�
����� ?�!&�q�#�f�+�u�!=�?� 	?����E�f�E�E����7��7�7���K��	��K�K��Nr,   c                 �v  � | j                   }|sy| j                  |�      }t        ||�      }|t        |�      k(  ry| j                  }| j
                  }t        ||   |�      }t        |�      }t        ||   �      }		 ||   |   |k7  ry||   |   |k(  ry|dz  }||	k(  r|dz  }||k(  ryt        ||   �      }	d}�>)a�  Return true if `value` is an element of the sorted-key list.

        ``skl.__contains__(value)`` <==> ``value in skl``

        Runtime complexity: `O(log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList([1, 2, 3, 4, 5], key=neg)
        >>> 3 in skl
        True

        :param value: search for value in sorted-key list
        :return: true if `value` in sorted-key list

        FTrN   r   �r6   r<  r   rO   r5   r=  �
r"   rR   r6   r#   rS   r5   r=  rq   �len_keys�len_sublists
             r(   rr   zSortedKeyList.__contains__o  s�   � �  �������i�i�����&�#�&���#�f�+��������
�
���%��*�c�*���u�:���%��*�o����S�z�#��#�%���c�{�3��5�(���1�H�C��k�!��q����(�?� �!�%��*�o���� r,   c                 �  � | j                   }|sy| j                  |�      }t        ||�      }|t        |�      k(  ry| j                  }| j
                  }t        ||   |�      }t        |�      }t        ||   �      }		 ||   |   |k7  ry||   |   |k(  r| j                  ||�       y|dz  }||	k(  r|dz  }||k(  ryt        ||   �      }	d}�P)a�  Remove `value` from sorted-key list if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.discard(1)
        >>> skl.discard(0)
        >>> skl == [5, 4, 3, 2]
        True

        :param value: `value` to discard from sorted-key list

        NrN   r   )r6   r<  r   rO   r5   r=  rt   rM  s
             r(   r!   zSortedKeyList.discard�  s�   � �" �������i�i�����&�#�&���#�f�+��������
�
���%��*�c�*���u�:���%��*�o����S�z�#��#�%���c�{�3��5�(����S�#�&���1�H�C��k�!��q����(�?��!�%��*�o���� r,   c                 �b  � | j                   }|st        dj                  |�      �      �| j                  |�      }t	        ||�      }|t        |�      k(  rt        dj                  |�      �      �| j                  }| j                  }t	        ||   |�      }t        |�      }t        ||   �      }		 ||   |   |k7  rt        dj                  |�      �      �||   |   |k(  r| j                  ||�       y|dz  }||	k(  r4|dz  }||k(  rt        dj                  |�      �      �t        ||   �      }	d}��)aS  Remove `value` from sorted-key list; `value` must be a member.

        If `value` is not a member, raise ValueError.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([1, 2, 3, 4, 5], key=neg)
        >>> skl.remove(5)
        >>> skl == [4, 3, 2, 1]
        True
        >>> skl.remove(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 not in list

        :param value: `value` to remove from sorted-key list
        :raises ValueError: if `value` is not in sorted-key list

        rv   NrN   r   )	r6   rw   rx   r<  r   rO   r5   r=  rt   rM  s
             r(   ry   zSortedKeyList.remove�  s7  � �* ������0�7�7��>�?�?��i�i�����&�#�&���#�f�+���0�7�7��>�?�?������
�
���%��*�c�*���u�:���%��*�o����S�z�#��#�%� �!4�!;�!;�E�!B�C�C��c�{�3��5�(����S�#�&���1�H�C��k�!��q����(�?�$�%8�%?�%?��%F�G�G�!�%��*�o���� r,   c                 �  � | j                   }| j                  }| j                  }| j                  }||   }||   }||= ||= | xj                  dz  c_        t        |�      }	|	| j                  dz	  kD  rH|d   ||<   |r=| j                  |z   }
|
dkD  r||
xx   dz  cc<   |
dz
  dz	  }
|
dkD  r�|dxx   dz  cc<   yyt        |�      dkD  re|s|dz  }|dz
  }||   j                  ||   �       ||   j                  ||   �       ||   d   ||<   ||= ||= ||= |dd�= | j                  |�       y|	r	|d   ||<   y||= ||= ||= |dd�= yr{   )
r5   r=  r6   r7   r2   rO   r4   r8   rj   rQ   )r"   rS   rq   r5   r=  r6   r7   �keys_pos�	lists_pos�len_keys_posrZ   r}   s               r(   rt   zSortedKeyList._delete  s  � � �����
�
������������:���3�K�	��S�M��c�N��	�	�Q��	��8�}���4�:�:��?�+�"�2�,�F�3�K�����s�*���a�i��5�M�Q�&�M�"�Q�Y�1�,�E� �a�i� �q�	�Q��	� � ��Z�!�^���q�����7�D��$�K���u�S�z�*��4�L����s��,� ��;�r�?�F�4�L��s���c�
��s���q�	��L�L����"�2�,�F�3�K��s���c�
��s���q�	r,   c                 �   � |�| j                  |�      nd}|�| j                  |�      nd}| j                  ||||��      S )a  Create an iterator of values between `minimum` and `maximum`.

        Both `minimum` and `maximum` default to `None` which is automatically
        inclusive of the beginning and end of the sorted-key list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> from operator import neg
        >>> skl = SortedKeyList([11, 12, 13, 14, 15], key=neg)
        >>> it = skl.irange(14.5, 11.5)
        >>> list(it)
        [14, 13, 12]

        :param minimum: minimum value to start iterating
        :param maximum: maximum value to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        N)�min_key�max_keyr�   r�   )r<  �_irange_key)r"   r�   r�   r�   r�   rW  rX  s          r(   r�   zSortedKeyList.irangeB  sP   � �8 )0�(;�$�)�)�G�$���(/�(;�$�)�)�G�$�������W���  � 
� 	
r,   c                 �  � | j                   }|st        d�      S | j                  }|�d}d}nn|d   r5t        ||�      }|t	        |�      k(  rt        d�      S t        ||   |�      }n4t        ||�      }|t	        |�      k(  rt        d�      S t        ||   |�      }|�t	        |�      dz
  }	t	        ||	   �      }
n�|d   r>t        ||�      }	|	t	        |�      k(  r|	dz  }	t	        ||	   �      }
nMt        ||	   |�      }
n=t        ||�      }	|	t	        |�      k(  r|	dz  }	t	        ||	   �      }
nt        ||	   |�      }
| j                  |||	|
|�      S )a  Create an iterator of values between `min_key` and `max_key`.

        Both `min_key` and `max_key` default to `None` which is automatically
        inclusive of the beginning and end of the sorted-key list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> from operator import neg
        >>> skl = SortedKeyList([11, 12, 13, 14, 15], key=neg)
        >>> it = skl.irange_key(-14, -12)
        >>> list(it)
        [14, 13, 12]

        :param min_key: minimum key to start iterating
        :param max_key: maximum key to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        r-   r   rN   )r6   r�   r=  r   rO   r   r�   )r"   rW  rX  r�   r�   r6   r=  r�   r�   r�   r�   s              r(   �
irange_keyzSortedKeyList.irange_keyf  sZ  � �8 �������8�O��
�
��
 �?��G��G���|�%�f�g�6���c�&�k�)���8�O�%�e�G�n�g�>��&�v�w�7���c�&�k�)���8�O�&�u�W�~�w�?��
 �?��&�k�A�o�G��%��.�)�G���|�&�v�w�7���c�&�k�)��q�L�G�!�%��.�1�G�*�5��>�7�C�G�%�f�g�6���c�&�k�)��q�L�G�!�%��.�1�G�)�%��.�'�B�G��|�|�G�W�g�w��H�Hr,   c                 �B   � | j                  | j                  |�      �      S )a  Return an index to insert `value` in the sorted-key list.

        If the `value` is already present, the insertion point will be before
        (to the left of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_left(1)
        4

        :param value: insertion index of value in sorted-key list
        :return: index

        )�_bisect_key_leftr<  r�   s     r(   r   zSortedKeyList.bisect_left�  s   � �& �$�$�T�Y�Y�u�%5�6�6r,   c                 �B   � | j                  | j                  |�      �      S )a5  Return an index to insert `value` in the sorted-key list.

        Similar to `bisect_left`, but if `value` is already present, the
        insertion point will be after (to the right of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_right(1)
        5

        :param value: insertion index of value in sorted-key list
        :return: index

        )�_bisect_key_rightr<  r�   s     r(   r   zSortedKeyList.bisect_right�  s   � �& �%�%�d�i�i��&6�7�7r,   c                 ��   � | j                   }|syt        ||�      }|t        |�      k(  r| j                  S t        | j                  |   |�      }| j                  ||�      S )a  Return an index to insert `key` in the sorted-key list.

        If the `key` is already present, the insertion point will be before (to
        the left of) any existing keys.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_key_left(-1)
        4

        :param key: insertion index of key in sorted-key list
        :return: index

        r   )r6   r   rO   r2   r=  r�   �r"   r#   r6   rS   rq   s        r(   �bisect_key_leftzSortedKeyList.bisect_key_left�  sZ   � �& �������&�#�&���#�f�+���9�9���$�*�*�S�/�3�/���y�y��c�"�"r,   c                 ��   � | j                   }|syt        ||�      }|t        |�      k(  r| j                  S t        | j                  |   |�      }| j                  ||�      S )a4  Return an index to insert `key` in the sorted-key list.

        Similar to `bisect_key_left`, but if `key` is already present, the
        insertion point will be after (to the right of) any existing keys.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_key_right(-1)
        5

        :param key: insertion index of key in sorted-key list
        :return: index

        r   )r6   r   rO   r2   r=  r�   ra  s        r(   �bisect_key_rightzSortedKeyList.bisect_key_right	  sZ   � �& �������6�3�'���#�f�+���9�9���4�:�:�c�?�C�0���y�y��c�"�"r,   c                 �  � | j                   }|sy| j                  |�      }t        ||�      }|t        |�      k(  ry| j                  }| j
                  }t        ||   |�      }d}t        |�      }	t        ||   �      }
	 ||   |   |k7  r|S ||   |   |k(  r|dz  }|dz  }||
k(  r|dz  }||	k(  r|S t        ||   �      }
d}�D)ad  Return number of occurrences of `value` in the sorted-key list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([4, 4, 4, 4, 3, 3, 3, 2, 2, 1], key=neg)
        >>> skl.count(2)
        2

        :param value: value to count in sorted-key list
        :return: count

        r   rN   rL  )r"   rR   r6   r#   rS   r5   r=  rq   r�   rN  rO  s              r(   r�   zSortedKeyList.count3	  s�   � � �������i�i�����&�#�&���#�f�+��������
�
���%��*�c�*�����u�:���%��*�o����S�z�#��#�%����c�{�3��5�(���
���1�H�C��k�!��q����(�?� �L�!�%��*�o���� r,   c                 �<   � | j                  | | j                  ��      S )z�Return a shallow copy of the sorted-key list.

        Runtime complexity: `O(n)`

        :return: new sorted-key list

        rF  )r�   r<  rE   s    r(   r�   zSortedKeyList.copya	  s   � � �~�~�d��	�	�~�2�2r,   c                 �p  � | j                   }|st        dj                  |�      �      �|�d}|dk  r||z  }|dk  rd}|�|}|dk  r||z  }||kD  r|}||k  rt        dj                  |�      �      �| j                  }| j	                  |�      }t        ||�      }|t        |�      k(  rt        dj                  |�      �      �|dz  }| j                  }| j                  }	t        |	|   |�      }
t        |	�      }t        |	|   �      }	 |	|   |
   |k7  rt        dj                  |�      �      �||   |
   |k(  r&| j                  ||
�      }||cxk  r|k  r|S  ||kD  rn?|
dz  }
|
|k(  r4|dz  }||k(  rt        dj                  |�      �      �t        |	|   �      }d}
��t        dj                  |�      �      �)a�  Return first index of value in sorted-key list.

        Raise ValueError if `value` is not present.

        Index must be between `start` and `stop` for the `value` to be
        considered present. The default value, None, for `start` and `stop`
        indicate the beginning and end of the sorted-key list.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.index(2)
        3
        >>> skl.index(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 is not in list

        :param value: value in sorted-key list
        :param int start: start index (default None, start of sorted-key list)
        :param int stop: stop index (default None, end of sorted-key list)
        :return: index of value
        :raises ValueError: if value is not present

        r�   r   rN   )
r2   rw   rx   r6   r<  r   rO   r5   r=  r�   )r"   rR   r�   r�   r2   r6   r#   rS   r5   r=  rq   rN  rO  r�   s                 r(   r�   zSortedKeyList.indexn	  s�  � �: �y�y����3�:�:�5�A�B�B��=��E��1�9��T�M�E��1�9��E��<��D��!�8��D�L�D��$�;��D��5�=��3�:�:�5�A�B�B������i�i�����&�#�&���#�f�+���3�:�:�5�A�B�B���	�������
�
���%��*�c�*���u�:���%��*�o����S�z�#��#�%� �!7�!>�!>�u�!E�F�F��c�{�3��5�(��i�i��S�)���C�'�4�'��J� (��4�Z���1�H�C��k�!��q����(�?�$�%;�%B�%B�5�%I�J�J�!�%��*�o���� �" �/�6�6�u�=�>�>r,   c                 �   � t        t        | j                  g �      }|j                  |�       | j	                  || j
                  ��      S )a)  Return new sorted-key list containing all values in both sequences.

        ``skl.__add__(other)`` <==> ``skl + other``

        Values in `other` do not need to be in sorted-key order.

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl1 = SortedKeyList([5, 4, 3], key=neg)
        >>> skl2 = SortedKeyList([2, 1, 0], key=neg)
        >>> skl1 + skl2
        SortedKeyList([5, 4, 3, 2, 1, 0], key=<built-in function neg>)

        :param other: other iterable
        :return: new sorted-key list

        rF  )r   r   r5   rj   r�   r<  r�   s      r(   r�   zSortedKeyList.__add__�	  s9   � �& ��d�k�k�2�.�����e���~�~�f�$�)�)�~�4�4r,   c                 �x   � t        t        | j                  g �      |z  }| j                  || j                  ��      S )a�  Return new sorted-key list with `num` shallow copies of values.

        ``skl.__mul__(num)`` <==> ``skl * num``

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList([3, 2, 1], key=neg)
        >>> skl * 2
        SortedKeyList([3, 3, 2, 2, 1, 1], key=<built-in function neg>)

        :param int num: count of shallow copies
        :return: new sorted-key list

        rF  )r   r   r5   r�   r<  r�   s      r(   r�   zSortedKeyList.__mul__�	  s2   � �  ��d�k�k�2�.��4���~�~�f�$�)�)�~�4�4r,   c                 �j   � t        t        | j                  g �      }t        | �      || j                  ffS r   )r   r   r5   r  r#   r�   s     r(   r	  zSortedKeyList.__reduce__�	  s,   � ���d�k�k�2�.���T�
�V�T�X�X�.�/�/r,   c                 �x   � t        | �      j                  }dj                  |t        | �      | j                  �      S )z�Return string representation of sorted-key list.

        ``skl.__repr__()`` <==> ``repr(skl)``

        :return: string representation

        z{0}({1!r}, key={2!r}))r  r�   rx   r�   r<  )r"   �	type_names     r(   r  zSortedKeyList.__repr__�	  s0   � � ��J�'�'�	�&�-�-�i��d��T�Y�Y�O�Or,   c                 �
  �� 	 | j                   dk\  sJ �t        | j                  �      t        | j                  �      cxk(  rt        | j                  �      k(  sJ � J �| j
                  t        d� | j                  D �       �      k(  sJ �| j                  D ],  }t        dt        |�      �      D ]  }||dz
     ||   k  r�J � �. t        dt        | j                  �      �      D ],  }| j                  |dz
     d   | j                  |   d   k  r�,J � t        | j                  | j                  �      D ]H  \  }}t        |�      t        |�      k(  sJ �t        ||�      D ]  \  }}| j                  |�      |k(  r�J � �J t        t        | j                  �      �      D ]&  }| j                  |   | j                  |   d   k(  r�&J � | j                   dz  �t        �fd�| j                  D �       �      sJ �| j                   dz	  }t        dt        | j                  �      dz
  �      D ]  }t        | j                  |   �      |k\  r�J � | j                  �rw| j
                  | j                  d   k(  sJ �t        | j                  �      | j                  t        | j                  �      z   k(  sJ �t        t        | j                  �      �      D ];  }| j                  | j                  |z      }|t        | j                  |   �      k(  r�;J � t        | j                  �      D ]�  }|dz  dz   }	|	t        | j                  �      k\  r| j                  |   dk(  r�6J �|	dz   t        | j                  �      k(  r"| j                  |   | j                  |	   k(  r�sJ �| j                  |	   | j                  |	dz      z   }
|
| j                  |   k(  r��J � yy#  t        j                  t        j                   ��       t#        d| j
                  �       t#        d	| j                   �       t#        d
| j                  �       t#        dt        | j                  �      �       t#        d| j                  �       t#        dt        | j                  �      �       t#        d| j                  �       t#        dt        | j                  �      �       t#        d| j                  �       t#        dt        | j                  �      �       t#        d| j                  �       � xY w)zRCheck invariants of sorted-key list.

        Runtime complexity: `O(n)`

        r\   c              3   �2   K  � | ]  }t        |�      �� � y �wr   r  re   s     r(   r`   z'SortedKeyList._check.<locals>.<genexpr>
  r  r  rN   rV   r   c              3   �:   �K  � | ]  }t        |�      �k  �� � y �wr   r  r  s     �r(   r`   z'SortedKeyList._check.<locals>.<genexpr>(
  r  r  r  rO   rH   r  r�   r�   r  r  rN  �keysr  r  N)r4   rO   r6   r5   r=  r2   r  rk   r�   r<  r  r7   r8   r  r   r!  r"  r#  )r"   rf   rS   �val_sublist�key_sublistrm   r#   rY   r$  rZ   r%  r  s              @r(   r&  zSortedKeyList._check
  s%  �� �J	��:�:��?�"�?��t�{�{�#�s�4�;�;�'7�J�3�t�z�z�?�J�J�J�J�J��9�9��#L����#L� L�L�L�L�  �:�:�� ��C��L�1�C�"�3��7�+�w�s�|�;�;�;� 2� &� �Q��D�J�J��0���z�z�#��'�*�2�.�$�*�*�S�/�!�2D�D�D�D� 1�
 -0����T�Z�Z�,H�(��[��;�'�3�{�+;�;�;�;� #�K�� =�H�C���9�9�S�>�S�0�0�0� !>� -I� �S����-�.���{�{�3�'�4�:�:�c�?�2�+>�>�>�>� /�
 �Z�Z�1�_�F��I�T�[�[�I�I�I�I�
 �:�:��?�D��Q��D�K�K� 0�1� 4�5���4�;�;�s�+�,��4�4�4� 6� �{�{��y�y�D�K�K��N�2�2�2��4�;�;�'�4�<�<�#�d�k�k�:J�+J�J�J�J� !��T�[�[�!1�2�C��;�;�t�|�|�c�'9�:�D��3�t�{�{�3�'7�#8�8�8�8� 3� !����.�C� �A�X��N�E���D�K�K� 0�0�#�{�{�3�/�1�4�4�4����c�$�+�+�&6�6�#�{�{�3�/�4�;�;�u�3E�E�E�E�$(�K�K��$6����U�Q�Y�9O�$O�	�(�D�K�K��,<�<�<�<� /� ��*	����S�Z�Z�0��%����#��&�$�*�*�%��(�D�L�L�)��+�s�4�;�;�/�0��'�4�;�;�'��+�s�4�;�;�/�0��'�4�;�;�'��*�c�$�*�*�o�.��&�$�*�*�%��+�s�4�;�;�/�0��'�4�;�;�'��sI   �B:O
 �>AO
 �A(O
 �7AO
 � BO
 �C O
 �AO
 �<O
 �6O
 �O
 �
D=Tr(  r'  ))r�   r)  r*  r�   r9  r<   r?   r+  r#   rL   rG   r   rQ   rn   r9   rr   r!   ry   rt   r�   r[  rY  r   r   r,  rb  r]  rd  �
bisect_keyr_  r�   r�   r-  r�   r�   r.  r�   r	  r.   r  r&  r-   r,   r(   r@   r@   �  s  � ��0 !%�(� "#�J #�� #� �� ��

� �F�)�X$�N%�N �G�.�b.�b2�j9�x <H��!
�H @L� �QI�f �K�7�,8�* �F�#�B '��#�B "�J�(��+�\3� �H�R?�j5�. �H�5�(0�
 ��	P� �	P�Pr,   r@   )z...)1r�   �
__future__r   r!  r  r,  r   r   r   �	itertoolsr   r   r	   �mathr
   �operatorr   r   r   r   r   r   r   r   �textwrapr   �collections.abcr   r   �ImportError�collections�	functoolsr   r   r   r�   r   r�   �threadr   �dummy_threadr   �_thread�_dummy_threadr.   r0   r9  r@   �SortedListWithKeyr-   r,   r(   �<module>r�     s�   ���  &� 
� � 4� 4� ,� ,� � 6� 6� 6� �6�9� � ��
��%�%�+�$� !�,�%�
�<~�� ~�B2�
x�J� x�v "� ��iQ � 6�5�5�6�� � +�*�+�� � ,�+�,�s6   �B  �,B3 �:C � B0�/B0�3C� C�C�CPK     ���Y2��_  �_  6   sortedcontainers/__pycache__/sortedset.cpython-312.pyc�
    �A`gNP  �                   �   � d Z ddlmZ ddlmZmZmZmZmZm	Z	 ddl
mZ ddlmZmZ 	 ddlmZmZmZ  G d� d	ee�      Zy
# e$ r ddlmZmZmZ Y �w xY w)aE  Sorted Set
=============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted set implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedSet`

�    )�chain)�eq�ne�gt�ge�lt�le)�dedent�   )�
SortedList�recursive_repr)�
MutableSet�Sequence�Setc                   �  � e Zd ZdZd+d�Zed,d��       Zed� �       Zd� Z	d� Z
d� Zd	� Z eed
d�      Z eedd�      Z eedd�      Z eedd�      Z eedd�      Z eedd�      Z ee�      Zd� Zd� Zd� Zd� ZeZd� Zd� Z e Z!d� Z"d� Z#e#Z$d-d�Z%d� Z&d � Z'e'Z(d!� Z)e)Z*d"� Z+e+Z,e,Z-d#� Z.e.Z/d$� Z0e0Z1e1Z2d%� Z3e3Z4d&� Z5e5Z6e6Z7d'� Z8e8Z9e8Z:d(� Z; e<�       d)� �       Z=d*� Z>y).�	SortedSeta�  Sorted set is a sorted mutable set.

    Sorted set values are maintained in sorted order. The design of sorted set
    is simple: sorted set uses a set for set-operations and maintains a sorted
    list of values.

    Sorted set values must be hashable and comparable. The hash and total
    ordering of values must not change while they are stored in the sorted set.

    Mutable set methods:

    * :func:`SortedSet.__contains__`
    * :func:`SortedSet.__iter__`
    * :func:`SortedSet.__len__`
    * :func:`SortedSet.add`
    * :func:`SortedSet.discard`

    Sequence methods:

    * :func:`SortedSet.__getitem__`
    * :func:`SortedSet.__delitem__`
    * :func:`SortedSet.__reversed__`

    Methods for removing values:

    * :func:`SortedSet.clear`
    * :func:`SortedSet.pop`
    * :func:`SortedSet.remove`

    Set-operation methods:

    * :func:`SortedSet.difference`
    * :func:`SortedSet.difference_update`
    * :func:`SortedSet.intersection`
    * :func:`SortedSet.intersection_update`
    * :func:`SortedSet.symmetric_difference`
    * :func:`SortedSet.symmetric_difference_update`
    * :func:`SortedSet.union`
    * :func:`SortedSet.update`

    Methods for miscellany:

    * :func:`SortedSet.copy`
    * :func:`SortedSet.count`
    * :func:`SortedSet.__repr__`
    * :func:`SortedSet._check`

    Sorted list methods available:

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.index`
    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList._reset`

    Additional sorted list methods available, if key-function used:

    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Sorted set comparisons use subset and superset relations. Two sorted sets
    are equal if and only if every element of each sorted set is contained in
    the other (each is a subset of the other). A sorted set is less than
    another sorted set if and only if the first sorted set is a proper subset
    of the second sorted set (is a subset, but is not equal). A sorted set is
    greater than another sorted set if and only if the first sorted set is a
    proper superset of the second sorted set (is a superset, but is not equal).

    Nc                 �  � || _         t        | d�      st        �       | _        t	        | j                  |��      | _        | j                  }|j                  | _        |j                  | _        |j                  | _        | j
                  }|j                  | _	        |j                  | _
        |j                  | _        |j                  | _        |j                  | _        |j                  | _        |j                  | _        |�D|j                   | _        |j"                  | _        |j$                  | _        |j&                  | _        |�| j)                  |�       yy)a  Initialize sorted set instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted set.

        Optional `key` argument defines a callable that, like the `key`
        argument to Python's `sorted` function, extracts a comparison key from
        each value. The default, none, compares values directly.

        Runtime complexity: `O(n*log(n))`

        >>> ss = SortedSet([3, 1, 2, 5, 4])
        >>> ss
        SortedSet([1, 2, 3, 4, 5])
        >>> from operator import neg
        >>> ss = SortedSet([3, 1, 2, 5, 4], neg)
        >>> ss
        SortedSet([5, 4, 3, 2, 1], key=<built-in function neg>)

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)

        �_set��keyN)�_key�hasattr�setr   r   �_list�
isdisjoint�issubset�
issuperset�bisect_left�bisect�bisect_right�index�irange�islice�_reset�bisect_key_left�bisect_key_right�
bisect_key�
irange_key�_update)�self�iterabler   r   r   s        ��C:\Users\abuch\OneDrive\Bureaublad\School\Courses\Geometric Algorithms\Programming assigment\geometric_algorithms\plane_sweep\sortedcontainers\sortedset.py�__init__zSortedSet.__init__l   s  � �0 ��	� �t�V�$���D�I���	�	�s�3��
� �y�y���/�/���������/�/��� �
�
�� �,�,����l�l���!�.�.����[�[��
��l�l����l�l����l�l����?�#(�#8�#8�D� �$)�$:�$:�D�!�#�.�.�D�O�#�.�.�D�O����L�L��"�  �    c                 �b   � t         j                  | �      }||_        |j                  |��       |S )ztInitialize sorted set from existing set.

        Used internally by set operations that return a new set.

        r   )�object�__new__r   r-   )�cls�valuesr   �
sorted_sets       r,   �_fromsetzSortedSet._fromset�   s0   � � �^�^�C�(�
� �
�������$��r.   c                 �   � | j                   S )z�Function used to extract comparison key from values.

        Sorted set compares values directly when the key function is none.

        )r   �r*   s    r,   r   zSortedSet.key�   s   � � �y�y�r.   c                 �   � || j                   v S )aQ  Return true if `value` is an element of the sorted set.

        ``ss.__contains__(value)`` <==> ``value in ss``

        Runtime complexity: `O(1)`

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> 3 in ss
        True

        :param value: search for value in sorted set
        :return: true if `value` in sorted set

        �r   �r*   �values     r,   �__contains__zSortedSet.__contains__�   s   � � ��	�	�!�!r.   c                 �    � | j                   |   S )a�  Lookup value at `index` in sorted set.

        ``ss.__getitem__(index)`` <==> ``ss[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> ss[2]
        'c'
        >>> ss[-1]
        'e'
        >>> ss[2:5]
        ['c', 'd', 'e']

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        )r   )r*   r!   s     r,   �__getitem__zSortedSet.__getitem__�   s   � �, �z�z�%� � r.   c                 �   � | j                   }| j                  }t        |t        �      r||   }|j	                  |�       ||= y||   }|j                  |�       ||= y)a�  Remove value at `index` from sorted set.

        ``ss.__delitem__(index)`` <==> ``del ss[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> del ss[2]
        >>> ss
        SortedSet(['a', 'b', 'd', 'e'])
        >>> del ss[:2]
        >>> ss
        SortedSet(['d', 'e'])

        :param index: integer or slice for indexing
        :raises IndexError: if index out of range

        N)r   r   �
isinstance�slice�difference_update�remove)r*   r!   r   r   r3   r;   s         r,   �__delitem__zSortedSet.__delitem__�   s^   � �* �y�y���
�
���e�U�#��5�\�F��"�"�6�*� �%�L� �%�L�E��K�K����%�Lr.   c                 �   � � � fd�}� j                   }dj                  |�      |_         d}t        |j                  |||�      �      |_        |S )zMake comparator method.c                 �   �� t        |t        �      r �| j                  |j                  �      S t        |t        �      r �| j                  |�      S t        S )z&Compare method for sorted set and set.)r@   r   r   r   �NotImplemented)r*   �other�set_ops     �r,   �comparerz&SortedSet.__make_cmp.<locals>.comparer  sC   �� ��%��+��d�i�i����4�4��E�3�'��d�i�i��/�/�!�!r.   z__{0}__a3  Return true if and only if sorted set is {0} `other`.

        ``ss.__{1}__(other)`` <==> ``ss {2} other``

        Comparisons use subset and superset semantics as with sets.

        Runtime complexity: `O(n)`

        :param other: `other` set
        :return: true if sorted set is {0} `other`

        )�__name__�formatr
   �__doc__)rI   �symbol�docrJ   �set_op_name�doc_strs   `     r,   �
__make_cmpzSortedSet.__make_cmp  sN   �� �	"� �o�o��%�,�,�[�9����� "�'�.�.��k�6�"J�K����r.   z==zequal toz!=znot equal to�<za proper subset of�>za proper superset ofz<=za subset ofz>=za superset ofc                 �,   � t        | j                  �      S )z|Return the size of the sorted set.

        ``ss.__len__()`` <==> ``len(ss)``

        :return: size of sorted set

        )�lenr   r7   s    r,   �__len__zSortedSet.__len__2  s   � � �4�9�9�~�r.   c                 �,   � t        | j                  �      S )z�Return an iterator over the sorted set.

        ``ss.__iter__()`` <==> ``iter(ss)``

        Iterating the sorted set while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        )�iterr   r7   s    r,   �__iter__zSortedSet.__iter__=  s   � � �D�J�J��r.   c                 �,   � t        | j                  �      S )z�Return a reverse iterator over the sorted set.

        ``ss.__reversed__()`` <==> ``reversed(ss)``

        Iterating the sorted set while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        )�reversedr   r7   s    r,   �__reversed__zSortedSet.__reversed__I  s   � � ��
�
�#�#r.   c                 �~   � | j                   }||vr-|j                  |�       | j                  j                  |�       yy)a  Add `value` to sorted set.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet()
        >>> ss.add(3)
        >>> ss.add(1)
        >>> ss.add(2)
        >>> ss
        SortedSet([1, 2, 3])

        :param value: value to add to sorted set

        N)r   �addr   �r*   r;   r   s      r,   r_   zSortedSet.addU  s5   � � �y�y������H�H�U�O��J�J�N�N�5�!� r.   c                 �l   � | j                   j                  �        | j                  j                  �        y)zPRemove all values from sorted set.

        Runtime complexity: `O(n)`

        N)r   �clearr   r7   s    r,   rb   zSortedSet.clearl  s"   � � 	�	�	�����
�
���r.   c                 �b   � | j                  t        | j                  �      | j                  ��      S )zwReturn a shallow copy of the sorted set.

        Runtime complexity: `O(n)`

        :return: new sorted set

        r   )r5   r   r   r   r7   s    r,   �copyzSortedSet.copyv  s#   � � �}�}�S����^����}�;�;r.   c                 �&   � || j                   v rdS dS )a  Return number of occurrences of `value` in the sorted set.

        Runtime complexity: `O(1)`

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.count(3)
        1

        :param value: value to count in sorted set
        :return: count

        r   r   r9   r:   s     r,   �countzSortedSet.count�  s   � � �T�Y�Y�&�q�-�A�-r.   c                 �~   � | j                   }||v r-|j                  |�       | j                  j                  |�       yy)aq  Remove `value` from sorted set if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.discard(5)
        >>> ss.discard(0)
        >>> ss == set([1, 2, 3, 4])
        True

        :param value: `value` to discard from sorted set

        N�r   rC   r   r`   s      r,   �discardzSortedSet.discard�  s7   � �  �y�y���D�=��K�K����J�J���e�$� r.   c                 �r   � | j                   j                  |�      }| j                  j                  |�       |S )a  Remove and return value at `index` in sorted set.

        Raise :exc:`IndexError` if the sorted set is empty or index is out of
        range.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> ss.pop()
        'e'
        >>> ss.pop(2)
        'c'
        >>> ss
        SortedSet(['a', 'b', 'd'])

        :param int index: index of value (default -1)
        :return: value
        :raises IndexError: if index is out of range

        )r   �popr   rC   )r*   r!   r;   s      r,   rk   zSortedSet.pop�  s-   � �0 �
�
���u�%���	�	������r.   c                 �p   � | j                   j                  |�       | j                  j                  |�       y)a  Remove `value` from sorted set; `value` must be a member.

        If `value` is not a member, raise :exc:`KeyError`.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.remove(5)
        >>> ss == set([1, 2, 3, 4])
        True
        >>> ss.remove(0)
        Traceback (most recent call last):
          ...
        KeyError: 0

        :param value: `value` to remove from sorted set
        :raises KeyError: if `value` is not in sorted set

        Nrh   r:   s     r,   rC   zSortedSet.remove�  s(   � �( 	�	�	������
�
���%� r.   c                 �n   �  | j                   j                  |� }| j                  || j                  ��      S )a�  Return the difference of two or more sets as a new sorted set.

        The `difference` method also corresponds to operator ``-``.

        ``ss.__sub__(iterable)`` <==> ``ss - iterable``

        The difference is all values that are in this sorted set but not the
        other `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.difference([4, 5, 6, 7])
        SortedSet([1, 2, 3])

        :param iterables: iterable arguments
        :return: new sorted set

        r   )r   �
differencer5   r   )r*   �	iterables�diffs      r,   rn   zSortedSet.difference�  s1   � �$ $�t�y�y�#�#�Y�/���}�}�T�t�y�y�}�1�1r.   c                 �*  � | j                   }| j                  }t        t        |� �      }dt	        |�      z  t	        |�      kD  r4|j                  |�       |j                  �        |j                  |�       | S | j                  }|D ]
  } ||�       � | S )a�  Remove all values of `iterables` from this sorted set.

        The `difference_update` method also corresponds to operator ``-=``.

        ``ss.__isub__(iterable)`` <==> ``ss -= iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.difference_update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3])

        :param iterables: iterable arguments
        :return: itself

        �   )	r   r   r   r   rV   rB   rb   �update�_discard)r*   ro   r   r   r3   rt   r;   s          r,   rB   zSortedSet.difference_update�  s�   � �  �y�y���
�
���U�I�&�'����F��O�s�4�y�(��"�"�6�*��K�K�M��L�L���
 �� �}�}�H������  ��r.   c                 �n   �  | j                   j                  |� }| j                  || j                  ��      S )a�  Return the intersection of two or more sets as a new sorted set.

        The `intersection` method also corresponds to operator ``&``.

        ``ss.__and__(iterable)`` <==> ``ss & iterable``

        The intersection is all values that are in this sorted set and each of
        the other `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.intersection([4, 5, 6, 7])
        SortedSet([4, 5])

        :param iterables: iterable arguments
        :return: new sorted set

        r   )r   �intersectionr5   r   )r*   ro   �	intersects      r,   rv   zSortedSet.intersection  s1   � �$ +�D�I�I�*�*�I�6�	��}�}�Y�D�I�I�}�6�6r.   c                 �   � | j                   }| j                  } |j                  |�  |j                  �        |j	                  |�       | S )a�  Update the sorted set with the intersection of `iterables`.

        The `intersection_update` method also corresponds to operator ``&=``.

        ``ss.__iand__(iterable)`` <==> ``ss &= iterable``

        Keep only values found in itself and all `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.intersection_update([4, 5, 6, 7])
        >>> ss
        SortedSet([4, 5])

        :param iterables: iterable arguments
        :return: itself

        )r   r   �intersection_updaterb   rs   )r*   ro   r   r   s       r,   ry   zSortedSet.intersection_update1  s@   � �$ �y�y���
�
�� �� � �)�,��������T���r.   c                 �r   � | j                   j                  |�      }| j                  || j                  ��      S )a�  Return the symmetric difference with `other` as a new sorted set.

        The `symmetric_difference` method also corresponds to operator ``^``.

        ``ss.__xor__(other)`` <==> ``ss ^ other``

        The symmetric difference is all values tha are in exactly one of the
        sets.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.symmetric_difference([4, 5, 6, 7])
        SortedSet([1, 2, 3, 6, 7])

        :param other: `other` iterable
        :return: new sorted set

        r   )r   �symmetric_differencer5   r   )r*   rH   rp   s      r,   r{   zSortedSet.symmetric_differenceM  s/   � �$ �y�y�-�-�e�4���}�}�T�t�y�y�}�1�1r.   c                 �   � | j                   }| j                  }|j                  |�       |j                  �        |j	                  |�       | S )a  Update the sorted set with the symmetric difference with `other`.

        The `symmetric_difference_update` method also corresponds to operator
        ``^=``.

        ``ss.__ixor__(other)`` <==> ``ss ^= other``

        Keep only values found in exactly one of itself and `other`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.symmetric_difference_update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3, 6, 7])

        :param other: `other` iterable
        :return: itself

        )r   r   �symmetric_difference_updaterb   rs   )r*   rH   r   r   s       r,   r}   z%SortedSet.symmetric_difference_updatef  s>   � �& �y�y���
�
���(�(��/��������T���r.   c                 �b   � | j                  t        t        | �      g|��� | j                  ��      S )a�  Return new sorted set with values from itself and all `iterables`.

        The `union` method also corresponds to operator ``|``.

        ``ss.__or__(iterable)`` <==> ``ss | iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.union([4, 5, 6, 7])
        SortedSet([1, 2, 3, 4, 5, 6, 7])

        :param iterables: iterable arguments
        :return: new sorted set

        r   )�	__class__r   rY   r   )r*   ro   s     r,   �unionzSortedSet.union�  s)   � � �~�~�e�D��J�;��;����~�K�Kr.   c                 �B  � | j                   }| j                  }t        t        |� �      }dt	        |�      z  t	        |�      kD  r@| j                  }|j                  |�       |j                  �        |j                  |�       | S | j                  }|D ]
  } ||�       � | S )a�  Update the sorted set adding values from all `iterables`.

        The `update` method also corresponds to operator ``|=``.

        ``ss.__ior__(iterable)`` <==> ``ss |= iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3, 4, 5, 6, 7])

        :param iterables: iterable arguments
        :return: itself

        rr   )r   r   r   r   rV   rs   rb   �_add)r*   ro   r   r   r3   r�   r;   s          r,   rs   zSortedSet.update�  s�   � �  �y�y���
�
���U�I�&�'����F��O�s�4�y�(��J�J�E��K�K����K�K�M��L�L���
 �� �9�9�D����U��  ��r.   c                 �H   � t        | �      | j                  | j                  ffS )z�Support for pickle.

        The tricks played with exposing methods in :func:`SortedSet.__init__`
        confuse pickle so customize the reducer.

        )�typer   r   r7   s    r,   �
__reduce__zSortedSet.__reduce__�  s    � � �T�
�T�Y�Y��	�	�2�3�3r.   c                 �   � | j                   }|�dndj                  |�      }t        | �      j                  }dj                  |t	        | �      |�      S )z�Return string representation of sorted set.

        ``ss.__repr__()`` <==> ``repr(ss)``

        :return: string representation

        � z, key={0!r}z{0}({1!r}{2}))r   rL   r�   rK   �list)r*   r   r   �	type_names       r,   �__repr__zSortedSet.__repr__�  sK   � � �y�y���L�b�m�&:�&:�4�&@����J�'�'�	��%�%�i��d��S�A�Ar.   c                 �   �� | j                   �| j                  }|j                  �        t        ��      t        |�      k(  sJ �t	        �fd�|D �       �      sJ �y)zMCheck invariants of sorted set.

        Runtime complexity: `O(n)`

        c              3   �&   �K  � | ]  }|�v �� �
 y �w�N� )�.0r;   r   s     �r,   �	<genexpr>z#SortedSet._check.<locals>.<genexpr>�  s   �� �� �4�e�U�5�D�=�e�s   �N)r   r   �_checkrV   �all)r*   r   r   s     @r,   r�   zSortedSet._check�  sJ   �� � �y�y���
�
�������4�y�C��J�&�&�&��4�e�4�4�4�4r.   )NNr�   )�����)?rK   �
__module__�__qualname__rM   r-   �classmethodr5   �propertyr   r<   r>   rD   �_SortedSet__make_cmpr   �__eq__r   �__ne__r   �__lt__r   �__gt__r	   �__le__r   �__ge__�staticmethodrW   rZ   r]   r_   r�   rb   rd   �__copy__rf   ri   rt   rk   rC   rn   �__sub__rB   �__isub__rv   �__and__�__rand__ry   �__iand__r{   �__xor__�__rxor__r}   �__ixor__r�   �__or__�__ror__rs   �__ior__r)   r�   r   r�   r�   r�   r.   r,   r   r   $   s�  � �F�N<#�~ �	� �	� �� ��"�$!�2�@�8 ��D�*�-�F���D�.�1�F���C�!5�6�F���C�!7�8�F���D�-�0�F���D�/�2�F��j�)�J��	 �	$�"�( �D��<� �H�.� %�* �H��:!�02�* �G��: !�H�7�* �G��H��2 #�H�2�* #�G��H��4 +�H�L�" �F��G��< �G��G�4� ��B� �B�
5r.   r   N)rM   �	itertoolsr   �operatorr   r   r   r   r   r	   �textwrapr
   �
sortedlistr   r   �collections.abcr   r   r   �ImportError�collectionsr   r�   r.   r,   �<module>r�      sM   ��� � +� +� � 2�6�9�9�y
5�
�H� y
5�� � 6�5�5�6�s   �
? �A�APK     ˀ�Y��Ea:  :     sortedcontainers/LICENSECopyright 2014-2019 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
PK     ˀ�Y���k�[  �[     sortedcontainers/sorteddict.py"""Sorted Dict
==============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted dict implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedDict`
* :class:`SortedKeysView`
* :class:`SortedItemsView`
* :class:`SortedValuesView`

"""

import sys
import warnings

from itertools import chain

from .sortedlist import SortedList, recursive_repr
from .sortedset import SortedSet

###############################################################################
# BEGIN Python 2/3 Shims
###############################################################################

try:
    from collections.abc import (
        ItemsView, KeysView, Mapping, ValuesView, Sequence
    )
except ImportError:
    from collections import ItemsView, KeysView, Mapping, ValuesView, Sequence

###############################################################################
# END Python 2/3 Shims
###############################################################################


class SortedDict(dict):
    """Sorted dict is a sorted mutable mapping.

    Sorted dict keys are maintained in sorted order. The design of sorted dict
    is simple: sorted dict inherits from dict to store items and maintains a
    sorted list of keys.

    Sorted dict keys must be hashable and comparable. The hash and total
    ordering of keys must not change while they are stored in the sorted dict.

    Mutable mapping methods:

    * :func:`SortedDict.__getitem__` (inherited from dict)
    * :func:`SortedDict.__setitem__`
    * :func:`SortedDict.__delitem__`
    * :func:`SortedDict.__iter__`
    * :func:`SortedDict.__len__` (inherited from dict)

    Methods for adding items:

    * :func:`SortedDict.setdefault`
    * :func:`SortedDict.update`

    Methods for removing items:

    * :func:`SortedDict.clear`
    * :func:`SortedDict.pop`
    * :func:`SortedDict.popitem`

    Methods for looking up items:

    * :func:`SortedDict.__contains__` (inherited from dict)
    * :func:`SortedDict.get` (inherited from dict)
    * :func:`SortedDict.peekitem`

    Methods for views:

    * :func:`SortedDict.keys`
    * :func:`SortedDict.items`
    * :func:`SortedDict.values`

    Methods for miscellany:

    * :func:`SortedDict.copy`
    * :func:`SortedDict.fromkeys`
    * :func:`SortedDict.__reversed__`
    * :func:`SortedDict.__eq__` (inherited from dict)
    * :func:`SortedDict.__ne__` (inherited from dict)
    * :func:`SortedDict.__repr__`
    * :func:`SortedDict._check`

    Sorted list methods available (applies to keys):

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.count`
    * :func:`SortedList.index`
    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList._reset`

    Additional sorted list methods available, if key-function used:

    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Sorted dicts may only be compared for equality and inequality.

    """
    def __init__(self, *args, **kwargs):
        """Initialize sorted dict instance.

        Optional key-function argument defines a callable that, like the `key`
        argument to the built-in `sorted` function, extracts a comparison key
        from each dictionary key. If no function is specified, the default
        compares the dictionary keys directly. The key-function argument must
        be provided as a positional argument and must come before all other
        arguments.

        Optional iterable argument provides an initial sequence of pairs to
        initialize the sorted dict. Each pair in the sequence defines the key
        and corresponding value. If a key is seen more than once, the last
        value associated with it is stored in the new sorted dict.

        Optional mapping argument provides an initial mapping of items to
        initialize the sorted dict.

        If keyword arguments are given, the keywords themselves, with their
        associated values, are added as items to the dictionary. If a key is
        specified both in the positional argument and as a keyword argument,
        the value associated with the keyword is stored in the
        sorted dict.

        Sorted dict keys must be hashable, per the requirement for Python's
        dictionaries. Keys (or the result of the key-function) must also be
        comparable, per the requirement for sorted lists.

        >>> d = {'alpha': 1, 'beta': 2}
        >>> SortedDict([('alpha', 1), ('beta', 2)]) == d
        True
        >>> SortedDict({'alpha': 1, 'beta': 2}) == d
        True
        >>> SortedDict(alpha=1, beta=2) == d
        True

        """
        if args and (args[0] is None or callable(args[0])):
            _key = self._key = args[0]
            args = args[1:]
        else:
            _key = self._key = None

        self._list = SortedList(key=_key)

        # Reaching through ``self._list`` repeatedly adds unnecessary overhead
        # so cache references to sorted list methods.

        _list = self._list
        self._list_add = _list.add
        self._list_clear = _list.clear
        self._list_iter = _list.__iter__
        self._list_reversed = _list.__reversed__
        self._list_pop = _list.pop
        self._list_remove = _list.remove
        self._list_update = _list.update

        # Expose some sorted list methods publicly.

        self.bisect_left = _list.bisect_left
        self.bisect = _list.bisect_right
        self.bisect_right = _list.bisect_right
        self.index = _list.index
        self.irange = _list.irange
        self.islice = _list.islice
        self._reset = _list._reset

        if _key is not None:
            self.bisect_key_left = _list.bisect_key_left
            self.bisect_key_right = _list.bisect_key_right
            self.bisect_key = _list.bisect_key
            self.irange_key = _list.irange_key

        self._update(*args, **kwargs)


    @property
    def key(self):
        """Function used to extract comparison key from keys.

        Sorted dict compares keys directly when the key function is none.

        """
        return self._key


    @property
    def iloc(self):
        """Cached reference of sorted keys view.

        Deprecated in version 2 of Sorted Containers. Use
        :func:`SortedDict.keys` instead.

        """
        # pylint: disable=attribute-defined-outside-init
        try:
            return self._iloc
        except AttributeError:
            warnings.warn(
                'sorted_dict.iloc is deprecated.'
                ' Use SortedDict.keys() instead.',
                DeprecationWarning,
                stacklevel=2,
            )
            _iloc = self._iloc = SortedKeysView(self)
            return _iloc


    def clear(self):

        """Remove all items from sorted dict.

        Runtime complexity: `O(n)`

        """
        dict.clear(self)
        self._list_clear()


    def __delitem__(self, key):
        """Remove item from sorted dict identified by `key`.

        ``sd.__delitem__(key)`` <==> ``del sd[key]``

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> del sd['b']
        >>> sd
        SortedDict({'a': 1, 'c': 3})
        >>> del sd['z']
        Traceback (most recent call last):
          ...
        KeyError: 'z'

        :param key: `key` for item lookup
        :raises KeyError: if key not found

        """
        dict.__delitem__(self, key)
        self._list_remove(key)


    def __iter__(self):
        """Return an iterator over the keys of the sorted dict.

        ``sd.__iter__()`` <==> ``iter(sd)``

        Iterating the sorted dict while adding or deleting items may raise a
        :exc:`RuntimeError` or fail to iterate over all keys.

        """
        return self._list_iter()


    def __reversed__(self):
        """Return a reverse iterator over the keys of the sorted dict.

        ``sd.__reversed__()`` <==> ``reversed(sd)``

        Iterating the sorted dict while adding or deleting items may raise a
        :exc:`RuntimeError` or fail to iterate over all keys.

        """
        return self._list_reversed()


    def __setitem__(self, key, value):
        """Store item in sorted dict with `key` and corresponding `value`.

        ``sd.__setitem__(key, value)`` <==> ``sd[key] = value``

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict()
        >>> sd['c'] = 3
        >>> sd['a'] = 1
        >>> sd['b'] = 2
        >>> sd
        SortedDict({'a': 1, 'b': 2, 'c': 3})

        :param key: key for item
        :param value: value for item

        """
        if key not in self:
            self._list_add(key)
        dict.__setitem__(self, key, value)

    _setitem = __setitem__


    def __or__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        items = chain(self.items(), other.items())
        return self.__class__(self._key, items)


    def __ror__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        items = chain(other.items(), self.items())
        return self.__class__(self._key, items)


    def __ior__(self, other):
        self._update(other)
        return self


    def copy(self):
        """Return a shallow copy of the sorted dict.

        Runtime complexity: `O(n)`

        :return: new sorted dict

        """
        return self.__class__(self._key, self.items())

    __copy__ = copy


    @classmethod
    def fromkeys(cls, iterable, value=None):
        """Return a new sorted dict initailized from `iterable` and `value`.

        Items in the sorted dict have keys from `iterable` and values equal to
        `value`.

        Runtime complexity: `O(n*log(n))`

        :return: new sorted dict

        """
        return cls((key, value) for key in iterable)


    def keys(self):
        """Return new sorted keys view of the sorted dict's keys.

        See :class:`SortedKeysView` for details.

        :return: new sorted keys view

        """
        return SortedKeysView(self)


    def items(self):
        """Return new sorted items view of the sorted dict's items.

        See :class:`SortedItemsView` for details.

        :return: new sorted items view

        """
        return SortedItemsView(self)


    def values(self):
        """Return new sorted values view of the sorted dict's values.

        See :class:`SortedValuesView` for details.

        :return: new sorted values view

        """
        return SortedValuesView(self)


    if sys.hexversion < 0x03000000:
        def __make_raise_attributeerror(original, alternate):
            # pylint: disable=no-self-argument
            message = (
                'SortedDict.{original}() is not implemented.'
                ' Use SortedDict.{alternate}() instead.'
            ).format(original=original, alternate=alternate)
            def method(self):
                # pylint: disable=missing-docstring,unused-argument
                raise AttributeError(message)
            method.__name__ = original  # pylint: disable=non-str-assignment-to-dunder-name
            method.__doc__ = message
            return property(method)

        iteritems = __make_raise_attributeerror('iteritems', 'items')
        iterkeys = __make_raise_attributeerror('iterkeys', 'keys')
        itervalues = __make_raise_attributeerror('itervalues', 'values')
        viewitems = __make_raise_attributeerror('viewitems', 'items')
        viewkeys = __make_raise_attributeerror('viewkeys', 'keys')
        viewvalues = __make_raise_attributeerror('viewvalues', 'values')


    class _NotGiven(object):
        # pylint: disable=too-few-public-methods
        def __repr__(self):
            return '<not-given>'

    __not_given = _NotGiven()

    def pop(self, key, default=__not_given):
        """Remove and return value for item identified by `key`.

        If the `key` is not found then return `default` if given. If `default`
        is not given then raise :exc:`KeyError`.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> sd.pop('c')
        3
        >>> sd.pop('z', 26)
        26
        >>> sd.pop('y')
        Traceback (most recent call last):
          ...
        KeyError: 'y'

        :param key: `key` for item
        :param default: `default` value if key not found (optional)
        :return: value for item
        :raises KeyError: if `key` not found and `default` not given

        """
        if key in self:
            self._list_remove(key)
            return dict.pop(self, key)
        else:
            if default is self.__not_given:
                raise KeyError(key)
            return default


    def popitem(self, index=-1):
        """Remove and return ``(key, value)`` pair at `index` from sorted dict.

        Optional argument `index` defaults to -1, the last item in the sorted
        dict. Specify ``index=0`` for the first item in the sorted dict.

        If the sorted dict is empty, raises :exc:`KeyError`.

        If the `index` is out of range, raises :exc:`IndexError`.

        Runtime complexity: `O(log(n))`

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> sd.popitem()
        ('c', 3)
        >>> sd.popitem(0)
        ('a', 1)
        >>> sd.popitem(100)
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param int index: `index` of item (default -1)
        :return: key and value pair
        :raises KeyError: if sorted dict is empty
        :raises IndexError: if `index` out of range

        """
        if not self:
            raise KeyError('popitem(): dictionary is empty')

        key = self._list_pop(index)
        value = dict.pop(self, key)
        return (key, value)


    def peekitem(self, index=-1):
        """Return ``(key, value)`` pair at `index` in sorted dict.

        Optional argument `index` defaults to -1, the last item in the sorted
        dict. Specify ``index=0`` for the first item in the sorted dict.

        Unlike :func:`SortedDict.popitem`, the sorted dict is not modified.

        If the `index` is out of range, raises :exc:`IndexError`.

        Runtime complexity: `O(log(n))`

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> sd.peekitem()
        ('c', 3)
        >>> sd.peekitem(0)
        ('a', 1)
        >>> sd.peekitem(100)
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param int index: index of item (default -1)
        :return: key and value pair
        :raises IndexError: if `index` out of range

        """
        key = self._list[index]
        return key, self[key]


    def setdefault(self, key, default=None):
        """Return value for item identified by `key` in sorted dict.

        If `key` is in the sorted dict then return its value. If `key` is not
        in the sorted dict then insert `key` with value `default` and return
        `default`.

        Optional argument `default` defaults to none.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict()
        >>> sd.setdefault('a', 1)
        1
        >>> sd.setdefault('a', 10)
        1
        >>> sd
        SortedDict({'a': 1})

        :param key: key for item
        :param default: value for item (default None)
        :return: value for item identified by `key`

        """
        if key in self:
            return self[key]
        dict.__setitem__(self, key, default)
        self._list_add(key)
        return default


    def update(self, *args, **kwargs):
        """Update sorted dict with items from `args` and `kwargs`.

        Overwrites existing items.

        Optional arguments `args` and `kwargs` may be a mapping, an iterable of
        pairs or keyword arguments. See :func:`SortedDict.__init__` for
        details.

        :param args: mapping or iterable of pairs
        :param kwargs: keyword arguments mapping

        """
        if not self:
            dict.update(self, *args, **kwargs)
            self._list_update(dict.__iter__(self))
            return

        if not kwargs and len(args) == 1 and isinstance(args[0], dict):
            pairs = args[0]
        else:
            pairs = dict(*args, **kwargs)

        if (10 * len(pairs)) > len(self):
            dict.update(self, pairs)
            self._list_clear()
            self._list_update(dict.__iter__(self))
        else:
            for key in pairs:
                self._setitem(key, pairs[key])

    _update = update


    def __reduce__(self):
        """Support for pickle.

        The tricks played with caching references in
        :func:`SortedDict.__init__` confuse pickle so customize the reducer.

        """
        items = dict.copy(self)
        return (type(self), (self._key, items))


    @recursive_repr()
    def __repr__(self):
        """Return string representation of sorted dict.

        ``sd.__repr__()`` <==> ``repr(sd)``

        :return: string representation

        """
        _key = self._key
        type_name = type(self).__name__
        key_arg = '' if _key is None else '{0!r}, '.format(_key)
        item_format = '{0!r}: {1!r}'.format
        items = ', '.join(item_format(key, self[key]) for key in self._list)
        return '{0}({1}{{{2}}})'.format(type_name, key_arg, items)


    def _check(self):
        """Check invariants of sorted dict.

        Runtime complexity: `O(n)`

        """
        _list = self._list
        _list._check()
        assert len(self) == len(_list)
        assert all(key in self for key in _list)


def _view_delitem(self, index):
    """Remove item at `index` from sorted dict.

    ``view.__delitem__(index)`` <==> ``del view[index]``

    Supports slicing.

    Runtime complexity: `O(log(n))` -- approximate.

    >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
    >>> view = sd.keys()
    >>> del view[0]
    >>> sd
    SortedDict({'b': 2, 'c': 3})
    >>> del view[-1]
    >>> sd
    SortedDict({'b': 2})
    >>> del view[:]
    >>> sd
    SortedDict({})

    :param index: integer or slice for indexing
    :raises IndexError: if index out of range

    """
    _mapping = self._mapping
    _list = _mapping._list
    dict_delitem = dict.__delitem__
    if isinstance(index, slice):
        keys = _list[index]
        del _list[index]
        for key in keys:
            dict_delitem(_mapping, key)
    else:
        key = _list.pop(index)
        dict_delitem(_mapping, key)


class SortedKeysView(KeysView, Sequence):
    """Sorted keys view is a dynamic view of the sorted dict's keys.

    When the sorted dict's keys change, the view reflects those changes.

    The keys view implements the set and sequence abstract base classes.

    """
    __slots__ = ()


    @classmethod
    def _from_iterable(cls, it):
        return SortedSet(it)


    def __getitem__(self, index):
        """Lookup key at `index` in sorted keys views.

        ``skv.__getitem__(index)`` <==> ``skv[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> skv = sd.keys()
        >>> skv[0]
        'a'
        >>> skv[-1]
        'c'
        >>> skv[:]
        ['a', 'b', 'c']
        >>> skv[100]
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param index: integer or slice for indexing
        :return: key or list of keys
        :raises IndexError: if index out of range

        """
        return self._mapping._list[index]


    __delitem__ = _view_delitem


class SortedItemsView(ItemsView, Sequence):
    """Sorted items view is a dynamic view of the sorted dict's items.

    When the sorted dict's items change, the view reflects those changes.

    The items view implements the set and sequence abstract base classes.

    """
    __slots__ = ()


    @classmethod
    def _from_iterable(cls, it):
        return SortedSet(it)


    def __getitem__(self, index):
        """Lookup item at `index` in sorted items view.

        ``siv.__getitem__(index)`` <==> ``siv[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> siv = sd.items()
        >>> siv[0]
        ('a', 1)
        >>> siv[-1]
        ('c', 3)
        >>> siv[:]
        [('a', 1), ('b', 2), ('c', 3)]
        >>> siv[100]
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param index: integer or slice for indexing
        :return: item or list of items
        :raises IndexError: if index out of range

        """
        _mapping = self._mapping
        _mapping_list = _mapping._list

        if isinstance(index, slice):
            keys = _mapping_list[index]
            return [(key, _mapping[key]) for key in keys]

        key = _mapping_list[index]
        return key, _mapping[key]


    __delitem__ = _view_delitem


class SortedValuesView(ValuesView, Sequence):
    """Sorted values view is a dynamic view of the sorted dict's values.

    When the sorted dict's values change, the view reflects those changes.

    The values view implements the sequence abstract base class.

    """
    __slots__ = ()


    def __getitem__(self, index):
        """Lookup value at `index` in sorted values view.

        ``siv.__getitem__(index)`` <==> ``siv[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> svv = sd.values()
        >>> svv[0]
        1
        >>> svv[-1]
        3
        >>> svv[:]
        [1, 2, 3]
        >>> svv[100]
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        """
        _mapping = self._mapping
        _mapping_list = _mapping._list

        if isinstance(index, slice):
            keys = _mapping_list[index]
            return [_mapping[key] for key in keys]

        key = _mapping_list[index]
        return _mapping[key]


    __delitem__ = _view_delitem
PK     ˀ�Y�gXi�4 �4    sortedcontainers/sortedlist.py"""Sorted List
==============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted list implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedList`
* :class:`SortedKeyList`

"""
# pylint: disable=too-many-lines
from __future__ import print_function

import sys
import traceback

from bisect import bisect_left, bisect_right, insort
from itertools import chain, repeat, starmap
from math import log
from operator import add, eq, ne, gt, ge, lt, le, iadd
from textwrap import dedent

###############################################################################
# BEGIN Python 2/3 Shims
###############################################################################

try:
    from collections.abc import Sequence, MutableSequence
except ImportError:
    from collections import Sequence, MutableSequence

from functools import wraps
from sys import hexversion

if hexversion < 0x03000000:
    from itertools import imap as map  # pylint: disable=redefined-builtin
    from itertools import izip as zip  # pylint: disable=redefined-builtin
    try:
        from thread import get_ident
    except ImportError:
        from dummy_thread import get_ident
else:
    from functools import reduce
    try:
        from _thread import get_ident
    except ImportError:
        from _dummy_thread import get_ident


def recursive_repr(fillvalue='...'):
    "Decorator to make a repr function return fillvalue for a recursive call."
    # pylint: disable=missing-docstring
    # Copied from reprlib in Python 3
    # https://hg.python.org/cpython/file/3.6/Lib/reprlib.py

    def decorating_function(user_function):
        repr_running = set()

        @wraps(user_function)
        def wrapper(self):
            key = id(self), get_ident()
            if key in repr_running:
                return fillvalue
            repr_running.add(key)
            try:
                result = user_function(self)
            finally:
                repr_running.discard(key)
            return result

        return wrapper

    return decorating_function

###############################################################################
# END Python 2/3 Shims
###############################################################################


class SortedList(MutableSequence):
    """Sorted list is a sorted mutable sequence.

    Sorted list values are maintained in sorted order.

    Sorted list values must be comparable. The total ordering of values must
    not change while they are stored in the sorted list.

    Methods for adding values:

    * :func:`SortedList.add`
    * :func:`SortedList.update`
    * :func:`SortedList.__add__`
    * :func:`SortedList.__iadd__`
    * :func:`SortedList.__mul__`
    * :func:`SortedList.__imul__`

    Methods for removing values:

    * :func:`SortedList.clear`
    * :func:`SortedList.discard`
    * :func:`SortedList.remove`
    * :func:`SortedList.pop`
    * :func:`SortedList.__delitem__`

    Methods for looking up values:

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.count`
    * :func:`SortedList.index`
    * :func:`SortedList.__contains__`
    * :func:`SortedList.__getitem__`

    Methods for iterating values:

    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList.__iter__`
    * :func:`SortedList.__reversed__`

    Methods for miscellany:

    * :func:`SortedList.copy`
    * :func:`SortedList.__len__`
    * :func:`SortedList.__repr__`
    * :func:`SortedList._check`
    * :func:`SortedList._reset`

    Sorted lists use lexicographical ordering semantics when compared to other
    sequences.

    Some methods of mutable sequences are not supported and will raise
    not-implemented error.

    """
    DEFAULT_LOAD_FACTOR = 1000


    def __init__(self, iterable=None, key=None):
        """Initialize sorted list instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted list.

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList()
        >>> sl
        SortedList([])
        >>> sl = SortedList([3, 1, 2, 5, 4])
        >>> sl
        SortedList([1, 2, 3, 4, 5])

        :param iterable: initial values (optional)

        """
        assert key is None
        self._len = 0
        self._load = self.DEFAULT_LOAD_FACTOR
        self._lists = []
        self._maxes = []
        self._index = []
        self._offset = 0

        if iterable is not None:
            self._update(iterable)


    def __new__(cls, iterable=None, key=None):
        """Create new sorted list or sorted-key list instance.

        Optional `key`-function argument will return an instance of subtype
        :class:`SortedKeyList`.

        >>> sl = SortedList()
        >>> isinstance(sl, SortedList)
        True
        >>> sl = SortedList(key=lambda x: -x)
        >>> isinstance(sl, SortedList)
        True
        >>> isinstance(sl, SortedKeyList)
        True

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)
        :return: sorted list or sorted-key list instance

        """
        # pylint: disable=unused-argument
        if key is None:
            return object.__new__(cls)
        else:
            if cls is SortedList:
                return object.__new__(SortedKeyList)
            else:
                raise TypeError('inherit SortedKeyList for key argument')


    @property
    def key(self):  # pylint: disable=useless-return
        """Function used to extract comparison key from values.

        Sorted list compares values directly so the key function is none.

        """
        return None


    def _reset(self, load):
        """Reset sorted list load factor.

        The `load` specifies the load-factor of the list. The default load
        factor of 1000 works well for lists from tens to tens-of-millions of
        values. Good practice is to use a value that is the cube root of the
        list size. With billions of elements, the best load factor depends on
        your usage. It's best to leave the load factor at the default until you
        start benchmarking.

        See :doc:`implementation` and :doc:`performance-scale` for more
        information.

        Runtime complexity: `O(n)`

        :param int load: load-factor for sorted list sublists

        """
        values = reduce(iadd, self._lists, [])
        self._clear()
        self._load = load
        self._update(values)


    def clear(self):
        """Remove all values from sorted list.

        Runtime complexity: `O(n)`

        """
        self._len = 0
        del self._lists[:]
        del self._maxes[:]
        del self._index[:]
        self._offset = 0

    _clear = clear


    def add(self, value):
        """Add `value` to sorted list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList()
        >>> sl.add(3)
        >>> sl.add(1)
        >>> sl.add(2)
        >>> sl
        SortedList([1, 2, 3])

        :param value: value to add to sorted list

        """
        _lists = self._lists
        _maxes = self._maxes

        if _maxes:
            pos = bisect_right(_maxes, value)

            if pos == len(_maxes):
                pos -= 1
                _lists[pos].append(value)
                _maxes[pos] = value
            else:
                insort(_lists[pos], value)

            self._expand(pos)
        else:
            _lists.append([value])
            _maxes.append(value)

        self._len += 1


    def _expand(self, pos):
        """Split sublists with length greater than double the load-factor.

        Updates the index when the sublist length is less than double the load
        level. This requires incrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        """
        _load = self._load
        _lists = self._lists
        _index = self._index

        if len(_lists[pos]) > (_load << 1):
            _maxes = self._maxes

            _lists_pos = _lists[pos]
            half = _lists_pos[_load:]
            del _lists_pos[_load:]
            _maxes[pos] = _lists_pos[-1]

            _lists.insert(pos + 1, half)
            _maxes.insert(pos + 1, half[-1])

            del _index[:]
        else:
            if _index:
                child = self._offset + pos
                while child:
                    _index[child] += 1
                    child = (child - 1) >> 1
                _index[0] += 1


    def update(self, iterable):
        """Update sorted list by adding all values from `iterable`.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> sl = SortedList()
        >>> sl.update([3, 1, 2])
        >>> sl
        SortedList([1, 2, 3])

        :param iterable: iterable of values to add

        """
        _lists = self._lists
        _maxes = self._maxes
        values = sorted(iterable)

        if _maxes:
            if len(values) * 4 >= self._len:
                _lists.append(values)
                values = reduce(iadd, _lists, [])
                values.sort()
                self._clear()
            else:
                _add = self.add
                for val in values:
                    _add(val)
                return

        _load = self._load
        _lists.extend(values[pos:(pos + _load)]
                      for pos in range(0, len(values), _load))
        _maxes.extend(sublist[-1] for sublist in _lists)
        self._len = len(values)
        del self._index[:]

    _update = update


    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list.

        ``sl.__contains__(value)`` <==> ``value in sl``

        Runtime complexity: `O(log(n))`

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> 3 in sl
        True

        :param value: search for value in sorted list
        :return: true if `value` in sorted list

        """
        _maxes = self._maxes

        if not _maxes:
            return False

        pos = bisect_left(_maxes, value)

        if pos == len(_maxes):
            return False

        _lists = self._lists
        idx = bisect_left(_lists[pos], value)

        return _lists[pos][idx] == value


    def discard(self, value):
        """Remove `value` from sorted list if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> sl.discard(5)
        >>> sl.discard(0)
        >>> sl == [1, 2, 3, 4]
        True

        :param value: `value` to discard from sorted list

        """
        _maxes = self._maxes

        if not _maxes:
            return

        pos = bisect_left(_maxes, value)

        if pos == len(_maxes):
            return

        _lists = self._lists
        idx = bisect_left(_lists[pos], value)

        if _lists[pos][idx] == value:
            self._delete(pos, idx)


    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member.

        If `value` is not a member, raise ValueError.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> sl.remove(5)
        >>> sl == [1, 2, 3, 4]
        True
        >>> sl.remove(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 not in list

        :param value: `value` to remove from sorted list
        :raises ValueError: if `value` is not in sorted list

        """
        _maxes = self._maxes

        if not _maxes:
            raise ValueError('{0!r} not in list'.format(value))

        pos = bisect_left(_maxes, value)

        if pos == len(_maxes):
            raise ValueError('{0!r} not in list'.format(value))

        _lists = self._lists
        idx = bisect_left(_lists[pos], value)

        if _lists[pos][idx] == value:
            self._delete(pos, idx)
        else:
            raise ValueError('{0!r} not in list'.format(value))


    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`.

        Combines lists that are less than half the load level.

        Updates the index when the sublist length is more than half the load
        level. This requires decrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        :param int pos: lists index
        :param int idx: sublist index

        """
        _lists = self._lists
        _maxes = self._maxes
        _index = self._index

        _lists_pos = _lists[pos]

        del _lists_pos[idx]
        self._len -= 1

        len_lists_pos = len(_lists_pos)

        if len_lists_pos > (self._load >> 1):
            _maxes[pos] = _lists_pos[-1]

            if _index:
                child = self._offset + pos
                while child > 0:
                    _index[child] -= 1
                    child = (child - 1) >> 1
                _index[0] -= 1
        elif len(_lists) > 1:
            if not pos:
                pos += 1

            prev = pos - 1
            _lists[prev].extend(_lists[pos])
            _maxes[prev] = _lists[prev][-1]

            del _lists[pos]
            del _maxes[pos]
            del _index[:]

            self._expand(prev)
        elif len_lists_pos:
            _maxes[pos] = _lists_pos[-1]
        else:
            del _lists[pos]
            del _maxes[pos]
            del _index[:]


    def _loc(self, pos, idx):
        """Convert an index pair (lists index, sublist index) into a single
        index number that corresponds to the position of the value in the
        sorted list.

        Many queries require the index be built. Details of the index are
        described in ``SortedList._build_index``.

        Indexing requires traversing the tree from a leaf node to the root. The
        parent of each node is easily computable at ``(pos - 1) // 2``.

        Left-child nodes are always at odd indices and right-child nodes are
        always at even indices.

        When traversing up from a right-child node, increment the total by the
        left-child node.

        The final index is the sum from traversal and the index in the sublist.

        For example, using the index from ``SortedList._build_index``::

            _index = 14 5 9 3 2 4 5
            _offset = 3

        Tree::

                 14
              5      9
            3   2  4   5

        Converting an index pair (2, 3) into a single index involves iterating
        like so:

        1. Starting at the leaf node: offset + alpha = 3 + 2 = 5. We identify
           the node as a left-child node. At such nodes, we simply traverse to
           the parent.

        2. At node 9, position 2, we recognize the node as a right-child node
           and accumulate the left-child in our total. Total is now 5 and we
           traverse to the parent at position 0.

        3. Iteration ends at the root.

        The index is then the sum of the total and sublist index: 5 + 3 = 8.

        :param int pos: lists index
        :param int idx: sublist index
        :return: index in sorted list

        """
        if not pos:
            return idx

        _index = self._index

        if not _index:
            self._build_index()

        total = 0

        # Increment pos to point in the index to len(self._lists[pos]).

        pos += self._offset

        # Iterate until reaching the root of the index tree at pos = 0.

        while pos:

            # Right-child nodes are at odd indices. At such indices
            # account the total below the left child node.

            if not pos & 1:
                total += _index[pos - 1]

            # Advance pos to the parent node.

            pos = (pos - 1) >> 1

        return total + idx


    def _pos(self, idx):
        """Convert an index into an index pair (lists index, sublist index)
        that can be used to access the corresponding lists position.

        Many queries require the index be built. Details of the index are
        described in ``SortedList._build_index``.

        Indexing requires traversing the tree to a leaf node. Each node has two
        children which are easily computable. Given an index, pos, the
        left-child is at ``pos * 2 + 1`` and the right-child is at ``pos * 2 +
        2``.

        When the index is less than the left-child, traversal moves to the
        left sub-tree. Otherwise, the index is decremented by the left-child
        and traversal moves to the right sub-tree.

        At a child node, the indexing pair is computed from the relative
        position of the child node as compared with the offset and the remaining
        index.

        For example, using the index from ``SortedList._build_index``::

            _index = 14 5 9 3 2 4 5
            _offset = 3

        Tree::

                 14
              5      9
            3   2  4   5

        Indexing position 8 involves iterating like so:

        1. Starting at the root, position 0, 8 is compared with the left-child
           node (5) which it is greater than. When greater the index is
           decremented and the position is updated to the right child node.

        2. At node 9 with index 3, we again compare the index to the left-child
           node with value 4. Because the index is the less than the left-child
           node, we simply traverse to the left.

        3. At node 4 with index 3, we recognize that we are at a leaf node and
           stop iterating.

        4. To compute the sublist index, we subtract the offset from the index
           of the leaf node: 5 - 3 = 2. To compute the index in the sublist, we
           simply use the index remaining from iteration. In this case, 3.

        The final index pair from our example is (2, 3) which corresponds to
        index 8 in the sorted list.

        :param int idx: index in sorted list
        :return: (lists index, sublist index) pair

        """
        if idx < 0:
            last_len = len(self._lists[-1])

            if (-idx) <= last_len:
                return len(self._lists) - 1, last_len + idx

            idx += self._len

            if idx < 0:
                raise IndexError('list index out of range')
        elif idx >= self._len:
            raise IndexError('list index out of range')

        if idx < len(self._lists[0]):
            return 0, idx

        _index = self._index

        if not _index:
            self._build_index()

        pos = 0
        child = 1
        len_index = len(_index)

        while child < len_index:
            index_child = _index[child]

            if idx < index_child:
                pos = child
            else:
                idx -= index_child
                pos = child + 1

            child = (pos << 1) + 1

        return (pos - self._offset, idx)


    def _build_index(self):
        """Build a positional index for indexing the sorted list.

        Indexes are represented as binary trees in a dense array notation
        similar to a binary heap.

        For example, given a lists representation storing integers::

            0: [1, 2, 3]
            1: [4, 5]
            2: [6, 7, 8, 9]
            3: [10, 11, 12, 13, 14]

        The first transformation maps the sub-lists by their length. The
        first row of the index is the length of the sub-lists::

            0: [3, 2, 4, 5]

        Each row after that is the sum of consecutive pairs of the previous
        row::

            1: [5, 9]
            2: [14]

        Finally, the index is built by concatenating these lists together::

            _index = [14, 5, 9, 3, 2, 4, 5]

        An offset storing the start of the first row is also stored::

            _offset = 3

        When built, the index can be used for efficient indexing into the list.
        See the comment and notes on ``SortedList._pos`` for details.

        """
        row0 = list(map(len, self._lists))

        if len(row0) == 1:
            self._index[:] = row0
            self._offset = 0
            return

        head = iter(row0)
        tail = iter(head)
        row1 = list(starmap(add, zip(head, tail)))

        if len(row0) & 1:
            row1.append(row0[-1])

        if len(row1) == 1:
            self._index[:] = row1 + row0
            self._offset = 1
            return

        size = 2 ** (int(log(len(row1) - 1, 2)) + 1)
        row1.extend(repeat(0, size - len(row1)))
        tree = [row0, row1]

        while len(tree[-1]) > 1:
            head = iter(tree[-1])
            tail = iter(head)
            row = list(starmap(add, zip(head, tail)))
            tree.append(row)

        reduce(iadd, reversed(tree), self._index)
        self._offset = size * 2 - 1


    def __delitem__(self, index):
        """Remove value at `index` from sorted list.

        ``sl.__delitem__(index)`` <==> ``del sl[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> del sl[2]
        >>> sl
        SortedList(['a', 'b', 'd', 'e'])
        >>> del sl[:2]
        >>> sl
        SortedList(['d', 'e'])

        :param index: integer or slice for indexing
        :raises IndexError: if index out of range

        """
        if isinstance(index, slice):
            start, stop, step = index.indices(self._len)

            if step == 1 and start < stop:
                if start == 0 and stop == self._len:
                    return self._clear()
                elif self._len <= 8 * (stop - start):
                    values = self._getitem(slice(None, start))
                    if stop < self._len:
                        values += self._getitem(slice(stop, None))
                    self._clear()
                    return self._update(values)

            indices = range(start, stop, step)

            # Delete items from greatest index to least so
            # that the indices remain valid throughout iteration.

            if step > 0:
                indices = reversed(indices)

            _pos, _delete = self._pos, self._delete

            for index in indices:
                pos, idx = _pos(index)
                _delete(pos, idx)
        else:
            pos, idx = self._pos(index)
            self._delete(pos, idx)


    def __getitem__(self, index):
        """Lookup value at `index` in sorted list.

        ``sl.__getitem__(index)`` <==> ``sl[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl[1]
        'b'
        >>> sl[-1]
        'e'
        >>> sl[2:5]
        ['c', 'd', 'e']

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        """
        _lists = self._lists

        if isinstance(index, slice):
            start, stop, step = index.indices(self._len)

            if step == 1 and start < stop:
                # Whole slice optimization: start to stop slices the whole
                # sorted list.

                if start == 0 and stop == self._len:
                    return reduce(iadd, self._lists, [])

                start_pos, start_idx = self._pos(start)
                start_list = _lists[start_pos]
                stop_idx = start_idx + stop - start

                # Small slice optimization: start index and stop index are
                # within the start list.

                if len(start_list) >= stop_idx:
                    return start_list[start_idx:stop_idx]

                if stop == self._len:
                    stop_pos = len(_lists) - 1
                    stop_idx = len(_lists[stop_pos])
                else:
                    stop_pos, stop_idx = self._pos(stop)

                prefix = _lists[start_pos][start_idx:]
                middle = _lists[(start_pos + 1):stop_pos]
                result = reduce(iadd, middle, prefix)
                result += _lists[stop_pos][:stop_idx]

                return result

            if step == -1 and start > stop:
                result = self._getitem(slice(stop + 1, start + 1))
                result.reverse()
                return result

            # Return a list because a negative step could
            # reverse the order of the items and this could
            # be the desired behavior.

            indices = range(start, stop, step)
            return list(self._getitem(index) for index in indices)
        else:
            if self._len:
                if index == 0:
                    return _lists[0][0]
                elif index == -1:
                    return _lists[-1][-1]
            else:
                raise IndexError('list index out of range')

            if 0 <= index < len(_lists[0]):
                return _lists[0][index]

            len_last = len(_lists[-1])

            if -len_last < index < 0:
                return _lists[-1][len_last + index]

            pos, idx = self._pos(index)
            return _lists[pos][idx]

    _getitem = __getitem__


    def __setitem__(self, index, value):
        """Raise not-implemented error.

        ``sl.__setitem__(index, value)`` <==> ``sl[index] = value``

        :raises NotImplementedError: use ``del sl[index]`` and
            ``sl.add(value)`` instead

        """
        message = 'use ``del sl[index]`` and ``sl.add(value)`` instead'
        raise NotImplementedError(message)


    def __iter__(self):
        """Return an iterator over the sorted list.

        ``sl.__iter__()`` <==> ``iter(sl)``

        Iterating the sorted list while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        """
        return chain.from_iterable(self._lists)


    def __reversed__(self):
        """Return a reverse iterator over the sorted list.

        ``sl.__reversed__()`` <==> ``reversed(sl)``

        Iterating the sorted list while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        """
        return chain.from_iterable(map(reversed, reversed(self._lists)))


    def reverse(self):
        """Raise not-implemented error.

        Sorted list maintains values in ascending sort order. Values may not be
        reversed in-place.

        Use ``reversed(sl)`` for an iterator over values in descending sort
        order.

        Implemented to override `MutableSequence.reverse` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``reversed(sl)`` instead

        """
        raise NotImplementedError('use ``reversed(sl)`` instead')


    def islice(self, start=None, stop=None, reverse=False):
        """Return an iterator that slices sorted list from `start` to `stop`.

        The `start` and `stop` index are treated inclusive and exclusive,
        respectively.

        Both `start` and `stop` default to `None` which is automatically
        inclusive of the beginning and end of the sorted list.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> sl = SortedList('abcdefghij')
        >>> it = sl.islice(2, 6)
        >>> list(it)
        ['c', 'd', 'e', 'f']

        :param int start: start index (inclusive)
        :param int stop: stop index (exclusive)
        :param bool reverse: yield values in reverse order
        :return: iterator

        """
        _len = self._len

        if not _len:
            return iter(())

        start, stop, _ = slice(start, stop).indices(self._len)

        if start >= stop:
            return iter(())

        _pos = self._pos

        min_pos, min_idx = _pos(start)

        if stop == _len:
            max_pos = len(self._lists) - 1
            max_idx = len(self._lists[-1])
        else:
            max_pos, max_idx = _pos(stop)

        return self._islice(min_pos, min_idx, max_pos, max_idx, reverse)


    def _islice(self, min_pos, min_idx, max_pos, max_idx, reverse):
        """Return an iterator that slices sorted list using two index pairs.

        The index pairs are (min_pos, min_idx) and (max_pos, max_idx), the
        first inclusive and the latter exclusive. See `_pos` for details on how
        an index is converted to an index pair.

        When `reverse` is `True`, values are yielded from the iterator in
        reverse order.

        """
        _lists = self._lists

        if min_pos > max_pos:
            return iter(())

        if min_pos == max_pos:
            if reverse:
                indices = reversed(range(min_idx, max_idx))
                return map(_lists[min_pos].__getitem__, indices)

            indices = range(min_idx, max_idx)
            return map(_lists[min_pos].__getitem__, indices)

        next_pos = min_pos + 1

        if next_pos == max_pos:
            if reverse:
                min_indices = range(min_idx, len(_lists[min_pos]))
                max_indices = range(max_idx)
                return chain(
                    map(_lists[max_pos].__getitem__, reversed(max_indices)),
                    map(_lists[min_pos].__getitem__, reversed(min_indices)),
                )

            min_indices = range(min_idx, len(_lists[min_pos]))
            max_indices = range(max_idx)
            return chain(
                map(_lists[min_pos].__getitem__, min_indices),
                map(_lists[max_pos].__getitem__, max_indices),
            )

        if reverse:
            min_indices = range(min_idx, len(_lists[min_pos]))
            sublist_indices = range(next_pos, max_pos)
            sublists = map(_lists.__getitem__, reversed(sublist_indices))
            max_indices = range(max_idx)
            return chain(
                map(_lists[max_pos].__getitem__, reversed(max_indices)),
                chain.from_iterable(map(reversed, sublists)),
                map(_lists[min_pos].__getitem__, reversed(min_indices)),
            )

        min_indices = range(min_idx, len(_lists[min_pos]))
        sublist_indices = range(next_pos, max_pos)
        sublists = map(_lists.__getitem__, sublist_indices)
        max_indices = range(max_idx)
        return chain(
            map(_lists[min_pos].__getitem__, min_indices),
            chain.from_iterable(sublists),
            map(_lists[max_pos].__getitem__, max_indices),
        )


    def irange(self, minimum=None, maximum=None, inclusive=(True, True),
               reverse=False):
        """Create an iterator of values between `minimum` and `maximum`.

        Both `minimum` and `maximum` default to `None` which is automatically
        inclusive of the beginning and end of the sorted list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> sl = SortedList('abcdefghij')
        >>> it = sl.irange('c', 'f')
        >>> list(it)
        ['c', 'd', 'e', 'f']

        :param minimum: minimum value to start iterating
        :param maximum: maximum value to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        """
        _maxes = self._maxes

        if not _maxes:
            return iter(())

        _lists = self._lists

        # Calculate the minimum (pos, idx) pair. By default this location
        # will be inclusive in our calculation.

        if minimum is None:
            min_pos = 0
            min_idx = 0
        else:
            if inclusive[0]:
                min_pos = bisect_left(_maxes, minimum)

                if min_pos == len(_maxes):
                    return iter(())

                min_idx = bisect_left(_lists[min_pos], minimum)
            else:
                min_pos = bisect_right(_maxes, minimum)

                if min_pos == len(_maxes):
                    return iter(())

                min_idx = bisect_right(_lists[min_pos], minimum)

        # Calculate the maximum (pos, idx) pair. By default this location
        # will be exclusive in our calculation.

        if maximum is None:
            max_pos = len(_maxes) - 1
            max_idx = len(_lists[max_pos])
        else:
            if inclusive[1]:
                max_pos = bisect_right(_maxes, maximum)

                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_lists[max_pos])
                else:
                    max_idx = bisect_right(_lists[max_pos], maximum)
            else:
                max_pos = bisect_left(_maxes, maximum)

                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_lists[max_pos])
                else:
                    max_idx = bisect_left(_lists[max_pos], maximum)

        return self._islice(min_pos, min_idx, max_pos, max_idx, reverse)


    def __len__(self):
        """Return the size of the sorted list.

        ``sl.__len__()`` <==> ``len(sl)``

        :return: size of sorted list

        """
        return self._len


    def bisect_left(self, value):
        """Return an index to insert `value` in the sorted list.

        If the `value` is already present, the insertion point will be before
        (to the left of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([10, 11, 12, 13, 14])
        >>> sl.bisect_left(12)
        2

        :param value: insertion index of value in sorted list
        :return: index

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        pos = bisect_left(_maxes, value)

        if pos == len(_maxes):
            return self._len

        idx = bisect_left(self._lists[pos], value)
        return self._loc(pos, idx)


    def bisect_right(self, value):
        """Return an index to insert `value` in the sorted list.

        Similar to `bisect_left`, but if `value` is already present, the
        insertion point will be after (to the right of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([10, 11, 12, 13, 14])
        >>> sl.bisect_right(12)
        3

        :param value: insertion index of value in sorted list
        :return: index

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        pos = bisect_right(_maxes, value)

        if pos == len(_maxes):
            return self._len

        idx = bisect_right(self._lists[pos], value)
        return self._loc(pos, idx)

    bisect = bisect_right
    _bisect_right = bisect_right


    def count(self, value):
        """Return number of occurrences of `value` in the sorted list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        >>> sl.count(3)
        3

        :param value: value to count in sorted list
        :return: count

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        pos_left = bisect_left(_maxes, value)

        if pos_left == len(_maxes):
            return 0

        _lists = self._lists
        idx_left = bisect_left(_lists[pos_left], value)
        pos_right = bisect_right(_maxes, value)

        if pos_right == len(_maxes):
            return self._len - self._loc(pos_left, idx_left)

        idx_right = bisect_right(_lists[pos_right], value)

        if pos_left == pos_right:
            return idx_right - idx_left

        right = self._loc(pos_right, idx_right)
        left = self._loc(pos_left, idx_left)
        return right - left


    def copy(self):
        """Return a shallow copy of the sorted list.

        Runtime complexity: `O(n)`

        :return: new sorted list

        """
        return self.__class__(self)

    __copy__ = copy


    def append(self, value):
        """Raise not-implemented error.

        Implemented to override `MutableSequence.append` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``sl.add(value)`` instead

        """
        raise NotImplementedError('use ``sl.add(value)`` instead')


    def extend(self, values):
        """Raise not-implemented error.

        Implemented to override `MutableSequence.extend` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``sl.update(values)`` instead

        """
        raise NotImplementedError('use ``sl.update(values)`` instead')


    def insert(self, index, value):
        """Raise not-implemented error.

        :raises NotImplementedError: use ``sl.add(value)`` instead

        """
        raise NotImplementedError('use ``sl.add(value)`` instead')


    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list.

        Raise :exc:`IndexError` if the sorted list is empty or index is out of
        range.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl.pop()
        'e'
        >>> sl.pop(2)
        'c'
        >>> sl
        SortedList(['a', 'b', 'd'])

        :param int index: index of value (default -1)
        :return: value
        :raises IndexError: if index is out of range

        """
        if not self._len:
            raise IndexError('pop index out of range')

        _lists = self._lists

        if index == 0:
            val = _lists[0][0]
            self._delete(0, 0)
            return val

        if index == -1:
            pos = len(_lists) - 1
            loc = len(_lists[pos]) - 1
            val = _lists[pos][loc]
            self._delete(pos, loc)
            return val

        if 0 <= index < len(_lists[0]):
            val = _lists[0][index]
            self._delete(0, index)
            return val

        len_last = len(_lists[-1])

        if -len_last < index < 0:
            pos = len(_lists) - 1
            loc = len_last + index
            val = _lists[pos][loc]
            self._delete(pos, loc)
            return val

        pos, idx = self._pos(index)
        val = _lists[pos][idx]
        self._delete(pos, idx)
        return val


    def index(self, value, start=None, stop=None):
        """Return first index of value in sorted list.

        Raise ValueError if `value` is not present.

        Index must be between `start` and `stop` for the `value` to be
        considered present. The default value, None, for `start` and `stop`
        indicate the beginning and end of the sorted list.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl.index('d')
        3
        >>> sl.index('z')
        Traceback (most recent call last):
          ...
        ValueError: 'z' is not in list

        :param value: value in sorted list
        :param int start: start index (default None, start of sorted list)
        :param int stop: stop index (default None, end of sorted list)
        :return: index of value
        :raises ValueError: if value is not present

        """
        _len = self._len

        if not _len:
            raise ValueError('{0!r} is not in list'.format(value))

        if start is None:
            start = 0
        if start < 0:
            start += _len
        if start < 0:
            start = 0

        if stop is None:
            stop = _len
        if stop < 0:
            stop += _len
        if stop > _len:
            stop = _len

        if stop <= start:
            raise ValueError('{0!r} is not in list'.format(value))

        _maxes = self._maxes
        pos_left = bisect_left(_maxes, value)

        if pos_left == len(_maxes):
            raise ValueError('{0!r} is not in list'.format(value))

        _lists = self._lists
        idx_left = bisect_left(_lists[pos_left], value)

        if _lists[pos_left][idx_left] != value:
            raise ValueError('{0!r} is not in list'.format(value))

        stop -= 1
        left = self._loc(pos_left, idx_left)

        if start <= left:
            if left <= stop:
                return left
        else:
            right = self._bisect_right(value) - 1

            if start <= right:
                return start

        raise ValueError('{0!r} is not in list'.format(value))


    def __add__(self, other):
        """Return new sorted list containing all values in both sequences.

        ``sl.__add__(other)`` <==> ``sl + other``

        Values in `other` do not need to be in sorted order.

        Runtime complexity: `O(n*log(n))`

        >>> sl1 = SortedList('bat')
        >>> sl2 = SortedList('cat')
        >>> sl1 + sl2
        SortedList(['a', 'a', 'b', 'c', 't', 't'])

        :param other: other iterable
        :return: new sorted list

        """
        values = reduce(iadd, self._lists, [])
        values.extend(other)
        return self.__class__(values)

    __radd__ = __add__


    def __iadd__(self, other):
        """Update sorted list with values from `other`.

        ``sl.__iadd__(other)`` <==> ``sl += other``

        Values in `other` do not need to be in sorted order.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> sl = SortedList('bat')
        >>> sl += 'cat'
        >>> sl
        SortedList(['a', 'a', 'b', 'c', 't', 't'])

        :param other: other iterable
        :return: existing sorted list

        """
        self._update(other)
        return self


    def __mul__(self, num):
        """Return new sorted list with `num` shallow copies of values.

        ``sl.__mul__(num)`` <==> ``sl * num``

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList('abc')
        >>> sl * 3
        SortedList(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'])

        :param int num: count of shallow copies
        :return: new sorted list

        """
        values = reduce(iadd, self._lists, []) * num
        return self.__class__(values)

    __rmul__ = __mul__


    def __imul__(self, num):
        """Update the sorted list with `num` shallow copies of values.

        ``sl.__imul__(num)`` <==> ``sl *= num``

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList('abc')
        >>> sl *= 3
        >>> sl
        SortedList(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'])

        :param int num: count of shallow copies
        :return: existing sorted list

        """
        values = reduce(iadd, self._lists, []) * num
        self._clear()
        self._update(values)
        return self


    def __make_cmp(seq_op, symbol, doc):
        "Make comparator method."
        def comparer(self, other):
            "Compare method for sorted list and sequence."
            if not isinstance(other, Sequence):
                return NotImplemented

            self_len = self._len
            len_other = len(other)

            if self_len != len_other:
                if seq_op is eq:
                    return False
                if seq_op is ne:
                    return True

            for alpha, beta in zip(self, other):
                if alpha != beta:
                    return seq_op(alpha, beta)

            return seq_op(self_len, len_other)

        seq_op_name = seq_op.__name__
        comparer.__name__ = '__{0}__'.format(seq_op_name)
        doc_str = """Return true if and only if sorted list is {0} `other`.

        ``sl.__{1}__(other)`` <==> ``sl {2} other``

        Comparisons use lexicographical order as with sequences.

        Runtime complexity: `O(n)`

        :param other: `other` sequence
        :return: true if sorted list is {0} `other`

        """
        comparer.__doc__ = dedent(doc_str.format(doc, seq_op_name, symbol))
        return comparer


    __eq__ = __make_cmp(eq, '==', 'equal to')
    __ne__ = __make_cmp(ne, '!=', 'not equal to')
    __lt__ = __make_cmp(lt, '<', 'less than')
    __gt__ = __make_cmp(gt, '>', 'greater than')
    __le__ = __make_cmp(le, '<=', 'less than or equal to')
    __ge__ = __make_cmp(ge, '>=', 'greater than or equal to')
    __make_cmp = staticmethod(__make_cmp)


    def __reduce__(self):
        values = reduce(iadd, self._lists, [])
        return (type(self), (values,))


    @recursive_repr()
    def __repr__(self):
        """Return string representation of sorted list.

        ``sl.__repr__()`` <==> ``repr(sl)``

        :return: string representation

        """
        return '{0}({1!r})'.format(type(self).__name__, list(self))


    def _check(self):
        """Check invariants of sorted list.

        Runtime complexity: `O(n)`

        """
        try:
            assert self._load >= 4
            assert len(self._maxes) == len(self._lists)
            assert self._len == sum(len(sublist) for sublist in self._lists)

            # Check all sublists are sorted.

            for sublist in self._lists:
                for pos in range(1, len(sublist)):
                    assert sublist[pos - 1] <= sublist[pos]

            # Check beginning/end of sublists are sorted.

            for pos in range(1, len(self._lists)):
                assert self._lists[pos - 1][-1] <= self._lists[pos][0]

            # Check _maxes index is the last value of each sublist.

            for pos in range(len(self._maxes)):
                assert self._maxes[pos] == self._lists[pos][-1]

            # Check sublist lengths are less than double load-factor.

            double = self._load << 1
            assert all(len(sublist) <= double for sublist in self._lists)

            # Check sublist lengths are greater than half load-factor for all
            # but the last sublist.

            half = self._load >> 1
            for pos in range(0, len(self._lists) - 1):
                assert len(self._lists[pos]) >= half

            if self._index:
                assert self._len == self._index[0]
                assert len(self._index) == self._offset + len(self._lists)

                # Check index leaf nodes equal length of sublists.

                for pos in range(len(self._lists)):
                    leaf = self._index[self._offset + pos]
                    assert leaf == len(self._lists[pos])

                # Check index branch nodes are the sum of their children.

                for pos in range(self._offset):
                    child = (pos << 1) + 1
                    if child >= len(self._index):
                        assert self._index[pos] == 0
                    elif child + 1 == len(self._index):
                        assert self._index[pos] == self._index[child]
                    else:
                        child_sum = self._index[child] + self._index[child + 1]
                        assert child_sum == self._index[pos]
        except:
            traceback.print_exc(file=sys.stdout)
            print('len', self._len)
            print('load', self._load)
            print('offset', self._offset)
            print('len_index', len(self._index))
            print('index', self._index)
            print('len_maxes', len(self._maxes))
            print('maxes', self._maxes)
            print('len_lists', len(self._lists))
            print('lists', self._lists)
            raise


def identity(value):
    "Identity function."
    return value


class SortedKeyList(SortedList):
    """Sorted-key list is a subtype of sorted list.

    The sorted-key list maintains values in comparison order based on the
    result of a key function applied to every value.

    All the same methods that are available in :class:`SortedList` are also
    available in :class:`SortedKeyList`.

    Additional methods provided:

    * :attr:`SortedKeyList.key`
    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Some examples below use:

    >>> from operator import neg
    >>> neg
    <built-in function neg>
    >>> neg(1)
    -1

    """
    def __init__(self, iterable=None, key=identity):
        """Initialize sorted-key list instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted-key list.

        Optional `key` argument defines a callable that, like the `key`
        argument to Python's `sorted` function, extracts a comparison key from
        each value. The default is the identity function.

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl
        SortedKeyList([], key=<built-in function neg>)
        >>> skl = SortedKeyList([3, 1, 2], key=neg)
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)

        """
        self._key = key
        self._len = 0
        self._load = self.DEFAULT_LOAD_FACTOR
        self._lists = []
        self._keys = []
        self._maxes = []
        self._index = []
        self._offset = 0

        if iterable is not None:
            self._update(iterable)


    def __new__(cls, iterable=None, key=identity):
        return object.__new__(cls)


    @property
    def key(self):
        "Function used to extract comparison key from values."
        return self._key


    def clear(self):
        """Remove all values from sorted-key list.

        Runtime complexity: `O(n)`

        """
        self._len = 0
        del self._lists[:]
        del self._keys[:]
        del self._maxes[:]
        del self._index[:]

    _clear = clear


    def add(self, value):
        """Add `value` to sorted-key list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl.add(3)
        >>> skl.add(1)
        >>> skl.add(2)
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param value: value to add to sorted-key list

        """
        _lists = self._lists
        _keys = self._keys
        _maxes = self._maxes

        key = self._key(value)

        if _maxes:
            pos = bisect_right(_maxes, key)

            if pos == len(_maxes):
                pos -= 1
                _lists[pos].append(value)
                _keys[pos].append(key)
                _maxes[pos] = key
            else:
                idx = bisect_right(_keys[pos], key)
                _lists[pos].insert(idx, value)
                _keys[pos].insert(idx, key)

            self._expand(pos)
        else:
            _lists.append([value])
            _keys.append([key])
            _maxes.append(key)

        self._len += 1


    def _expand(self, pos):
        """Split sublists with length greater than double the load-factor.

        Updates the index when the sublist length is less than double the load
        level. This requires incrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        """
        _lists = self._lists
        _keys = self._keys
        _index = self._index

        if len(_keys[pos]) > (self._load << 1):
            _maxes = self._maxes
            _load = self._load

            _lists_pos = _lists[pos]
            _keys_pos = _keys[pos]
            half = _lists_pos[_load:]
            half_keys = _keys_pos[_load:]
            del _lists_pos[_load:]
            del _keys_pos[_load:]
            _maxes[pos] = _keys_pos[-1]

            _lists.insert(pos + 1, half)
            _keys.insert(pos + 1, half_keys)
            _maxes.insert(pos + 1, half_keys[-1])

            del _index[:]
        else:
            if _index:
                child = self._offset + pos
                while child:
                    _index[child] += 1
                    child = (child - 1) >> 1
                _index[0] += 1


    def update(self, iterable):
        """Update sorted-key list by adding all values from `iterable`.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl.update([3, 1, 2])
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param iterable: iterable of values to add

        """
        _lists = self._lists
        _keys = self._keys
        _maxes = self._maxes
        values = sorted(iterable, key=self._key)

        if _maxes:
            if len(values) * 4 >= self._len:
                _lists.append(values)
                values = reduce(iadd, _lists, [])
                values.sort(key=self._key)
                self._clear()
            else:
                _add = self.add
                for val in values:
                    _add(val)
                return

        _load = self._load
        _lists.extend(values[pos:(pos + _load)]
                      for pos in range(0, len(values), _load))
        _keys.extend(list(map(self._key, _list)) for _list in _lists)
        _maxes.extend(sublist[-1] for sublist in _keys)
        self._len = len(values)
        del self._index[:]

    _update = update


    def __contains__(self, value):
        """Return true if `value` is an element of the sorted-key list.

        ``skl.__contains__(value)`` <==> ``value in skl``

        Runtime complexity: `O(log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList([1, 2, 3, 4, 5], key=neg)
        >>> 3 in skl
        True

        :param value: search for value in sorted-key list
        :return: true if `value` in sorted-key list

        """
        _maxes = self._maxes

        if not _maxes:
            return False

        key = self._key(value)
        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            return False

        _lists = self._lists
        _keys = self._keys

        idx = bisect_left(_keys[pos], key)

        len_keys = len(_keys)
        len_sublist = len(_keys[pos])

        while True:
            if _keys[pos][idx] != key:
                return False
            if _lists[pos][idx] == value:
                return True
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    return False
                len_sublist = len(_keys[pos])
                idx = 0


    def discard(self, value):
        """Remove `value` from sorted-key list if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.discard(1)
        >>> skl.discard(0)
        >>> skl == [5, 4, 3, 2]
        True

        :param value: `value` to discard from sorted-key list

        """
        _maxes = self._maxes

        if not _maxes:
            return

        key = self._key(value)
        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            return

        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])

        while True:
            if _keys[pos][idx] != key:
                return
            if _lists[pos][idx] == value:
                self._delete(pos, idx)
                return
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    return
                len_sublist = len(_keys[pos])
                idx = 0


    def remove(self, value):
        """Remove `value` from sorted-key list; `value` must be a member.

        If `value` is not a member, raise ValueError.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([1, 2, 3, 4, 5], key=neg)
        >>> skl.remove(5)
        >>> skl == [4, 3, 2, 1]
        True
        >>> skl.remove(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 not in list

        :param value: `value` to remove from sorted-key list
        :raises ValueError: if `value` is not in sorted-key list

        """
        _maxes = self._maxes

        if not _maxes:
            raise ValueError('{0!r} not in list'.format(value))

        key = self._key(value)
        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            raise ValueError('{0!r} not in list'.format(value))

        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])

        while True:
            if _keys[pos][idx] != key:
                raise ValueError('{0!r} not in list'.format(value))
            if _lists[pos][idx] == value:
                self._delete(pos, idx)
                return
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    raise ValueError('{0!r} not in list'.format(value))
                len_sublist = len(_keys[pos])
                idx = 0


    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`.

        Combines lists that are less than half the load level.

        Updates the index when the sublist length is more than half the load
        level. This requires decrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        :param int pos: lists index
        :param int idx: sublist index

        """
        _lists = self._lists
        _keys = self._keys
        _maxes = self._maxes
        _index = self._index
        keys_pos = _keys[pos]
        lists_pos = _lists[pos]

        del keys_pos[idx]
        del lists_pos[idx]
        self._len -= 1

        len_keys_pos = len(keys_pos)

        if len_keys_pos > (self._load >> 1):
            _maxes[pos] = keys_pos[-1]

            if _index:
                child = self._offset + pos
                while child > 0:
                    _index[child] -= 1
                    child = (child - 1) >> 1
                _index[0] -= 1
        elif len(_keys) > 1:
            if not pos:
                pos += 1

            prev = pos - 1
            _keys[prev].extend(_keys[pos])
            _lists[prev].extend(_lists[pos])
            _maxes[prev] = _keys[prev][-1]

            del _lists[pos]
            del _keys[pos]
            del _maxes[pos]
            del _index[:]

            self._expand(prev)
        elif len_keys_pos:
            _maxes[pos] = keys_pos[-1]
        else:
            del _lists[pos]
            del _keys[pos]
            del _maxes[pos]
            del _index[:]


    def irange(self, minimum=None, maximum=None, inclusive=(True, True),
               reverse=False):
        """Create an iterator of values between `minimum` and `maximum`.

        Both `minimum` and `maximum` default to `None` which is automatically
        inclusive of the beginning and end of the sorted-key list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> from operator import neg
        >>> skl = SortedKeyList([11, 12, 13, 14, 15], key=neg)
        >>> it = skl.irange(14.5, 11.5)
        >>> list(it)
        [14, 13, 12]

        :param minimum: minimum value to start iterating
        :param maximum: maximum value to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        """
        min_key = self._key(minimum) if minimum is not None else None
        max_key = self._key(maximum) if maximum is not None else None
        return self._irange_key(
            min_key=min_key, max_key=max_key,
            inclusive=inclusive, reverse=reverse,
        )


    def irange_key(self, min_key=None, max_key=None, inclusive=(True, True),
                   reverse=False):
        """Create an iterator of values between `min_key` and `max_key`.

        Both `min_key` and `max_key` default to `None` which is automatically
        inclusive of the beginning and end of the sorted-key list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> from operator import neg
        >>> skl = SortedKeyList([11, 12, 13, 14, 15], key=neg)
        >>> it = skl.irange_key(-14, -12)
        >>> list(it)
        [14, 13, 12]

        :param min_key: minimum key to start iterating
        :param max_key: maximum key to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        """
        _maxes = self._maxes

        if not _maxes:
            return iter(())

        _keys = self._keys

        # Calculate the minimum (pos, idx) pair. By default this location
        # will be inclusive in our calculation.

        if min_key is None:
            min_pos = 0
            min_idx = 0
        else:
            if inclusive[0]:
                min_pos = bisect_left(_maxes, min_key)

                if min_pos == len(_maxes):
                    return iter(())

                min_idx = bisect_left(_keys[min_pos], min_key)
            else:
                min_pos = bisect_right(_maxes, min_key)

                if min_pos == len(_maxes):
                    return iter(())

                min_idx = bisect_right(_keys[min_pos], min_key)

        # Calculate the maximum (pos, idx) pair. By default this location
        # will be exclusive in our calculation.

        if max_key is None:
            max_pos = len(_maxes) - 1
            max_idx = len(_keys[max_pos])
        else:
            if inclusive[1]:
                max_pos = bisect_right(_maxes, max_key)

                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_keys[max_pos])
                else:
                    max_idx = bisect_right(_keys[max_pos], max_key)
            else:
                max_pos = bisect_left(_maxes, max_key)

                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_keys[max_pos])
                else:
                    max_idx = bisect_left(_keys[max_pos], max_key)

        return self._islice(min_pos, min_idx, max_pos, max_idx, reverse)

    _irange_key = irange_key


    def bisect_left(self, value):
        """Return an index to insert `value` in the sorted-key list.

        If the `value` is already present, the insertion point will be before
        (to the left of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_left(1)
        4

        :param value: insertion index of value in sorted-key list
        :return: index

        """
        return self._bisect_key_left(self._key(value))


    def bisect_right(self, value):
        """Return an index to insert `value` in the sorted-key list.

        Similar to `bisect_left`, but if `value` is already present, the
        insertion point will be after (to the right of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_right(1)
        5

        :param value: insertion index of value in sorted-key list
        :return: index

        """
        return self._bisect_key_right(self._key(value))

    bisect = bisect_right


    def bisect_key_left(self, key):
        """Return an index to insert `key` in the sorted-key list.

        If the `key` is already present, the insertion point will be before (to
        the left of) any existing keys.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_key_left(-1)
        4

        :param key: insertion index of key in sorted-key list
        :return: index

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            return self._len

        idx = bisect_left(self._keys[pos], key)

        return self._loc(pos, idx)

    _bisect_key_left = bisect_key_left


    def bisect_key_right(self, key):
        """Return an index to insert `key` in the sorted-key list.

        Similar to `bisect_key_left`, but if `key` is already present, the
        insertion point will be after (to the right of) any existing keys.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_key_right(-1)
        5

        :param key: insertion index of key in sorted-key list
        :return: index

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        pos = bisect_right(_maxes, key)

        if pos == len(_maxes):
            return self._len

        idx = bisect_right(self._keys[pos], key)

        return self._loc(pos, idx)

    bisect_key = bisect_key_right
    _bisect_key_right = bisect_key_right


    def count(self, value):
        """Return number of occurrences of `value` in the sorted-key list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([4, 4, 4, 4, 3, 3, 3, 2, 2, 1], key=neg)
        >>> skl.count(2)
        2

        :param value: value to count in sorted-key list
        :return: count

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        key = self._key(value)
        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            return 0

        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        total = 0
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])

        while True:
            if _keys[pos][idx] != key:
                return total
            if _lists[pos][idx] == value:
                total += 1
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    return total
                len_sublist = len(_keys[pos])
                idx = 0


    def copy(self):
        """Return a shallow copy of the sorted-key list.

        Runtime complexity: `O(n)`

        :return: new sorted-key list

        """
        return self.__class__(self, key=self._key)

    __copy__ = copy


    def index(self, value, start=None, stop=None):
        """Return first index of value in sorted-key list.

        Raise ValueError if `value` is not present.

        Index must be between `start` and `stop` for the `value` to be
        considered present. The default value, None, for `start` and `stop`
        indicate the beginning and end of the sorted-key list.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.index(2)
        3
        >>> skl.index(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 is not in list

        :param value: value in sorted-key list
        :param int start: start index (default None, start of sorted-key list)
        :param int stop: stop index (default None, end of sorted-key list)
        :return: index of value
        :raises ValueError: if value is not present

        """
        _len = self._len

        if not _len:
            raise ValueError('{0!r} is not in list'.format(value))

        if start is None:
            start = 0
        if start < 0:
            start += _len
        if start < 0:
            start = 0

        if stop is None:
            stop = _len
        if stop < 0:
            stop += _len
        if stop > _len:
            stop = _len

        if stop <= start:
            raise ValueError('{0!r} is not in list'.format(value))

        _maxes = self._maxes
        key = self._key(value)
        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            raise ValueError('{0!r} is not in list'.format(value))

        stop -= 1
        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])

        while True:
            if _keys[pos][idx] != key:
                raise ValueError('{0!r} is not in list'.format(value))
            if _lists[pos][idx] == value:
                loc = self._loc(pos, idx)
                if start <= loc <= stop:
                    return loc
                elif loc > stop:
                    break
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    raise ValueError('{0!r} is not in list'.format(value))
                len_sublist = len(_keys[pos])
                idx = 0

        raise ValueError('{0!r} is not in list'.format(value))


    def __add__(self, other):
        """Return new sorted-key list containing all values in both sequences.

        ``skl.__add__(other)`` <==> ``skl + other``

        Values in `other` do not need to be in sorted-key order.

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl1 = SortedKeyList([5, 4, 3], key=neg)
        >>> skl2 = SortedKeyList([2, 1, 0], key=neg)
        >>> skl1 + skl2
        SortedKeyList([5, 4, 3, 2, 1, 0], key=<built-in function neg>)

        :param other: other iterable
        :return: new sorted-key list

        """
        values = reduce(iadd, self._lists, [])
        values.extend(other)
        return self.__class__(values, key=self._key)

    __radd__ = __add__


    def __mul__(self, num):
        """Return new sorted-key list with `num` shallow copies of values.

        ``skl.__mul__(num)`` <==> ``skl * num``

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList([3, 2, 1], key=neg)
        >>> skl * 2
        SortedKeyList([3, 3, 2, 2, 1, 1], key=<built-in function neg>)

        :param int num: count of shallow copies
        :return: new sorted-key list

        """
        values = reduce(iadd, self._lists, []) * num
        return self.__class__(values, key=self._key)


    def __reduce__(self):
        values = reduce(iadd, self._lists, [])
        return (type(self), (values, self.key))


    @recursive_repr()
    def __repr__(self):
        """Return string representation of sorted-key list.

        ``skl.__repr__()`` <==> ``repr(skl)``

        :return: string representation

        """
        type_name = type(self).__name__
        return '{0}({1!r}, key={2!r})'.format(type_name, list(self), self._key)


    def _check(self):
        """Check invariants of sorted-key list.

        Runtime complexity: `O(n)`

        """
        try:
            assert self._load >= 4
            assert len(self._maxes) == len(self._lists) == len(self._keys)
            assert self._len == sum(len(sublist) for sublist in self._lists)

            # Check all sublists are sorted.

            for sublist in self._keys:
                for pos in range(1, len(sublist)):
                    assert sublist[pos - 1] <= sublist[pos]

            # Check beginning/end of sublists are sorted.

            for pos in range(1, len(self._keys)):
                assert self._keys[pos - 1][-1] <= self._keys[pos][0]

            # Check _keys matches _key mapped to _lists.

            for val_sublist, key_sublist in zip(self._lists, self._keys):
                assert len(val_sublist) == len(key_sublist)
                for val, key in zip(val_sublist, key_sublist):
                    assert self._key(val) == key

            # Check _maxes index is the last value of each sublist.

            for pos in range(len(self._maxes)):
                assert self._maxes[pos] == self._keys[pos][-1]

            # Check sublist lengths are less than double load-factor.

            double = self._load << 1
            assert all(len(sublist) <= double for sublist in self._lists)

            # Check sublist lengths are greater than half load-factor for all
            # but the last sublist.

            half = self._load >> 1
            for pos in range(0, len(self._lists) - 1):
                assert len(self._lists[pos]) >= half

            if self._index:
                assert self._len == self._index[0]
                assert len(self._index) == self._offset + len(self._lists)

                # Check index leaf nodes equal length of sublists.

                for pos in range(len(self._lists)):
                    leaf = self._index[self._offset + pos]
                    assert leaf == len(self._lists[pos])

                # Check index branch nodes are the sum of their children.

                for pos in range(self._offset):
                    child = (pos << 1) + 1
                    if child >= len(self._index):
                        assert self._index[pos] == 0
                    elif child + 1 == len(self._index):
                        assert self._index[pos] == self._index[child]
                    else:
                        child_sum = self._index[child] + self._index[child + 1]
                        assert child_sum == self._index[pos]
        except:
            traceback.print_exc(file=sys.stdout)
            print('len', self._len)
            print('load', self._load)
            print('offset', self._offset)
            print('len_index', len(self._index))
            print('index', self._index)
            print('len_maxes', len(self._maxes))
            print('maxes', self._maxes)
            print('len_keys', len(self._keys))
            print('keys', self._keys)
            print('len_lists', len(self._lists))
            print('lists', self._lists)
            raise


SortedListWithKey = SortedKeyList
PK     ˀ�Y�h:�NP  NP     sortedcontainers/sortedset.py"""Sorted Set
=============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted set implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedSet`

"""

from itertools import chain
from operator import eq, ne, gt, ge, lt, le
from textwrap import dedent

from .sortedlist import SortedList, recursive_repr

###############################################################################
# BEGIN Python 2/3 Shims
###############################################################################

try:
    from collections.abc import MutableSet, Sequence, Set
except ImportError:
    from collections import MutableSet, Sequence, Set

###############################################################################
# END Python 2/3 Shims
###############################################################################


class SortedSet(MutableSet, Sequence):
    """Sorted set is a sorted mutable set.

    Sorted set values are maintained in sorted order. The design of sorted set
    is simple: sorted set uses a set for set-operations and maintains a sorted
    list of values.

    Sorted set values must be hashable and comparable. The hash and total
    ordering of values must not change while they are stored in the sorted set.

    Mutable set methods:

    * :func:`SortedSet.__contains__`
    * :func:`SortedSet.__iter__`
    * :func:`SortedSet.__len__`
    * :func:`SortedSet.add`
    * :func:`SortedSet.discard`

    Sequence methods:

    * :func:`SortedSet.__getitem__`
    * :func:`SortedSet.__delitem__`
    * :func:`SortedSet.__reversed__`

    Methods for removing values:

    * :func:`SortedSet.clear`
    * :func:`SortedSet.pop`
    * :func:`SortedSet.remove`

    Set-operation methods:

    * :func:`SortedSet.difference`
    * :func:`SortedSet.difference_update`
    * :func:`SortedSet.intersection`
    * :func:`SortedSet.intersection_update`
    * :func:`SortedSet.symmetric_difference`
    * :func:`SortedSet.symmetric_difference_update`
    * :func:`SortedSet.union`
    * :func:`SortedSet.update`

    Methods for miscellany:

    * :func:`SortedSet.copy`
    * :func:`SortedSet.count`
    * :func:`SortedSet.__repr__`
    * :func:`SortedSet._check`

    Sorted list methods available:

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.index`
    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList._reset`

    Additional sorted list methods available, if key-function used:

    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Sorted set comparisons use subset and superset relations. Two sorted sets
    are equal if and only if every element of each sorted set is contained in
    the other (each is a subset of the other). A sorted set is less than
    another sorted set if and only if the first sorted set is a proper subset
    of the second sorted set (is a subset, but is not equal). A sorted set is
    greater than another sorted set if and only if the first sorted set is a
    proper superset of the second sorted set (is a superset, but is not equal).

    """
    def __init__(self, iterable=None, key=None):
        """Initialize sorted set instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted set.

        Optional `key` argument defines a callable that, like the `key`
        argument to Python's `sorted` function, extracts a comparison key from
        each value. The default, none, compares values directly.

        Runtime complexity: `O(n*log(n))`

        >>> ss = SortedSet([3, 1, 2, 5, 4])
        >>> ss
        SortedSet([1, 2, 3, 4, 5])
        >>> from operator import neg
        >>> ss = SortedSet([3, 1, 2, 5, 4], neg)
        >>> ss
        SortedSet([5, 4, 3, 2, 1], key=<built-in function neg>)

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)

        """
        self._key = key

        # SortedSet._fromset calls SortedSet.__init__ after initializing the
        # _set attribute. So only create a new set if the _set attribute is not
        # already present.

        if not hasattr(self, '_set'):
            self._set = set()

        self._list = SortedList(self._set, key=key)

        # Expose some set methods publicly.

        _set = self._set
        self.isdisjoint = _set.isdisjoint
        self.issubset = _set.issubset
        self.issuperset = _set.issuperset

        # Expose some sorted list methods publicly.

        _list = self._list
        self.bisect_left = _list.bisect_left
        self.bisect = _list.bisect
        self.bisect_right = _list.bisect_right
        self.index = _list.index
        self.irange = _list.irange
        self.islice = _list.islice
        self._reset = _list._reset

        if key is not None:
            self.bisect_key_left = _list.bisect_key_left
            self.bisect_key_right = _list.bisect_key_right
            self.bisect_key = _list.bisect_key
            self.irange_key = _list.irange_key

        if iterable is not None:
            self._update(iterable)


    @classmethod
    def _fromset(cls, values, key=None):
        """Initialize sorted set from existing set.

        Used internally by set operations that return a new set.

        """
        sorted_set = object.__new__(cls)
        sorted_set._set = values
        sorted_set.__init__(key=key)
        return sorted_set


    @property
    def key(self):
        """Function used to extract comparison key from values.

        Sorted set compares values directly when the key function is none.

        """
        return self._key


    def __contains__(self, value):
        """Return true if `value` is an element of the sorted set.

        ``ss.__contains__(value)`` <==> ``value in ss``

        Runtime complexity: `O(1)`

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> 3 in ss
        True

        :param value: search for value in sorted set
        :return: true if `value` in sorted set

        """
        return value in self._set


    def __getitem__(self, index):
        """Lookup value at `index` in sorted set.

        ``ss.__getitem__(index)`` <==> ``ss[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> ss[2]
        'c'
        >>> ss[-1]
        'e'
        >>> ss[2:5]
        ['c', 'd', 'e']

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        """
        return self._list[index]


    def __delitem__(self, index):
        """Remove value at `index` from sorted set.

        ``ss.__delitem__(index)`` <==> ``del ss[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> del ss[2]
        >>> ss
        SortedSet(['a', 'b', 'd', 'e'])
        >>> del ss[:2]
        >>> ss
        SortedSet(['d', 'e'])

        :param index: integer or slice for indexing
        :raises IndexError: if index out of range

        """
        _set = self._set
        _list = self._list
        if isinstance(index, slice):
            values = _list[index]
            _set.difference_update(values)
        else:
            value = _list[index]
            _set.remove(value)
        del _list[index]


    def __make_cmp(set_op, symbol, doc):
        "Make comparator method."
        def comparer(self, other):
            "Compare method for sorted set and set."
            if isinstance(other, SortedSet):
                return set_op(self._set, other._set)
            elif isinstance(other, Set):
                return set_op(self._set, other)
            return NotImplemented

        set_op_name = set_op.__name__
        comparer.__name__ = '__{0}__'.format(set_op_name)
        doc_str = """Return true if and only if sorted set is {0} `other`.

        ``ss.__{1}__(other)`` <==> ``ss {2} other``

        Comparisons use subset and superset semantics as with sets.

        Runtime complexity: `O(n)`

        :param other: `other` set
        :return: true if sorted set is {0} `other`

        """
        comparer.__doc__ = dedent(doc_str.format(doc, set_op_name, symbol))
        return comparer


    __eq__ = __make_cmp(eq, '==', 'equal to')
    __ne__ = __make_cmp(ne, '!=', 'not equal to')
    __lt__ = __make_cmp(lt, '<', 'a proper subset of')
    __gt__ = __make_cmp(gt, '>', 'a proper superset of')
    __le__ = __make_cmp(le, '<=', 'a subset of')
    __ge__ = __make_cmp(ge, '>=', 'a superset of')
    __make_cmp = staticmethod(__make_cmp)


    def __len__(self):
        """Return the size of the sorted set.

        ``ss.__len__()`` <==> ``len(ss)``

        :return: size of sorted set

        """
        return len(self._set)


    def __iter__(self):
        """Return an iterator over the sorted set.

        ``ss.__iter__()`` <==> ``iter(ss)``

        Iterating the sorted set while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        """
        return iter(self._list)


    def __reversed__(self):
        """Return a reverse iterator over the sorted set.

        ``ss.__reversed__()`` <==> ``reversed(ss)``

        Iterating the sorted set while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        """
        return reversed(self._list)


    def add(self, value):
        """Add `value` to sorted set.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet()
        >>> ss.add(3)
        >>> ss.add(1)
        >>> ss.add(2)
        >>> ss
        SortedSet([1, 2, 3])

        :param value: value to add to sorted set

        """
        _set = self._set
        if value not in _set:
            _set.add(value)
            self._list.add(value)

    _add = add


    def clear(self):
        """Remove all values from sorted set.

        Runtime complexity: `O(n)`

        """
        self._set.clear()
        self._list.clear()


    def copy(self):
        """Return a shallow copy of the sorted set.

        Runtime complexity: `O(n)`

        :return: new sorted set

        """
        return self._fromset(set(self._set), key=self._key)

    __copy__ = copy


    def count(self, value):
        """Return number of occurrences of `value` in the sorted set.

        Runtime complexity: `O(1)`

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.count(3)
        1

        :param value: value to count in sorted set
        :return: count

        """
        return 1 if value in self._set else 0


    def discard(self, value):
        """Remove `value` from sorted set if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.discard(5)
        >>> ss.discard(0)
        >>> ss == set([1, 2, 3, 4])
        True

        :param value: `value` to discard from sorted set

        """
        _set = self._set
        if value in _set:
            _set.remove(value)
            self._list.remove(value)

    _discard = discard


    def pop(self, index=-1):
        """Remove and return value at `index` in sorted set.

        Raise :exc:`IndexError` if the sorted set is empty or index is out of
        range.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> ss.pop()
        'e'
        >>> ss.pop(2)
        'c'
        >>> ss
        SortedSet(['a', 'b', 'd'])

        :param int index: index of value (default -1)
        :return: value
        :raises IndexError: if index is out of range

        """
        # pylint: disable=arguments-differ
        value = self._list.pop(index)
        self._set.remove(value)
        return value


    def remove(self, value):
        """Remove `value` from sorted set; `value` must be a member.

        If `value` is not a member, raise :exc:`KeyError`.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.remove(5)
        >>> ss == set([1, 2, 3, 4])
        True
        >>> ss.remove(0)
        Traceback (most recent call last):
          ...
        KeyError: 0

        :param value: `value` to remove from sorted set
        :raises KeyError: if `value` is not in sorted set

        """
        self._set.remove(value)
        self._list.remove(value)


    def difference(self, *iterables):
        """Return the difference of two or more sets as a new sorted set.

        The `difference` method also corresponds to operator ``-``.

        ``ss.__sub__(iterable)`` <==> ``ss - iterable``

        The difference is all values that are in this sorted set but not the
        other `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.difference([4, 5, 6, 7])
        SortedSet([1, 2, 3])

        :param iterables: iterable arguments
        :return: new sorted set

        """
        diff = self._set.difference(*iterables)
        return self._fromset(diff, key=self._key)

    __sub__ = difference


    def difference_update(self, *iterables):
        """Remove all values of `iterables` from this sorted set.

        The `difference_update` method also corresponds to operator ``-=``.

        ``ss.__isub__(iterable)`` <==> ``ss -= iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.difference_update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3])

        :param iterables: iterable arguments
        :return: itself

        """
        _set = self._set
        _list = self._list
        values = set(chain(*iterables))
        if (4 * len(values)) > len(_set):
            _set.difference_update(values)
            _list.clear()
            _list.update(_set)
        else:
            _discard = self._discard
            for value in values:
                _discard(value)
        return self

    __isub__ = difference_update


    def intersection(self, *iterables):
        """Return the intersection of two or more sets as a new sorted set.

        The `intersection` method also corresponds to operator ``&``.

        ``ss.__and__(iterable)`` <==> ``ss & iterable``

        The intersection is all values that are in this sorted set and each of
        the other `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.intersection([4, 5, 6, 7])
        SortedSet([4, 5])

        :param iterables: iterable arguments
        :return: new sorted set

        """
        intersect = self._set.intersection(*iterables)
        return self._fromset(intersect, key=self._key)

    __and__ = intersection
    __rand__ = __and__


    def intersection_update(self, *iterables):
        """Update the sorted set with the intersection of `iterables`.

        The `intersection_update` method also corresponds to operator ``&=``.

        ``ss.__iand__(iterable)`` <==> ``ss &= iterable``

        Keep only values found in itself and all `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.intersection_update([4, 5, 6, 7])
        >>> ss
        SortedSet([4, 5])

        :param iterables: iterable arguments
        :return: itself

        """
        _set = self._set
        _list = self._list
        _set.intersection_update(*iterables)
        _list.clear()
        _list.update(_set)
        return self

    __iand__ = intersection_update


    def symmetric_difference(self, other):
        """Return the symmetric difference with `other` as a new sorted set.

        The `symmetric_difference` method also corresponds to operator ``^``.

        ``ss.__xor__(other)`` <==> ``ss ^ other``

        The symmetric difference is all values tha are in exactly one of the
        sets.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.symmetric_difference([4, 5, 6, 7])
        SortedSet([1, 2, 3, 6, 7])

        :param other: `other` iterable
        :return: new sorted set

        """
        diff = self._set.symmetric_difference(other)
        return self._fromset(diff, key=self._key)

    __xor__ = symmetric_difference
    __rxor__ = __xor__


    def symmetric_difference_update(self, other):
        """Update the sorted set with the symmetric difference with `other`.

        The `symmetric_difference_update` method also corresponds to operator
        ``^=``.

        ``ss.__ixor__(other)`` <==> ``ss ^= other``

        Keep only values found in exactly one of itself and `other`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.symmetric_difference_update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3, 6, 7])

        :param other: `other` iterable
        :return: itself

        """
        _set = self._set
        _list = self._list
        _set.symmetric_difference_update(other)
        _list.clear()
        _list.update(_set)
        return self

    __ixor__ = symmetric_difference_update


    def union(self, *iterables):
        """Return new sorted set with values from itself and all `iterables`.

        The `union` method also corresponds to operator ``|``.

        ``ss.__or__(iterable)`` <==> ``ss | iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.union([4, 5, 6, 7])
        SortedSet([1, 2, 3, 4, 5, 6, 7])

        :param iterables: iterable arguments
        :return: new sorted set

        """
        return self.__class__(chain(iter(self), *iterables), key=self._key)

    __or__ = union
    __ror__ = __or__


    def update(self, *iterables):
        """Update the sorted set adding values from all `iterables`.

        The `update` method also corresponds to operator ``|=``.

        ``ss.__ior__(iterable)`` <==> ``ss |= iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3, 4, 5, 6, 7])

        :param iterables: iterable arguments
        :return: itself

        """
        _set = self._set
        _list = self._list
        values = set(chain(*iterables))
        if (4 * len(values)) > len(_set):
            _list = self._list
            _set.update(values)
            _list.clear()
            _list.update(_set)
        else:
            _add = self._add
            for value in values:
                _add(value)
        return self

    __ior__ = update
    _update = update


    def __reduce__(self):
        """Support for pickle.

        The tricks played with exposing methods in :func:`SortedSet.__init__`
        confuse pickle so customize the reducer.

        """
        return (type(self), (self._set, self._key))


    @recursive_repr()
    def __repr__(self):
        """Return string representation of sorted set.

        ``ss.__repr__()`` <==> ``repr(ss)``

        :return: string representation

        """
        _key = self._key
        key = '' if _key is None else ', key={0!r}'.format(_key)
        type_name = type(self).__name__
        return '{0}({1!r}{2})'.format(type_name, list(self), key)


    def _check(self):
        """Check invariants of sorted set.

        Runtime complexity: `O(n)`

        """
        _set = self._set
        _list = self._list
        _list._check()
        assert len(_set) == len(_list)
        assert all(value in _set for value in _list)
PK     ˀ�Y               tree/PK     ˀ�Y               tree/__pycache__/PK       ��YS0�"�  �             ��    __main__.pyPK      ���Y                      �A�  __pycache__/PK      &��Y_�:��  �  $           ��  __pycache__/__main__.cpython-312.pycPK      ���Y�%�E  E  &           ��K  __pycache__/planesweep.cpython-312.pycPK      )h�Y            	          �A�#  geometry/PK      4��Y                      �A�#  geometry/__pycache__/PK      4��Y)���  �  ,           ��.$  geometry/__pycache__/Polygon.cpython-312.pycPK      "��Y	��I&  &             ��i)  geometry/Polygon.pyPK      ˀ�Y                      �A�,  intervaltree/PK      ˀ�Yq�m;g  g             ���,  intervaltree/__init__.pyPK      ���Y                      �A�0  intervaltree/__pycache__/PK      ���YQ�_@  @  1           ���0  intervaltree/__pycache__/__init__.cpython-312.pycPK      ���Y�mB4  4  1           ��N5  intervaltree/__pycache__/interval.cpython-312.pycPK      ���Y	��  �  5           ���i  intervaltree/__pycache__/intervaltree.cpython-312.pycPK      ���YI{[q*X  *X  -           ��	. intervaltree/__pycache__/node.cpython-312.pycPK      ���Y	�ɞ>)  >)             ��~� intervaltree/interval.pyPK      ˀ�Yb%�ū  ū             ��� intervaltree/intervaltree.pyPK      ˀ�Y��_I(-  (-             ���[ intervaltree/LICENSE.txtPK      ˀ�Y/����X  �X             ��O� intervaltree/node.pyPK      g��Yb�lZa  a             ��� planesweep.pyPK      �j�Y                      �A�� priorityqueue/PK      �|�Y                      �A�� priorityqueue/__pycache__/PK      �|�Y[݁��  �  9           ���� priorityqueue/__pycache__/PrioritizedItem.cpython-312.pycPK      �|�Yϸn�   �               ��>� priorityqueue/PrioritizedItem.pyPK      ˀ�Y                      �AH� sortedcontainers/PK      ˀ�Y�꒤�  �             ��w� sortedcontainers/__init__.pyPK      ���Y                      �AN  sortedcontainers/__pycache__/PK      ���Y�Z�X	  X	  5           ���  sortedcontainers/__pycache__/__init__.cpython-312.pycPK      ���Y�3xҶl  �l  7           ��4
 sortedcontainers/__pycache__/sorteddict.cpython-312.pycPK      ���Ynj���R �R 7           ��?w sortedcontainers/__pycache__/sortedlist.cpython-312.pycPK      ���Y2��_  �_  6           ��;� sortedcontainers/__pycache__/sortedset.cpython-312.pycPK      ˀ�Y��Ea:  :             ��Q* sortedcontainers/LICENSEPK      ˀ�Y���k�[  �[             ���, sortedcontainers/sorteddict.pyPK      ˀ�Y�gXi�4 �4            ��� sortedcontainers/sortedlist.pyPK      ˀ�Y�h:�NP  NP             ���� sortedcontainers/sortedset.pyPK      ˀ�Y                      �A' tree/PK      ˀ�Y                      �AJ tree/__pycache__/PK    % % �
  y   