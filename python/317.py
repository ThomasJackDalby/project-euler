"""
    Problem 317
    ===========
    
    A firecracker explodes at a height of 100 m above level ground. It breaks
    into a large number of very small fragments, which move in every
    direction; all of them have the same initial velocity of 20 m/s.
    
    We assume that the fragments move without air resistance, in a uniform
    gravitational field with g=9.81 m/s^2.
    
    Find the volume (in m^3) of the region through which the fragments move
    before reaching the ground. Give your answer rounded to four decimal
    places.
    
    Answer: b0e2bec93bfe598ade5d3d1141f76bdd
    
"""
from common import check
import math
from matplotlib import pyplot as plt

PROBLEM_NUMBER = 317
ANSWER_HASH = "b0e2bec93bfe598ade5d3d1141f76bdd"

# Only need to work out a slice, then can integrate.
# fire off at different angles. again only need to fire off from 0 to 90 (firing down is pointless.)

g = 9.81
sx = 0
sy = 20
z_step_size = 1
time_step = 0.001
v0 = 20
max_x = []
x = []
y = []

for elevation in [-90]:
    theta = elevation * math.pi / 180
    px = sx
    py = sy    
    vx = v0 * math.cos(theta * math.pi)
    vy = v0 * math.sin(theta * math.pi)

    while py > 0:
        px += time_step * vx
        py += time_step * vy
        
        vy -= time_step * 9.81

        x.append(px)
        y.append(py)

plt.plot(x, y)
plt.show()

check(None, PROBLEM_NUMBER, ANSWER_HASH)
