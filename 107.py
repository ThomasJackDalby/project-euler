"""
    Problem 107
    ===========
    
    The following undirected network consists of seven vertices and twelve
    edges with a total weight of 243.
    
    The same network can be represented by the matrix below.
    
    ┌──────┬────┬────┬────┬────┬────┬────┬────┐
    │      │ A  │ B  │ C  │ D  │ E  │ F  │ G  │
    ├──────┼────┼────┼────┼────┼────┼────┼────┤
    │ A    │ -  │ 16 │ 12 │ 21 │ -  │ -  │ -  │
    ├──────┼────┼────┼────┼────┼────┼────┼────┤
    │ B    │ 16 │ -  │ -  │ 17 │ 20 │ -  │ -  │
    ├──────┼────┼────┼────┼────┼────┼────┼────┤
    │ C    │ 12 │ -  │ -  │ 28 │ -  │ 31 │ -  │
    ├──────┼────┼────┼────┼────┼────┼────┼────┤
    │ D    │ 21 │ 17 │ 28 │ -  │ 18 │ 19 │ 23 │
    ├──────┼────┼────┼────┼────┼────┼────┼────┤
    │ E    │ -  │ 20 │ -  │ 18 │ -  │ -  │ 11 │
    ├──────┼────┼────┼────┼────┼────┼────┼────┤
    │ F    │ -  │ -  │ 31 │ 19 │ -  │ -  │ 27 │
    ├──────┼────┼────┼────┼────┼────┼────┼────┤
    │ G    │ -  │ -  │ -  │ 23 │ 11 │ 27 │ -  │
    └──────┴────┴────┴────┴────┴────┴────┴────┘
    
    However, it is possible to optimise the network by removing some edges and
    still ensure that all points on the network remain connected. The network
    which achieves the maximum saving is shown below. It has a weight of 93,
    representing a saving of 243 − 93 = 150 from the original network.
    
    Using [1]network.txt, a 6K text file containing a network with forty
    vertices, and given in matrix form, find the maximum saving which can be
    achieved by removing redundant edges whilst ensuring that the network
    remains connected.
    
    Visible links
    1. network.txt
    p_107_1.gif
    p_107_2.gif
    Answer: b0db1202ec966e7855ca23626eb285b8
    
"""
from common import check

PROBLEM_NUMBER = 107
ANSWER_HASH = "b0db1202ec966e7855ca23626eb285b8"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
