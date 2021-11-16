import timeit

print(timeit.timeit('x**0.5','import random\nx=random.random()', number=100000))
print(timeit.timeit('math.sqrt(x)','import random, math\nx=random.random()', number=100000))