from timeit import default_timer as timer
from FibonacciLattice import FibonacciLattice
from graphviz import Graph

m = 3
n = 5
l3n = FibonacciLattice(m, n)

def dual(m, n, v):
    return tuple(m*n + 1 - k for k in v[::-1])

components1 = sorted(l3n.components[1], key=lambda x:min(sum(v) for v in x))
components2 = sorted(l3n.components[2], key=lambda x:min(sum(v) for v in x))

for idx, c1 in enumerate(components1):
    print(idx, len(c1), c1)

print()

for idx, c2 in enumerate(components2):
    print(idx, len(c2), c2)

print()

for i, c1 in enumerate(components1):
    other_set = components2 if n % 2 == 1 else components1
    for j, c2 in enumerate(other_set):
        c2p = set(dual(m, n, v) for v in c2)
        if c1 == c2p:
            print(i, "=", j)
        elif c2p < c1:
            print(i, ">", j)
        elif c1 < c2p:
            print(i, "<", j)

print()

g = Graph('G', filename='connectivity.gv', engine='circo')

for i, c1 in enumerate(components1):
    for j, c2 in enumerate(components2):
        if set(c1) & set(c2):
            g.edge(str(i) + "r", str(j) + "b")

g.view()
